from django.views.generic import *
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import *
from .forms import *

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

class note(DetailView):

    template_name = 'notes/note.html'
    model = Note
    context_object_name = 'note'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['form'] = NoteForm(self.request.POST, instance=self.object)
        else:
            context['form'] = NoteForm(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = NoteForm(request.POST, instance=self.object)
        if form.is_valid():
            note = form.save(commit=False)
            note.last_modified = datetime.datetime.now()  # Son düzenleme tarihini ayarla
            note.save()
            return self.get(request, *args, **kwargs)
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

    

def PageNFView(request, exception):
    print(request.build_absolute_uri())
    return render(request, "404.html", {"url": request.build_absolute_uri()}, status=404)
