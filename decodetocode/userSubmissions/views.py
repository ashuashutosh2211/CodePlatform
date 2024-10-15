from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .models import UserSubmission
from .serializers import UserSubmissionSerializer
# Create your views here.

@api_view(['POST'])
def addSubmission(request):
    serializer = UserSubmissionSerializer(data=request.data)
    if serializer.is_valid():
        submission= serializer.save()
        print(submission.submission_id)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
