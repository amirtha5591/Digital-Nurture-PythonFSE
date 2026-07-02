from django.contrib import admin
from django.urls import path
from university.views import DepartmentListCreateView, DepartmentDetailView, CourseListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/departments/', DepartmentListCreateView.as_view()),
    path('api/departments/<int:pk>/', DepartmentDetailView.as_view()),
    path('api/courses/', CourseListCreateView.as_view()),
]