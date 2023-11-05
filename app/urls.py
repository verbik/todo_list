from django.urls import path

from app.views import (IndexView,
                       TaskCreateView,
                       TaskUpdateView,
                       TaskDeleteView,
                       TaskCompletionUpdateView,
                       )

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
    )
]

app_name = "app"
