from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from core.views import home_api

router = DefaultRouter()
router.register('courses', views.CourseViewSet)
router.register('instructors', views.InstructorViewSet)
router.register('jobs', views.JobPositionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/home/', home_api),
    path('home/', views.HomePageView.as_view()),
    path('about/', views.AboutPageView.as_view()),
    path('services/', views.ServicesPageView.as_view()),

    path('contact/', views.ContactSubmissionView.as_view()),
    path('admission/', views.AdmissionFormSubmissionView.as_view()),
]