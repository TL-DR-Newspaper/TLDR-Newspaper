from django.urls import path

from articles import views

urlpatterns = [
    path("<slug:slug>", views.article_by_slug, name="article_detail"),
    path("id/<int:id>", views.article_by_id, name="article_detail_by_id"),
    path("<slug:slug>/unpublish", views.unpublish_article, name="unpublish"),
    path("<slug:slug>/edit", views.edit_article, name="edit"),
    path("<slug:slug>/next", views.next_article, name="next"),
    ]