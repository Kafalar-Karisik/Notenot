from django.contrib import admin

from .models import Note


# Register your models here.

class AdminV(admin.ModelAdmin):

    fieldset = [
        (None, {"fields": ["title"]}),
        ("Edit Note", {"fields": ["note"]}),
    ]

    list_display = ["title","pub_date", "was_published_recently"]


admin.site.register(Note, AdminV)
