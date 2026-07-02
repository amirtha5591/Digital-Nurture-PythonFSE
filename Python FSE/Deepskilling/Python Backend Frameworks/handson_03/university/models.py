from django.db import models

class Department(models.Model):  # <-- Make sure 'Department' is capitalized exactly like this
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=15, unique=True)
    credits = models.IntegerField(default=3)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='courses')

    def __str__(self):
        return f"{self.code}: {self.title}"

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)
    grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} enrolled in {self.course.code}"