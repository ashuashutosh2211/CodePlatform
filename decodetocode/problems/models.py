from django.db import models

# Create your models here.

class Problem(models.Model):
    problem_id = models.AutoField(primary_key=True)  
    problem_statement = models.TextField()            
    constraint = models.TextField()                  
    sample_testcases = models.JSONField()                  
    example_test_case_explanation = models.TextField() 
    tags = models.CharField(max_length=255)         
    test_cases = models.JSONField()                
    problem_rating = models.FloatField()
    def __str__(self):
        return f"Problem {self.problem_id}: {self.problem_statement[:50]}..." 
