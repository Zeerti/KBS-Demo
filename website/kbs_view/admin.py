from django.contrib import admin
from django.db import models
from kbs_view.models import Document, Files

from markdownx.widgets import AdminMarkdownxWidget
# Register your models here.


class DocumentAdmin(admin.ModelAdmin):
	list_display = ('title', 'date_modified', 'publisher')

class FilesAdmin(admin.ModelAdmin):
	list_display = ('file', 'document', 'upload_date')

class DocumentAdminTest(admin.ModelAdmin):

	list_display = ('title', 'date_modified', 'publisher')

	formfield_overrides = {
		models.TextField: {'widget': AdminMarkdownxWidget}
	}

admin.site.register(Document, DocumentAdminTest)
admin.site.register(Files, FilesAdmin)
