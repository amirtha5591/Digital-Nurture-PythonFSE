from rest_framework import generics
from .models import Department, Course
from .serializers import DepartmentSerializer, CourseSerializer

# Handles GET (List all) and POST (Create new) for Departments
class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# Handles GET (Retrieve), PUT (Update), and DELETE for a single Department
class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.get_queryset()
    serializer_class = DepartmentSerializer

# Handles GET and POST for Courses
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer