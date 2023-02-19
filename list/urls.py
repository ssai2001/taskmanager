from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('task_status/<int:id>',views.update_status,name="up_status"),
    path('task_deletion/<int:id>',views.delete_task,name="del_task")
]
