from django.http import HttpResponse

from .models import Note


# Create your views here.


def index(request):
    latest_notest_list = Note.objects.order_by("-pub_date")[:5]
    output = ""

    for i in latest_notest_list:
        output = output + f"{i.title}: <br>{i.note}" + "<br><br>"

    return HttpResponse(output)
