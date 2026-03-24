from django.db import models

# -----------------------------
# Pages
# -----------------------------
class HomePage(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True)

class AboutPage(models.Model):
    content = models.TextField()
    founder_name = models.CharField(max_length=100)
    founder_image = models.ImageField(upload_to='about/')

class ServicesPage(models.Model):
    content = models.TextField()


# -----------------------------
# Courses
# -----------------------------
class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='instructors/')

class Course(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)


# -----------------------------
# Careers
# -----------------------------
class JobPosition(models.Model):
    title = models.CharField(max_length=200)
    job_type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    description = models.TextField()


# -----------------------------
# Forms
# -----------------------------
class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)


class AdmissionFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    document = models.FileField(upload_to='admissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)