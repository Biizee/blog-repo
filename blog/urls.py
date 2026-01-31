from django.urls import path
import blog.views as blog_views

urlpatterns = [
    path("", blog_views.post_list, name="posts_list"),
    path("<int:post_id>/", blog_views.get_post_by_id, name="post_details"),
    path("authors/", blog_views.author_list, name="authors_list"),
    path("authors/<int:author_id>/", blog_views.get_post_by_author_id, name="authors_posts"),
]
