from django.urls import path

from . import views

handler404 = "notes.views.PageNFView"

app_name = 'notes'

urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.NoteListsView.as_view()),
    path("<int:id>/", views.note.as_view(), name="note")
]
