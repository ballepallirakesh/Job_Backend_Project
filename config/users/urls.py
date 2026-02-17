from django.urls import path
from .views import JobListCreateAPIView,JobDetailView
urlpatterns=[
    path('jobs/',JobListCreateAPIView.as_view()),
    path('jobs/<int:id>',JobDetailView.as_view()),
]