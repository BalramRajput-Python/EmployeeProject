from django.shortcuts import render,redirect,get_object_or_404
from employee.forms import Employee_Form,Employee_Form2
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from employee.models import Register
from django.contrib.auth import authenticate,login,logout

@login_required(login_url="/login/")
def edm_home(request):
  x    = request.user
  role = Register.objects.get(user_id=x.id)
  data = User.objects.all() 
  data2 = Register.objects.all()

  context = {'data':data,'data2':data2,'role':role,'x':x}
  return render(request,'employee/home.html',context)

@login_required(login_url="/login/")
def details_employee(request,id=None):
  data = Register.objects.get(user_id=id)
  return render(request,'employee/details.html',{'data':data})


@login_required(login_url="/login/")
def edit_employee(request,id=None):

  data = get_object_or_404(User,id=id)
  data2 = get_object_or_404(Register,user_id=id)

  if request.method == "POST":
    employee_form = Employee_Form(request.POST,instance=data)
    employee_form2 = Employee_Form2(request.POST,instance=data2)

    if employee_form.is_valid() and employee_form2.is_valid():
      employee_form.save()
      employee_form2.save() 
    else:
      context ={'error':'you edit a invalid data here'}
      return render(request,'employee/edit.html',context)
    return redirect('edm_home')

  else:    
    employee_form = Employee_Form(instance=data)
    employee_form2 = Employee_Form2(instance=data2)

    context = {
      'employee_form':employee_form,
      'employee_form2':employee_form2,
      'data':data
    }                                                      
    return render(request,'employee/edit.html',context)

@login_required(login_url="/login/")
def add_employee(request):
  x    = request.user
  role = Register.objects.get(user_id=x.id)

  if role.user_type == "HR":  
    if request.method =="POST":
      E1 = Employee_Form(request.POST)
      E2 = Employee_Form2(request.POST)

      if E1.is_valid() and E2.is_valid():
        ES1 = E1.save(commit=False)
        ES1.set_password(ES1.password)
        ES1.save()

        ES2 = E2.save(commit=False)
        ES2.user = ES1  
        ES2.save()
      return redirect('edm_home')

    else:
      context = {
        'employee_form':Employee_Form,
        'employee_form2':Employee_Form2
      } 
      return render(request,'employee/add.html',context)
  
  else:
    return redirect('edm_home')


def delete_employee(request,id=None):
  user = get_object_or_404(User,id=id)
  user.delete()
  return redirect('edm_home')

# Login Function 
def employee_login(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']

    user= authenticate(username=username,password=password)
    if user:
      login(request,user)
      if request.GET.get('next',None):  
        return redirect(request.GET['next'])
      return redirect("edm_home")
    else:
      context = {'error':'Provide a valid Username and Password'}
      return render(request,'employee/login.html',context)

  return render(request,'employee/login.html')

def singup_employee(request): 

  if request.method =="POST":
    E1 = Employee_Form(request.POST)
    E2 = Employee_Form2(request.POST)

    if E1.is_valid() and E2.is_valid():
        ES1 = E1.save(commit=False)
        ES1.set_password(ES1.password)
        ES1.save()
        
        ES2 = E2.save(commit=False)
        ES2.user = ES1
        ES2.save()
    return redirect('employee_login')
  
  else:
    context={
      'employee_form' : Employee_Form(),
      'employee_form2': Employee_Form2()
    }
    return render(request,'employee/singup.html',context)
    

def employee_logout(request):
  logout(request)
  return redirect('employee_login') 