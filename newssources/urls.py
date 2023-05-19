from django.urls import path

from newssources import views

urlpatterns = [
    path("", views.get_news, name="fetch news"),
    ]