import logging
from django.shortcuts import render, redirect
from django.db.models import Count
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, View
from django.views.decorators.http import require_http_methods
from django.core import serializers
from .decorators import ajax_login_required

from .models import Video, Comment

logger = logging.getLogger("videos")

class VideoListView(ListView):
    model=Video
    template_name="videos/list.html"
    paginate_by = 10

class VideoDetailView(DetailView):
    model=Video
    template_name="videos/detail.html"
    query_set=Video.objects.all()
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
        video.save()
        
        return super().render_to_response(context, **response_kwargs)

@login_required
@require_http_methods(["POST"])
def comment_video(request, youtube_id):
    logger.info("comment a video: %s", youtube_id)
    user_logged=request.user
    x=Video.objects.get(youtube_id=youtube_id)
    
    comment_req=request.POST.get("comment")
    
    comment=Comment.objects.create(
        video=x,
        user=user_logged,
        comment=comment_req
    )

    return redirect(reverse_lazy("videos:detail", kwargs={"slug": x.slug}))

@ajax_login_required
@require_http_methods(["POST"])
def like_video(request, youtube_id):
    logger.info("like to video: %s", youtube_id)
    user_logged=request.user

    video = Video.objects.filter(youtube_id=youtube_id).first()

    if not video:
        return JsonResponse({'error': 'invalid video id'}, status=400)

    video.likes.add(user_logged)

    video.save()

    data={
        "ok": "Like saved"
    }

    return JsonResponse(data)

@login_required
@require_http_methods(["POST"])
def dislike_video(request, youtube_id):
    logger.info("disliked to video: %s", youtube_id)
    user_logged=request.user

    video=Video.objects.filter(youtube_id=youtube_id, active=True)[0]
    

    video.dislikes.add(user_logged)

    video.save()
   
    data={
        "ok": "Dislike saved"
    }

    return JsonResponse(data)
