from django.contrib import admin

from .models import Challenge, Category, Answer

# Register your models here.

@admin.register(Challenge)
class ChallengesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')

@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'challenge', 'user')
