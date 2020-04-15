from django.db import models


class Mineral(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image_filename = models.CharField(max_length=255, blank=True, null=True)
    image_caption = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    formula = models.TextField(blank=True, null=True)
    strunz_classification = models.CharField(
        max_length=255, blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    crystal_system = models.CharField(max_length=255, blank=True, null=True)
    unit_cell = models.TextField(blank=True, null=True)
    crystal_symmetry = models.TextField(blank=True, null=True)
    cleavage = models.CharField(max_length=255, blank=True, null=True)
    mohs_scale_hardness = models.TextField(blank=True, null=True)
    luster = models.TextField(blank=True, null=True)
    streak = models.CharField(max_length=255, blank=True, null=True)
    diaphaneity = models.CharField(max_length=255, blank=True, null=True)
    optical_properties = models.CharField(
        max_length=255, blank=True, null=True)
    refractive_index = models.TextField(blank=True, null=True)
    crystal_habit = models.TextField(blank=True, null=True)
    specific_gravity = models.TextField(blank=True, null=True)
    group = models.CharField(max_length=255, blank=True, null=True)
