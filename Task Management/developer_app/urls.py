from django.urls import path
from developer_app.views import *

urlpatterns = [
    path('login', DeveloperLoginView.as_view(), name='developer_login'),
    path('dashboard', DeveloperDashBoard.as_view(), name='developer_dashboard'),
    path('dashboard/<str:id>', ModifyTaskInfo.as_view(), name='edit_dashboard'),
    path('logout', LogoutView.as_view(), name='developer_logout'),
    path('sns/', SnsView.as_view(), name="aws_sns"),
]