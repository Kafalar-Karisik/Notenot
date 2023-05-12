from django.views.generic import TemplateView
from notes.views import NoteListsView
from django.urls import path

from . import views

handler404 = "notes.views.PageNFView"


urlpatterns = [
    path("", views.index, name="index"),
    path("test/", NoteListsView.as_view()),
]