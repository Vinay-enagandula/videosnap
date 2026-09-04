from django.contrib import admin
# pyrefly: ignore [missing-import]
from .models import *
admin.site.register(Video)
admin.site.register(VideoComment)
admin.site.register(VideoLike)
admin.site.register(VideoShare)


