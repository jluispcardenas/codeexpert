import logging
from datetime import date, timedelta
from itertools import chain

from django.utils import timezone
from django.shortcuts import render, redirect

from django.db import transaction
from django.db.models import Sum, Count, F, ExpressionWrapper, IntegerField, Case, When
from django.db.models.expressions import RawSQL

from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, View
from django.views.decorators.http import require_http_methods
from django.core import serializers

from .decorators import ajax_login_required
from .models import Video, Comment, Popularity

logger = logging.getLogger("videos")

POPULARITY_LIKE_VIDEO = 10
POPULARITY_DISLIKE_VIDEO = -5
POPULARITY_COMMENT_VIDEO = 1

class VideoListView(ListView):
    model=Video
    template_name="videos/list.html"
    paginate_by = 10
    # filtrar por activos
    queryset=Video.objects.filter(active=True)


class VideoDetailView(DetailView):
    model=Video
    template_name="videos/detail.html"
    # filtrar por activos
    queryset=Video.objects.filter(active=True)
    slug_field="slug"
    slug_url_kwarg="slug"

    def get_context_data(self, **kwargs):
        ContextOfTheView=super().get_context_data(**kwargs)

        video=self.get_object()

        likes=Video.objects.filter(youtube_id=video.youtube_id).aggregate(dislikes_count=Count('dislikes'), likes_count=Count('likes'))

        ContextOfTheView["comments"]=Comment.objects.filter(video=video)
        ContextOfTheView["likes"]=likes
        return ContextOfTheView


    def render_to_response(self, context, **response_kwargs):
        video=self.get_object()
        video.views=video.views + 1

        # Task number: 8
        user_logged = self.request.user
        if user_logged.is_authenticated:
            video.history.add(user_logged)

        video.save()
        
        return super().render_to_response(context, **response_kwargs)

# Task number: 1
class PopularListView(ListView):
  
    template_name = 'videos/popular.html'

    def get_queryset(self):
        # get items from the last month, order them by popularity, give a boost to the most recent ones
        # Task number: 5 
        last_month = date.today() - timedelta(days=30)
        populars = Popularity.objects.values('video').filter(created__gte=last_month).annotate(points_sum=Sum(F('points')+(ExpressionWrapper(timezone.now().date()-F('created'), IntegerField())*-100))).order_by('-points_sum')
        #populars = Popularity.objects.values('video_id').filter(created__gte=last_month).annotate(points_sum=RawSQL('SUM(points+(DATEDIFF(NOW(), created)*-100))', ())).order_by('-points_sum')
        populars = populars.all()[:5]
        
        video_ids = [elem["video"] for elem in populars]
        points = []
        [points.append(el["points_sum"]) for el in populars if el["points_sum"] not in points]
        
        order = Case(*[When(id=pk, then=pos) for pos, pk in enumerate(video_ids)], default=999999)
        videos = Video.objects.filter(id__in=video_ids, active=True).order_by(order).all()
        count = videos.count()
    
        # In case that all videos have the same popularity points, choose five videos at random. 
        # Task number: 6
        if len(points) < 2:
            videos = Video.objects.order_by('?').all()[:5]
        # if the count is less than 5, fill with random videos
        # Task number: 7
        elif count < 5:
            limit = 5-count
            videos = list(chain(videos, Video.objects.filter(active=True).order_by('?')[:limit]))
        
        return videos

# Task number: 8
class HistoryListView(ListView):
    model = Video
    template_name = "videos/history.html"
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user

        return Video.history.through.objects.filter(user=user).order_by('-id')

@login_required
@require_http_methods(["POST"])
def comment_video(request, youtube_id):
    logger.info("comment a video: %s", youtube_id)
    user_logged=request.user
    video=Video.objects.get(youtube_id=youtube_id)
    
    comment_req=request.POST.get("comment")
    
    comment=Comment.objects.create(
        video=x,
        user=user_logged,
        comment=comment_req
    )

    # Task number: 4
    update_popularity(video, POPULARITY_COMMENT_VIDEO)

    return redirect(reverse_lazy("videos:detail", kwargs={"slug": x.slug}))

@ajax_login_required
@require_http_methods(["POST"])
def like_video(request, youtube_id):
    logger.info("like to video: %s", youtube_id)
    user_logged = request.user

    video = Video.objects.filter(youtube_id=youtube_id, active=True).first()

    if not video:
        return JsonResponse({'error': 'invalid video id'}, status=400)

    if not video.likes.through.objects.filter(user=user_logged,video=video).exists():
        video.likes.add(user_logged)

        video.save()

        # Task number: 2
        if video.likes:
            update_popularity(video, POPULARITY_LIKE_VIDEO)
    
        data = {"ok": "Like saved"}
    else:
        data = {"error": "Not saved"}

    return JsonResponse(data)

@login_required
@require_http_methods(["POST"])
def dislike_video(request, youtube_id):
    logger.info("disliked to video: %s", youtube_id)
    user_logged=request.user

    video = Video.objects.filter(youtube_id=youtube_id, active=True).first()
    if not video:
        return JsonResponse({'error': 'invalid video id'}, status=400)

    if not video.dislikes.through.objects.filter(user=user_logged,video=video).exists():
        video.dislikes.add(user_logged)
    
        video.save()

        # Task number: 3
        update_popularity(video, POPULARITY_DISLIKE_VIDEO)

        data={"ok": "Dislike saved"}
    else:
        data={"error": "Not saved"}

    return JsonResponse(data)


def update_popularity(video, points):
    today = date.today()
    with transaction.atomic():
        popularity = Popularity.objects.select_for_update().filter(video=video,created=today).first()
        if not popularity:
            popularity = Popularity.objects.create(
                video=video,
                created=today
            )
        
        popularity.points += points

        popularity.save()