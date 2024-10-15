from django.urls import path 
from .views import addSubmission
urlpatterns = [
    path('addSubmission/' , addSubmission , name='add_submission')
]