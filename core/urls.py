from django.urls import path

from core.views import (
    TaskListView,
    index,
    TagListView,
    TagCreateView,
    TagDeleteView,
    TagUpdateView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    task_toggle_completion
)

urlpatterns = [
    path("", index, name="index"),

    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags/create", TagCreateView.as_view(), name="tag_create"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag_update"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag_delete"),

    path("task_list/", TaskListView.as_view(), name="task_list"),
    path("task_list/create", TaskCreateView.as_view(), name="task_create"),
    path("task_list/<int:pk>/update", TaskUpdateView.as_view(), name="task_update"),
    path("task_list/<int:pk>/delete", TaskDeleteView.as_view(), name="task_delete"),

    path("task_toggle_completion/<int:pk>/", task_toggle_completion, name="task_toggle_completion")
]

app_name = "core"
