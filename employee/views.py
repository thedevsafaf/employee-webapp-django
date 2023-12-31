from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

#display all employees list
def employees_list(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'employee/list.html', context)


#create employee method
def create_employee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees-list')
        else:
            form = EmployeeForm()
    
    context = {
        'form': form,
    }  
    return render(request, 'employee/create.html', context)


#edit employee method
def edit_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees-list')
        
    context = {
        'form' : form,
        'employee': employee,
    }
    return render(request, 'employee/edit.html', context)


#delete employee method
def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employees-list')
    
    context = {
        'employee':employee,
    }

    return render(request, 'employee/delete.html', context)

