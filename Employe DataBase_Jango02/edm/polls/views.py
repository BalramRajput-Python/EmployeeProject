from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from employee.models import Register
from polls.forms import Question_Form
from polls.models import Questions

#this function is for the find the user_role of admin which login in the the data
#there is diff between the basic 
def user_role(request):
  user = request.user
  user = Register.objects.get(user_id=user.id)
  return (user.user_type)


@login_required(login_url="/login/")
#Index page of polls groups 
def polls_index(request):
  role = user_role(request)
  questions = Questions.objects.all()
  context={
    'questions':questions,
    'user_role':role
  }
  return render(request,'polls/index.html',context)



@login_required(login_url="/login/")
#Ask Question in the basic way to find the basic work to get the basic ability to 
def polls_addquestion(request):
  role = user_role(request)
  if role == "HR":
    if request.method =="POST":
      Q1 = Question_Form(request.POST)

      if Q1.is_valid():
        Q1.save()
      return redirect('polls_addquestion')

    else:
      return render(request,'polls/addQuestion.html',{"Question_Form":Question_Form})
  else:
    return redirect('polls_index')



@login_required(login_url="/login/")

def polls_viewquestion(request,id=None):

  Q = Questions.objects.get(id=id)
  return render(request,'polls/views.html',{'Q':Q})



@login_required(login_url="/login/")

def polls_editquestion(request,id=None):
  Q =get_object_or_404(Questions,id=id)
  
  if request.method =="POST":
    question_save = Question_Form(request.POST,instance=Q)
    if question_save.is_valid():
      question_save.save()
    else:
      context ={"error":"Please Insert The Data"}
      return render(request,'polls/editQuestion.html',context)
    return redirect("polls_index")
  
  else:
    question_form = Question_Form(instance=Q)
    return render(request,'polls/editQuestion.html',{'question_form':question_form})



@login_required(login_url="/login/")

def polls_delete_question(request,id=None):

  Q = get_object_or_404(Questions,id=id)
  Q.delete()
  return redirect("polls_index")


@login_required(login_url="/login/")
def employee_test(request,id=None):
  
  Q = Questions.objects.all()
  context={
    'Q':Q
  }
  return render(request,'polls/test.html',context)