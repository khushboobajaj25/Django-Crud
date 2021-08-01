from django.shortcuts import render,HttpResponseRedirect
from enroll.forms import StudentModelForm
from enroll.models import Student
# Create your views here.

#This function will add new item and display all items
def add_show(request):

    #  print(request)
   if request.method == 'POST':

      fm = StudentModelForm(request.POST)
      if fm.is_valid():
         print('yes')
         # fm.save()
         nm = fm.cleaned_data['name']
         em = fm.cleaned_data['email']
         pa = fm.cleaned_data['password']
         reg = Student(name=nm, email=em, password=pa)
         reg.save()
   

    
   fm = StudentModelForm()
   stud = Student.objects.all()
   return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})

#This function will delete
def delete_data(request,id):
   if request.method == 'POST':
      detail = Student.objects.get(pk=id)
      detail.delete()
      return HttpResponseRedirect('/')

#This function will  update
def update_data(request,id):
   if request.method == 'POST':
      data = Student.objects.get(pk=id)
      fm = StudentModelForm(request.POST,instance = data)
      if fm.is_valid():
         fm.save()
   else:
      data = Student.objects.get(pk=id)
      fm = StudentModelForm(instance=data)
   return render(request,'enroll/update.html',{'form':fm})


