from django.urls import path
from employee.views import *

urlpatterns = [
    path('',edm_home,name="edm_home"),
    path('add/',add_employee,name="add_employee"),
    path('singup/',singup_employee,name="singup_employee"),
    path('<int:id>/details/',details_employee,name="details_employee"),
    path('<int:id>/edit/',edit_employee,name="edit_employee"),
    path('<int:id>/delete/',delete_employee,name="delete_employee"),
]