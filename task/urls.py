from django.urls import path
from . import views as vs

urlpatterns = [
    path('', vs.task_list, name='task_list'),
    path('newtask/', vs.newtask, name='new-task'),
    path('task/<int:id>/', vs.taskview, name='task-view'),
    path('edit/<int:id>/', vs.edittask, name='edit-task'),
    path('delete/<int:id>/', vs.deletetask, name='delete-task'),
]
