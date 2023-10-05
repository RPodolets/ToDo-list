from django.urls import path

from core.views import TaskListView, index

urlpatterns = [
    path("", index, name="index"),
    # path("list/", TaskListView.as_view(), "task_list")
]

app_name = "core"
