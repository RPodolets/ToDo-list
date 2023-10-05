from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from core.models import Task


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "base.html")


class TaskListView(generic.ListView):
    model = Task
