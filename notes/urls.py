from django.views.generic import TemplateView
from django.urls import path

from . import views

handler404 = "notes.views.PageNFView"


urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.NoteListsView.as_view()),
]