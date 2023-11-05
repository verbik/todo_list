from django.urls import path

from app.views import (IndexView,
                       TaskCreateView,
                       TaskUpdateView,
                       TaskDeleteView,
                       TaskCompletionUpdateView,
                       TagListView,
                       TagCreateView,
                       TagDeleteView,
                       TagUpdateView)

urlpatterns = [
    path(
        "",
        IndexView.as_view(),
        name="index"
    ),
    path(
        "create_task/",
        TaskCreateView.as_view(),
        name="create-task"
    ),
    path(
        "<int:pk>/update_task/",
        TaskUpdateView.as_view(),
        name="update-task"
    ),
    path(
        "<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="delete-task"
    ),
    path(
        "<int:pk>/is_done_update/",
        TaskCompletionUpdateView.as_view(),
        name="update-task-completion"
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    )
]

app_name = "app"
