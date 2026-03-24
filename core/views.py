from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from django.http import JsonResponse


def home_api(request):
    return JsonResponse({
        "hero_title": "Welcome from Backend 🚀",
        "hero_subtitle": "Django + React Connected",
        "hero_description": "Now it works!"
    })
# Pages
class HomePageView(generics.RetrieveAPIView):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer

    def get_object(self):
        return HomePage.objects.first()

class AboutPageView(generics.RetrieveAPIView):
    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializer

    def get_object(self):
        return AboutPage.objects.first()

class ServicesPageView(generics.RetrieveAPIView):
    queryset = ServicesPage.objects.all()
    serializer_class = ServicesPageSerializer

    def get_object(self):
        return ServicesPage.objects.first()


# Courses
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'category', 'level']


class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


# Jobs
class JobPositionViewSet(viewsets.ModelViewSet):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['job_type', 'location', 'status']


# Forms
class ContactSubmissionView(generics.CreateAPIView):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer


class AdmissionFormSubmissionView(generics.CreateAPIView):
    queryset = AdmissionFormSubmission.objects.all()
    serializer_class = AdmissionFormSubmissionSerializer