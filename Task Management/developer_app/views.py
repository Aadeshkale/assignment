from django.shortcuts import render,redirect
from django.views import View
from developer_app.models import TaskInfo
from django.http.response import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views.generic import RedirectView











class IndexView(View):
    def get(self,request):
        return render(request,'index.html')


class DeveloperLoginView(View):
    def get(self,request):
        return render(request,'developer_login.html')

    def post(self,request):

        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request,user)

            return redirect('developer_dashboard')
            # return HttpResponse("User is authenticated")
        else:
            return HttpResponse("Invalid user")


class DeveloperDashBoard(LoginRequiredMixin,View):
    login_url = '/developer_app/login'
    redirect_field_name = ''
    def get(self,request):
        current_user = request.user
        current_user_id =  current_user.id
        current_username = current_user.username
        tasks = TaskInfo.objects.filter(assign_developer=current_user_id)

        return render(request,'developer_dashboard.html',{'user':current_username,'tasks':tasks})


class ModifyTaskInfo(LoginRequiredMixin,View):
    login_url = '/developer_app/login'
    redirect_field_name = ''

    def get(self,request,id):
        current_user = request.user
        current_username = current_user.username
        return render(request,'developer_edit_task.html',{'user':current_username})

    def post(self,request,id):
        current_user = request.user
        current_username = current_user.username
        user_commit = request.POST['user_comment']
        task_status = request.POST['task_status']

        try:
            obj = TaskInfo.objects.get(id=id)
        except Exception as e:
            print('exception is there:',e)
            return HttpResponse("Something went to wrong :(")


        obj.user_commit = user_commit
        obj.status = task_status
        obj.save()

        return HttpResponse("Details Updated successfully")



class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/developer_app/login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class SnsView(View):

    def get(self,request):
        print(request)
        print('--'*20)
        print(request.GET)
        print('--'*20)
        print(request.body)
        return HttpResponse("ok")

    def post(self, request):
        print(request)
        print('--' * 20)
        print(request.POST)
        print('--' * 20)
        print(request.body)
        return HttpResponse("ok")
