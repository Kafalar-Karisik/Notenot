from django.views.generic import ListView
from django.http import HttpResponse
from django.template import loader
from .models import Note


# Create your views here.


def index(request):
    latest_notest_list = Note.objects.order_by("-pub_date")[:5]
    # output = ""
    template = loader.get_template("notes/notes.html")

    # for i in latest_notest_list:
    #    output = output + f"{i.title}: <br>{i.note}" + "<br><br>"

    context = {"output": latest_notest_list}

    return HttpResponse(template.render(context, request))


class NoteListsView(ListView):
    template_name = "notes/notes.html"
    model = Note
    ordering = "-pub_date"
    context_object_name = "output"
