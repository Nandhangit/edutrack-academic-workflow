from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CourseSerializer,EnrollmentSerializer
from .models import Course,Enrollment

class CourseViewSet(ModelViewSet):
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class EnrollmentViewSet(ModelViewSet):
    
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
