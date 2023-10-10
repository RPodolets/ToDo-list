from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from core.models import Task, Tag
from core.forms import TagForm, TaskForm


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponseRedirect(reverse("core:task_list"))


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags").order_by("is_done")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("core:tag_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("core:tag_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("core:tag_list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("core:task_list")

    def form_valid(self, form):
        form.deadline = ""
        return super().form_valid(form)


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("core:task_list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("core:task_list")


def task_toggle_completion(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, id=pk)
    if task:
        task.is_done = not task.is_done
        task.save()
    return HttpResponseRedirect(reverse("core:task_list"))
