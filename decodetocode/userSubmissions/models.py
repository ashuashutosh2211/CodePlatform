from django.db import models
from django.utils import timezone
from problems.models import Problem  
from django.contrib.auth.models import User 

class UserSubmission(models.Model):
    submission_id = models.AutoField(primary_key=True)  
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)  
    user_handle = models.ForeignKey(User, on_delete=models.CASCADE) 
    language = models.CharField(max_length=50)  
    verdict = models.CharField(max_length=20) 
    timestamp = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return f"Submission {self.submission_id} for Problem {self.problem.problem_id} by {self.user_handle.username}"
