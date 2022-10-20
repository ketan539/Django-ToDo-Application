
from django.views import View
from django.shortcuts import render,redirect
from myapp.forms import taskform
from .models import task
from django.db.models import Q
from django.contrib import messages


class home(View):
    def get(self,request):
        form=taskform
        d={'form':form}
        return render(request,'home.html',d)
    def post(self,request):
        form=taskform(request.POST)
        if form.is_valid():
            form.save()
            messages.warning(request,'Task Saved Successfully')
            return redirect('home')

class list(View):
    def get(self,request):
        details=task.objects.all().order_by('-id')
        d={'details':details}
        return render(request,'list.html',d)
    def post(self,request):
        search=request.POST['search']
        query=Q(task__icontains=search) | Q(id__icontains=search)
        details=task.objects.filter(query)
        d={'details':details}
        return render(request,'list.html',d)

class delete(View):
    def get(self,request,eid):
        obj=task.objects.get(id=eid)
        obj.delete()
        messages.error(request,'Task Deleted Successfully')
        return redirect ('list')

class admin(View):
    def get(self,request):
        return redirect('admin')
    
