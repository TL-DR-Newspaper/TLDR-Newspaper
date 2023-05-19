from django.urls import path

from homepage import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("faq/", views.faq, name="faq"),
    path("funding/", views.funding, name="funding"),
    path("ai/", views.responsibleai, name="ai"),
    ]