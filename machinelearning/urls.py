from django.urls import path
from machinelearning import views

urlpatterns = [
    path("findsimilar", views.analyse, name="analyse news"),
    path("summarize", views.create_summaries, name="summarize news"),
    ]