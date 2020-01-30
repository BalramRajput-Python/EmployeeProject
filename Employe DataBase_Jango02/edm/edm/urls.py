from django.contrib import admin
from django.urls import path,include
from employee.views import *
from polls.views import *

urlpatterns = [
    path('admin/', admin.site.urls),        
    path('edm/',include('employee.urls')),
    path('polls/',include('polls.urls')),

    path('login/',employee_login,name="employee_login"),
    path('logout/',employee_logout,name="employee_logout"),
]








