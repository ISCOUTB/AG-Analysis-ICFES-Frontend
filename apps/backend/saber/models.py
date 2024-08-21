from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class StudentResults(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    result_type = GenericForeignKey('content_type', 'object_id')


class Saber11Results(StudentResults):
    PUNT_ENGLISH = models.FloatField()
    PUNT_MATHEMATICS = models.FloatField()
    PUNT_SOCIAL_CITIZENSHIP = models.FloatField()
    PUNT_NATURAL_SCIENCES = models.FloatField()
    PUNT_CRITICAL_READING = models.FloatField()
    PUNT_GLOBAL = models.FloatField()


class SaberProResults(StudentResults):
    MOD_QUANTITATIVE_REASONING = models.FloatField()
    MOD_WRITTEN_COMMUNICATION = models.FloatField()
    MOD_CRITICAL_READING = models.FloatField()
    MOD_ENGLISH = models.FloatField()
    MOD_CITIZENSHIP_COMPETENCES = models.FloatField()


class Student(models.Model):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"

    GENRE = [
        (MALE, MALE),
        (FEMALE, FEMALE),
        (OTHER, OTHER)
    ]

    genre = models.CharField(max_length=20, choices=GENRE)
    results = models.OneToOneField(StudentResults, on_delete=models.CASCADE)


class Institution(models.Model):
    SABER11 = "SABER11"
    SABERPRO = "SABERPRO"

    REPORT_TYPE = [
        (SABER11, SABER11),
        (SABERPRO, SABERPRO)
    ]

    name = models.TextField()
    period = models.CharField(max_length=255)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE)
    students = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='students')


class Municipality(models.Model):
    name = models.CharField(max_length=255)


class Department(models.Model):
    name = models.CharField(max_length=255)
    municipalities = models.ForeignKey(
        Municipality, on_delete=models.CASCADE, related_name='departments')
