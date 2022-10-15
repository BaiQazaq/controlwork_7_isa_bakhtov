from django.contrib import admin

from webapp.models import Record

# Register your models here.

class RecordAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "email", "text", "status",  "created_at")
    list_filter = ("id", "author", "email", "text", "created_at")
    search_fields = ("author", "status")
    fields = ("author", "email", "text", "status", "created_at", "changed_at")
    readonly_fields = ("id", "created_at", "changed_at")

admin.site.register(Record, RecordAdmin)