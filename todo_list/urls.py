from django.urls import path

from todo_list.views import TaskListView, TaskCreateView, TaskUpdateView, \
    TaskDeleteView, change_task_status, TagListView, TagUpdateView, \
    TagDeleteView, TagCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create-task/", TaskCreateView.as_view(), name="task-create"),
    path("update-task/<int:pk>/", TaskUpdateView.as_view(),
         name="task-update"),
    path("delete-task/<int:pk>/", TaskDeleteView.as_view(),
         name="task-delete"),
    path("task-status/<int:pk>/<action>", change_task_status,
         name="task-status"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("update-tag/<int:pk>/", TagUpdateView.as_view(),
         name="tag-update"),
    path("delete-tag/<int:pk>/", TagDeleteView.as_view(),
         name="tag-delete"),
    path("create-tag/", TagCreateView.as_view(), name="tag-create"),
]

app_name = "todo_list"
