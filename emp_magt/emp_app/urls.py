from django.contrib import admin
from rest_framework.authtoken.views import ObtainAuthToken
from django.urls import path, include
from emp_app.views import *
urlpatterns = [
    path('info/', EmpReg.as_view()),
    path('info/<str:id>/',EmpReg.as_view()),
    path('register/',EmpReg.as_view()),
    path('login/',EmpLogin.as_view()),
    path('get-token/',ObtainAuthToken.as_view()),
]