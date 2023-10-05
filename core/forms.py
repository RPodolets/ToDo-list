from django import forms

from core.models import Tag, Task


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name",)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

        widgets = {
            'deadline': forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'})
        }
