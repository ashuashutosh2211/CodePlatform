# Generated by Django 5.1.1 on 2024-10-08 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('problem_id', models.AutoField(primary_key=True, serialize=False)),
                ('problem_statement', models.TextField()),
                ('constraint', models.TextField()),
                ('sample_testcases', models.JSONField()),
                ('example_test_case_explanation', models.TextField()),
                ('tags', models.CharField(max_length=255)),
                ('test_cases', models.JSONField()),
                ('problem_rating', models.FloatField()),
            ],
        ),
    ]
