from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer
class JobListCreateAPIView(APIView):
    #get all objects
    def get(self,request):
        jobs=Job.objects.all()
        serializer=JobSerializer(jobs,many=True)
        return Response(serializer.data)
    #post create
    def post(self,request):
        serializer=JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_created)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class JobDetailView(APIView):
    def get_object(self,id):
        try:
            return Job.objects.get(id=id)
        except Job.DoesNotExist:
            return None 
    def get(self,request,id):
        job=self.get_object(id)
        if not job:
            return Response({"error":"job not found"},status=404)
        serializer=JobSerializer(job)
        return Response(serializer.data)
    def put(self,request,id):
        job=self.get_object(id)
        if not job:
            return Response({"error":"job not found"},status=404)
        serializer=JobSerializer(job,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    def delete(self,request,id):
        try:
           job=Job.objects.get(id=id)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=404)
        job.delete()
        return Response({"message":"job deleted"},status=204)
            

# Create your views here.
