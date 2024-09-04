from django.contrib import admin

from translate.models import Translations, Language, Project, Project_Language

class ListTranslations(admin.ModelAdmin):
    list_display = ("id", "id_project", "strategy", "id_language", "value")
    list_display_links = ("id", "id_project",)
    search_fields = ("id_project",)
    list_filter = ("strategy",)
    list_per_page = 10

admin.site.register(Translations, ListTranslations)

class ListLanguage(admin.ModelAdmin):
    list_display = ("id", "name", "rtl_direction")
    list_display_links = ("id",)
    search_fields = ("id",)
    list_filter = ("name",)
    list_per_page = 10

admin.site.register(Language, ListLanguage)

class ListProject(admin.ModelAdmin):
    list_display = ("id", "name", "export_strategy")
    list_display_links = ("id",)
    search_fields = ("id", "name",)
    list_filter = ("name",)
    list_per_page = 10

admin.site.register(Project, ListProject)

class ListProjectLanguage(admin.ModelAdmin):
    list_display = ("id", "id_project", "id_language")
    list_display_links = ("id", "id_project",)
    search_fields = ("id", "id_project", "id_language",)
    list_filter = ("id_project", "id_language",)
    list_per_page = 10

admin.site.register(Project_Language, ListProjectLanguage)
