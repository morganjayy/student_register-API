from rest_framework import serializers
from attendance.models import Student, Register

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','name', 'email_address', 'phone', 'date', 'age', 'address', 'course')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        # exclude = []
        fields = ('id', 'name', 'date', 'attendance')
        # extra_kwargs = {
        #     'name': {'required':True},
        #     'date': {'required':True},
        #     'attendance': {'required':True},
        # }
        
        