from django.contrib import admin
from .models import Account, Video, Comment, Like


class AccountCommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class VideoCommentInline(admin.TabularInline):
    model = Comment


class AccountLikeInline(admin.TabularInline):
    model = Like
    extra = 1


class VideoLikeInline(admin.TabularInline):
    model = Like
    extra = 1


class AccountAdmin(admin.ModelAdmin):
    inlines = [AccountCommentInline, AccountLikeInline]


class VideoAdmin(admin.ModelAdmin):
    inlines = [VideoCommentInline, VideoLikeInline]


admin.site.register(Account, AccountAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Comment)
admin.site.register(Like)
