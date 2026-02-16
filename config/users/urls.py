from django.urls import path
from .views import JobListAPIView
urlpatterns=[
    path('jobs/',JobListAPIView.as_view(),name='job-list'),
]