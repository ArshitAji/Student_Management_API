from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from StudApp.models import StudentDb
from StudApp.serializers import UserSerializer,StudentSerializer

from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated


class RegistrationView(APIView):
    def post(self,request):
        serializer_instance=UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class StudentListCreateView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        student_obj=StudentDb.objects.all()
        serializer_instance=StudentSerializer(student_obj,many=True)
        return Response(serializer_instance.data)
    
    def post(self,request):
        serializer_instance=StudentSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class StudentRetrieveUpdateDeleteView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request,pk):
        student_obj=get_object_or_404(StudentDb,id=pk)
        serializer_instance=StudentSerializer(student_obj)
        return Response(serializer_instance.data)

    def put(self,request,pk):
        student_obj=get_object_or_404(StudentDb,id=pk)
        serialzer_instance=StudentSerializer(student_obj,data=request.data)
        if serialzer_instance.is_valid():
            serialzer_instance.save()
            return Response(serialzer_instance.data)
        else:
            return Response(serialzer_instance.errors)

    def delete(self,request,pk):
        student_obj=get_object_or_404(StudentDb,id=pk)
        student_obj.delete()
        return Response({
            "Message":"Deleted Successfully"
        })

class logout(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        request.user.auth_token.delete()
        return Response({
            "Message":"Logout Successfully..!"
        })



