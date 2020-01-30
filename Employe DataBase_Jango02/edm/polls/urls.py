from django.urls import path
from polls.views import *

urlpatterns = [
    path('',polls_index,name="polls_index"),
    path('AddQuestion/',polls_addquestion,name="polls_addquestion"),
    path('<int:id>/view/',polls_viewquestion,name="polls_viewquestion"),
    path('<int:id>/edit/',polls_editquestion,name="polls_editquestion"),
    path('<int:id>/delete/',polls_delete_question,name="polls_deletequestion"),

    path('<int:id>/EmployeeTest/',employee_test,name="employee_test"),

]