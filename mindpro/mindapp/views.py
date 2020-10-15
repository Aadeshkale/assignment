from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from mindapp.models import ManagerUser
from django.contrib.auth import authenticate, login

class SignupView(APIView):

    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']

            try:
                firstname = request.data['firstname']
            except:
                firstname = None

            try:
                lastname = request.data['lastname']
            except:
                lastname = None

            try:
                company = request.data['company']
            except:
                company = None

            user = ManagerUser.objects.create_user(
                email=email,
                password=password,
            )
            user.firstname = firstname,
            user.lastname = lastname,
            user.company = company,

            user.is_staff = True
            user.save()

        except Exception as e:
            print('Exception:', e)
            return Response("operation faild")

        return Response("Manager User created successfully :)")


class LoginView(APIView):

    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
            else:
                data = dict()
                data['Exception'] = "Invalid credentials"
                return Response(data)
        except Exception as e:
            data = dict()
            data['Exception'] = str(e)
            return Response(data)

        return Response("Manager Login successfully :)")


