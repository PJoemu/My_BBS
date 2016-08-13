from django.contrib import admin
import models


# Register your models here.
@admin.register(models.BbsPost)
class BbsPostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'summary', 'view_count', 'ranking', 'content', 'create_time', 'modify_time')
    list_filter = ('title', 'author')
    search_fields = ('title', 'author__user__username')


@admin.register(models.BbsUser)
class BbsUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'signature', 'user_email')
    fields = ['user', 'signature', 'head_img']

    def user_email(self, obj):
        return obj.user.email
