from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world !")

from django.shortcuts import render,redirect
from .models import Details
# Create your views here.
def indexhtml(request):
    return render(request,'index.html')

def create(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        phone=request.POST['phone']
        obj=Details.objects.create(name=name,age=age,phone=phone)
        obj.save()
        return redirect('/')


def retrieve(request):
    details=Details.objects.all()
    return render(request,'retrieve.html',{'details':details})


from .forms import detailsform
def edit(request,id):
    object=Details.objects.get(id=id)
    return render(request,'edit.html',{'object':object})

def update(request,id):
    object=Details.objects.get(id=id)
    form=detailsform(request.POST,instance=object)
    if form.is_valid:
        form.save()
        object=Details.objects.all()
        return redirect('retrieve')

def delete(request,id):
    Details.objects.filter(id=id).delete()
    return redirect('retrieve')
