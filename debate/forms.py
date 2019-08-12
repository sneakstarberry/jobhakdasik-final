from django import forms
from .models import Debate_Comment

class Debate_CommentForm(forms.ModelForm):
    class Meta:
        model = Debate_Comment
        fields = ('debate_author', 'debate_text','debate_author')