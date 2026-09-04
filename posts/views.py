from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
# pyrefly: ignore [missing-import]
from .models import Post, PostImage


# Display all posts
def posts_view(request):
    posts = Post.objects.all()
    return render(request, "post/posts.html", {"posts_all": posts})


# Create a new post
def create_post_view(request):

    if request.method == "POST":
        title_variable = request.POST.get("title.html")
        content_variable = request.POST.get("content.html")

        # Create the post
        post = Post.objects.create(
            title_model=title_variable,
            content_model=content_variable
        )

        # Get all uploaded images
        images = request.FILES.getlist("images")

        # Save each image
        for image in images:
            PostImage.objects.create(
                post=post,
                image=image
            )

        return redirect("posts")

    return render(request, "post/create_posts.html")