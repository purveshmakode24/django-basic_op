from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Employee
# Create your views here.
def home(request):
	return render(request, 'home.html')

def submit(request):
	e_name = request.POST.get('name')
	e_salary = request.POST.get('salary')
	try:
		obj = Employee(ename=e_name, esalary=e_salary)
		obj.save() 
	except Exception as e:
		print(e)
	
	return HttpResponse("<h1 style=\"color:green\">Form successfully submitted!</h1>")
   

def show(request):
	# return render(request,'show.html')
	mydata=Employee.objects.all()
	my_dict={
		'data': mydata
	}

	return render(request,'show.html',my_dict)

def delete(request):
	del_entry = request.POST.getlist('datatodelete')

	for item in del_entry:
		Employee.objects.filter(ename=item).delete()

	return HttpResponse("<h1>Data has been Deleted!</h1>")

def update(request):
	name = request.POST.get('name')
	newsalary = request.POST.get('newsalary')
	Employee.objects.filter(ename=name).update(esalary=newsalary)

	return HttpResponse("<h1>Employee salary has been updated!</h1>")