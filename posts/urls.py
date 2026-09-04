from django.urls import path
# pyrefly: ignore [missing-import]
from . import views
urlpatterns = [
    path("posts/",views.posts_view,name="posts"),
    path("create_posts/",views.create_post_view,name="create_posts")
    
        

]
