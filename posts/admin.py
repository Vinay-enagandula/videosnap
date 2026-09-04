from posts.models import Post,PostImage

from django.contrib import admin
# pyrefly: ignore [missing-import]
from .models import *

admin .site.register(Post)
admin .site.register(PostImage)
