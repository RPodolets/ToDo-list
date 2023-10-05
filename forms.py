from django import forms

from core.models import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name",)
