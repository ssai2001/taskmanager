from django.shortcuts import render,redirect
from django.http import HttpResponse
from list.models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='signin')
def index(request):
    if request.method == "POST":
        task_name = request.POST.get('t_name')
        task_details = request.POST.get('t_details')

        print(task_name)
        print(task_details)

        try:
            task = Task.objects.create(
                user = request.user,
                task_name = task_name,
                task_description = task_details
            )
            task.save()
        except Exception as e:
            print(e)
        tasks = Task.objects.filter(user=request.user).order_by("-id")
        context = {
            'task' : tasks
        }
        return render(request,'list/index.html',context)
    # del_task()
    tasks = Task.objects.filter(user=request.user).order_by("-id")
    context = {
        'task' : tasks
    }
    # for t in tasks:
    #     print(t.id)
    #     print(t.task_name)
    return render(request,'list/index.html',context)

@login_required(login_url='signin')
def update_status(request,id):
    task = Task.objects.get(id=id)
    if(task.task_status):
        Task.objects.filter(id=id).update(task_status=False)
    else:
        Task.objects.filter(id=id).update(task_status=True)
    return redirect('index')

@login_required(login_url='signin')
def delete_task(request,id):
    Task.objects.get(id=id).delete()
    return redirect('index')
