from emp_app.models import Employee
from emp_app.serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class EmpReg(APIView):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self,request,id=None):
        if id:
            data = Employee.objects.get(id=id)
            serial = EmployeeSerializer(data)
            return Response(serial.data)
        else:
            data = Employee.objects.all()
            serial = EmployeeSerializer(data, many=True)
            return Response(serial.data)

    def post(self, request):
        data = request.data
        serial = EmployeeSerializer(data=data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=201)
        else:
            return Response({'error':'invalid data'}, status=404)
    
    def put(self,request,id):
        info = request.data
        data = Employee.objects.get(id=id)
        serial = EmployeeSerializer(data, data=info, partial=True)
        if serial.is_valid():
            serial.save()
            return Response({'message': 'data is updated'}, status=200)
        else:
            return Response({"error": "data is not valid"}, status=404)

    def delete(self,request,id):
        data = Employee.objects.get(id=id)
        data.delete()
        return Response({"message": "data deleted successfully"}, status=200)

class EmpLogin(APIView):
    def post(self,request):
        data = request.data
        username = request.data['username']
        password = request.data['password']
        info = Employee.objects.get(username=username)
        if info.password == password:
            return Response({'msg':'Login successfully'},status=200)
        else:
            return Response({'msg':'Invalid username or password'},status=404)
