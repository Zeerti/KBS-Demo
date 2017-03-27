from django.contrib import admin
from kbs_view.models import Document, Files
# Register your models here.


class DocumentAdmin(admin.ModelAdmin):
	list_display = ('title', 'date_modified', 'publisher', 'software_product')

class FilesAdmin(admin.ModelAdmin):
	list_display = ('file', 'document', 'upload_date')

admin.site.register(Document, DocumentAdmin)
admin.site.register(Files, FilesAdmin)
