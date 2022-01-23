from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from projects.models import *

@admin.register(post)
class post(ImportExportModelAdmin):
    """ Column lists to be displayed in the admin """

    search_fields = ('title',)

    list_display = (
                    'author',
                    'title',
                    'description',
                    'photo',
                    'created',
                    'modified',
                    )

