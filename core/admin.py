from django.contrib import admin
from .models import (
    HomePage, AboutPage, ServicesPage,
    Instructor, Course,
    JobPosition,
    ContactSubmission, AdmissionFormSubmission
)

# Pages
admin.site.register(HomePage)
admin.site.register(AboutPage)
admin.site.register(ServicesPage)

# Courses
admin.site.register(Instructor)
admin.site.register(Course)

# Jobs
admin.site.register(JobPosition)

# Forms
admin.site.register(ContactSubmission)
admin.site.register(AdmissionFormSubmission)