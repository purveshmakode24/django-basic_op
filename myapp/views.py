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
	
	return HttpResponse("Form successfully submitted!")
   

def show(request):
	# return render(request,'show.html')
	mydata=Employee.objects.all()
	my_dict={
		'data': mydata
	}

	return render(request,'show.html',my_dict)