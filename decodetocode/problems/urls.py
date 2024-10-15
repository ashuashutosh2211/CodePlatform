from django.urls import path 
from .views import addProblem, getProblem


urlpatterns = [
    path('addProblem/', addProblem, name='add_problem'),
    path('getProblem/', getProblem, name='get_problems'), 
    path('getProblem/<int:problem_id>/', getProblem, name='get_problem_by_id'),
]   