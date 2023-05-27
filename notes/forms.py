from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ['last_modified']  
        fields = ['title', 'note','last_modified']
