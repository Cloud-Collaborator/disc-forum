from django.contrib import admin
from .models import(
    Topic,
    UserProfile,
    Thread,
    ThreadPosts
)

# Register your models here.

admin.site.register(Topic)
admin.site.register(UserProfile)
admin.site.register(Thread)
admin.site.register(ThreadPosts)
