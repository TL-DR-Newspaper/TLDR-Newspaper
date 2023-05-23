from django.urls import path

from articles import views

urlpatterns = [
    path("<slug:slug>", views.article_by_slug, name="article_detail"),
    path("id/<int:id>", views.article_by_id, name="article_detail_by_id"),
    path("<slug:slug>/unpublish", views.unpublish_article, name="unpublish"),
    path("<slug:slug>/edit", views.edit_article, name="edit"),
    path("<slug:slug>/next", views.next_article, name="next"),
    path("mobileapi/random", views.random_article, name="random"),
    path("mobileapi/sources", views.mobile_api_data_sources, name="mobile api sources"),
    path("mobileapi/recent", views.mobile_api_data_recent, name="mobile api recent"),
    path("mobileapi/all", views.mobile_api_data_all, name="mobile api recent"),

    ]