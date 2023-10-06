from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from attendance.models import Student, Register
from attendance.serializers import StudentSerializer, RegisterSerializer
from rest_framework.reverse import reverse
from django.http import Http404
from rest_framework.permissions import AllowAny
from rest_framework.schemas import SchemaGenerator
from django.http import HttpResponse
from django.template import loader


class StudentList(APIView):
    """
    This list all existing students and register new students
    """
    def get(self, request, format=None):
        """
        Fetch all students information in the academy 
        """
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True )
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        To register a new student. Create a new student profile
        ---
            parameters:
                    ---
                    - name: name
                    description: student's name
                    required: True
                    type: string
                    paramType: form
                    ---
                    - email_address: email
                    description: student's email address
                    required: True
                    type: string
                    paramType: form
                    ---
                    - phone: phone
                    description: student's phone number
                    required: True
                    type: int
                    paramType: form
                    ---
                    - date: date
                    description: date joined
                    required: False
                    type: string
                    paramType: form
                    ---
                    - age: age
                    description: student's age
                    required: True
                    type: int
                    paramType: form
                    ---
                    - address: address
                    description: student's home address
                    required: True
                    type: string
                    paramType: form
                    ---
                    - course: course
                    description: course to study in academy
                    required: True
                    type: string
                    paramType: form
                    ---
        """
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetail(APIView):
    """
    Retrieve, update, delete a student detail
    """
    def get_object(self,pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        """
        Retrieve a student data in the academy
        """
        # student = self.get_object(id=pk)
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        """
        To update student detail. Make changes to existing information
         ---
            parameters:
                    ---
                    - name: name
                    description: student's name
                    required: True
                    type: string
                    paramType: form
                    ---
                    - email_address: email
                    description: student's email address
                    required: True
                    type: string
                    paramType: form
                    ---
                    - phone: phone
                    description: student's phone number
                    required: True
                    type: int
                    paramType: form
                    ---
                    - date: date
                    description: date joined
                    required: False
                    type: string
                    paramType: form
                    ---
                    - age: age
                    description: student's age
                    required: True
                    type: int
                    paramType: form
                    ---
                    - address: address
                    description: student's home address
                    required: True
                    type: string
                    paramType: form
                    ---
                    - course: course
                    description: course to study in academy
                    required: True
                    type: string
                    paramType: form
                    ---
        """
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        """
        Delete a student profile from database
        """
        student = Student.objects.filter(id=pk)
        student.delete()
        return Response({'message': 'deleted sucessfully'},status=status.HTTP_200_OK)
    

class RegisterList(APIView):
    """
    List all existing attendance and register new student attendance
    """
    def get(self, request, format=None):
        """
        Fetch all existing attendance from database
        """
        register = Register.objects.all()
        serializer = RegisterSerializer(register, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        """
        To create a new attendance. Handles new attendance 
        ---
            parameters:
                    ---
                    - name: name
                    description: student's name
                    required: True
                    type: string
                    paramType: form
                    ---
                    - date: date
                    description: present date of classes
                    required: False
                    type: string
                    paramType: form
                    ---
                    - attendance: attendance
                    description: present/absent
                    required: True
                    type: string
                    paramType: form
                    ---
        """ 

        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ResgisterDetail(APIView):
    """
    Retrieve, update, delete an attendance wrongly inputed
    """
    def get_object(self, request, pk, format=None):    
        try:
            return Register.objects.get(pk=pk)
        except Register.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        """
        Retrieve a student attendance
        """
        # register = self.get_object(id=pk) 
        register = get_object_or_404(Register, id=pk)
        serializer = RegisterSerializer(instance=register)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        """
        Update existing attendance
        ---
            parameters:
                    ---
                    - name: name
                    description: student's name
                    required: True
                    type: string
                    paramType: form
                    ---
                    - date: date
                    description: present date of classes
                    required: False
                    type: string
                    paramType: form
                    ---
                    - attendance: attendance
                    description: present/absent
                    required: True
                    type: string
                    paramType: form
                    ---
        """
        # register = self.get_object(pk)
        register = get_object_or_404(Register, id=pk)
        serializer = RegisterSerializer(register, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        """
        Delete an attendance from database
        """
        register = Register.objects.filter(id=pk)
        register.delete()
        return Response({'message': 'deleted sucessfully'},status=status.HTTP_200_OK)




