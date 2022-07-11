from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from todo_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    ordering = ["completed", "-created_at"]


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("todo_list:task-list")
    fields = "__all__"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo_list/task_delete_form.html"
    success_url = reverse_lazy("todo_list:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo_list/tag_delete_form.html"
    success_url = reverse_lazy("todo_list:tag-list")


def change_task_status(request, pk, action):
    task = Task.objects.get(pk=pk)
    if action == "undo":
        task.completed = False
        task.save()
    elif action == "complete":
        task.completed = True
        task.save()

    return HttpResponseRedirect(reverse_lazy("todo_list:task-list"))
