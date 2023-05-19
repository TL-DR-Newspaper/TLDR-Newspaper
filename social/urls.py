from django.urls import path

from social import views

urlpatterns = [
    path("reddit/<str:subreddit>/<int:id>", views.post_to_reddit, name="post to reddit"),
    ]