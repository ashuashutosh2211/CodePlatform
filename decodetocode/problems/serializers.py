from rest_framework import serializers
from .models import Problem

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['problem_statement', 'constraint', 'sample_testcases',
                  'example_test_case_explanation', 'tags', 'problem_rating' , 'test_cases']
