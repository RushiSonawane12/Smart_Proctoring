# Generated by Django 3.0.5 on 2024-05-04 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_course_examsubmitted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='examSubmitted',
        ),
    ]
