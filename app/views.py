from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from app.models import Task


class IndexView(generic.ListView):
    model = Task
    template_name = "app/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("app:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("app:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("app:index")


class TaskCompletionUpdateView(generic.View):
    model = Task
    fields = ("is_done",)

    @staticmethod
    def post(request, *args, **kwargs) -> redirect:
        task = get_object_or_404(Task, pk=kwargs["pk"])
        if task.is_done:
            task.is_done = False
        else:
            task.is_done = True

        task.save()
        return redirect("app:index")

