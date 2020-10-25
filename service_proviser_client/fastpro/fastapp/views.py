from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User,Group
from django.http.response import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views.generic import RedirectView
from fastapp.models import Services


class IndexView(View):
    def get(self,request):
        return render(request,'index.html')


class ServiceProviderLoginView(View):

    def get(self, request):
        return render(request, 'service_provider_login.html')

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('service_provider_dashboard')
            # return HttpResponse("User is authenticated")
        else:
            return HttpResponse("Invalid user")


class ServiceProviderDashboardView(LoginRequiredMixin,View):
    login_url = 'service_provider_login'
    redirect_field_name = ''

    def get(self, request):
        current_user = request.user
        current_user_id = current_user.id
        current_username = current_user.username

        res = current_user.groups.filter(name='service_providers').exists()
        if res:

            return render(request, 'service_provider_dashboard.html', {'user': current_username})

        else:
            return HttpResponse('User Is Invalid')

    def post(self,request):

        service_name = request.POST['ser_name']
        service_discription = request.POST['ser_dis']
        contact_email = request.POST['contact_email']
        current_user = request.user
        service_provider_id = current_user.id
        obj=Services.objects.create(service_name=service_name,
                                    service_discription=service_discription,
                                    contact_email=contact_email,
                                    service_provider_id=service_provider_id)
        obj.save()
        return HttpResponse('Service is added :)')


class ServiceProviderLogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = ''

    def get(self, request, *args, **kwargs):
        logout(request)
        super(ServiceProviderLogoutView, self).get(request, *args, **kwargs)
        return redirect('service_provider_login')



class ClientLoginView(View):

    def get(self, request):
        return render(request, 'client_login.html')

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('client_dashboard')
            # return HttpResponse("User is authenticated")
        else:
            return HttpResponse("Invalid user")


class ClientDashBoardView(LoginRequiredMixin,View):

    login_url = 'client_login'
    redirect_field_name = ''

    def get(self, request):
        current_user = request.user
        current_user_id = current_user.id
        current_username = current_user.username
        res = current_user.groups.filter(name='client').exists()
        services = Services.objects.all()
        if res:
            return render(request, 'client_dash_board.html', {'user': current_username,'services':services })
        else:
            return HttpResponse('User Is Invalid')


class ClientLogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = ''

    def get(self, request, *args, **kwargs):
        logout(request)
        super(ClientLogoutView, self).get(request, *args, **kwargs)
        return redirect('client_login')