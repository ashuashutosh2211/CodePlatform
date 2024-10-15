from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Problem
from .serializers import ProblemSerializer

@api_view(['POST'])
def addProblem(request):
    serializer = ProblemSerializer(data=request.data)
    if serializer.is_valid():
        problem = serializer.save()  
        return JsonResponse({
            "message": "Problem added successfully",
            "problem_id": problem.problem_id 
        }, status=status.HTTP_201_CREATED)
    
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getProblem(request, problem_id=None):
    if problem_id is not None:
        try:
            problem = Problem.objects.get(problem_id=problem_id)
            serializer = ProblemSerializer(problem)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except Problem.DoesNotExist:
            return JsonResponse({"detail": "Problem not found."}, status=status.HTTP_404_NOT_FOUND)
    
    # If no specific problem_id is provided, return all problems
    problems = Problem.objects.all()
    serializer = ProblemSerializer(problems, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)