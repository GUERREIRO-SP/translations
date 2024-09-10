from django.db import models
from .generate_uuid import get_a_uuid


class Language(models.Model):

    id = models.CharField(max_length=25, null = False, blank = False, primary_key=True, editable=False)
    name = models.CharField(max_length=100, null = False, blank = False)
    rtl_direction = models.BooleanField(default=False)

    # Retorna o valor do registro...
    def __str__(self):
        return f"Language: [{self.id}]"   


class Project(models.Model):

    id = models.CharField(max_length=36, null = False, blank = False, primary_key=True, default=get_a_uuid, editable=False)
    name = models.CharField(max_length=255, null = False, blank = False)
    export_strategy = models.CharField(max_length=255, null = True, blank = True)

    # Retorna o valor do registro...
    def __str__(self):
        return f"Project: [{self.name}]"


class ProjectLanguage(models.Model):

    id = models.CharField(max_length=36, null = False, blank = False, primary_key=True, default=get_a_uuid, editable=False)
    id_project = models.CharField(max_length=36, null = False, blank = False)
    id_language = models.CharField(max_length=25, null = False, blank = False)
    txt_limit = models.IntegerField()

    # Retorna o valor do registro...
    def __str__(self):
        return f"Project Language: [{self.id_project}]"   


class Translations(models.Model):

    STRATEGY_OPTIONS = [
        ("ChatGPT", "ChatGPT"),
        ("Google", "Google"),
        ("Manual", "Manual"),
        ]

    id = models.CharField(max_length=36, null = False, blank = False, primary_key=True, default=get_a_uuid, editable=False)
    id_project = models.CharField(max_length=36, null = False, blank = False)
    id_language = models.CharField(max_length=25, null = False, blank = False)
    strategy = models.CharField(max_length=255, choices=STRATEGY_OPTIONS)
    key = models.CharField(max_length=255, null = True, blank = False)
    context = models.CharField(max_length=1000, null = True, blank = True)
    value = models.CharField(max_length=1000, null = False, blank = False)
    override_en = models.CharField(max_length=1000, null = True, blank = True)
    flag_export = models.BooleanField(default=False)

    # Retorna o valor do registro...
    def __str__(self):
        return f"Translate: [{self.value}]"
