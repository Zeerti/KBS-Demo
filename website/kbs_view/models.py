from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField


# Create your models here.
class Document(models.Model):
	BRINK = 'BR'
	PIXEL = 'PX'
	SIVA = 'SV'
	HERITAGE = 'HR'

	SOFTWARE_CHOICES = (
		(BRINK, 'Brink'),
		(PIXEL, 'Pixel'),
		(SIVA, 'Siva'),
		(HERITAGE, 'Heritage'),
	)

	title = models.CharField(max_length=128,
							 unique=True, verbose_name='Document Title')
	body = MarkdownxField(help_text='Enter the detailed information for this KBS Document')
	date_modified = models.DateField(auto_now=True, editable=False)
	publisher = models.CharField(max_length=50, default="Zoidberg") #Needs to update with each change
	software_product = models.CharField(
					   max_length=2,
					   choices = SOFTWARE_CHOICES,
					   default = BRINK,
					   help_text='Select the software regarding this KBS Document',
					   verbose_name='Software Product')
	favorited = models.BooleanField(default=False, verbose_name='Favorited?', editable=False)
	views = models.IntegerField(default=0, help_text='Number of times this document has been viewed.', editable=False) 
	
	
	
	def get_absolute_url(self):
		'''
		Returns the url to access a particular instance of MyModelName
		first argument is the name of the URL mapper for example:
		url(r'^document/(?P<pk>\d+)$', views.DocumentDetailView.as_view(), name='document-detail'),
		'''
		return reverse('document-detail', args=[str(self.id)])

	def __str__(self):
		return self.title

class Files(models.Model):
	document = models.ForeignKey(Document)
	file = models.FileField()
	upload_date = models.DateField(auto_now=True, editable=False)

	def __str__(self):
		return self.file.name

