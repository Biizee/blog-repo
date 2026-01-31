from django.shortcuts import render
from blog.models import Post, Author, Comment

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts_list": posts,
    }
    return render(
        request,
        template_name = "blog/posts_list.html",
        context=context,
    )

def get_post_by_id(request, post_id):
    post = Post.objects.get(id = post_id)
    comments = Comment.objects.filter(post = post_id)
    context = {
        "post": post,
        "comments": comments,
    }
    return render(
        request,
        template_name="blog/post_details.html",
        context=context,
    )

def author_list(request):
    authors = Author.objects.all()
    context = {
        "authors_list": authors,
    }
    return render(
        request,
        template_name = "blog/authors_list.html",
        context=context,
    )

def get_post_by_author_id(request, author_id):
    posts = Post.objects.filter(author = author_id)
    context = {
        "posts_list": posts,
    }
    return render(
        request,
        template_name="blog/authors_posts.html",
        context=context,
    )
