from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from inbox.models import *

@admin.register(message)
class message(ImportExportModelAdmin):
    """ Column lists to be displayed in the admin """
    
    search_fields = ('contact_full_name',)

    list_display = (
        'contact_full_name',
        'phone_number',
        'email',
        'message',
        'date',
    )
