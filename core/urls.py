from django.urls import path

from core.views import TaskListView, index, TagListView, TagCreateView, TagDeleteView, TagUpdateView

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags/create", TagCreateView.as_view(), name="tag_create"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag_delete"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag_update")
]

app_name = "core"
