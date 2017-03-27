from django.db import models


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
	body = models.TextField(help_text='Enter the detailed information for this KBS Document')
	date_modified = models.DateField(auto_now=True, editable=False)
	publisher = models.CharField(max_length=50, default="Zoidberg") #Needs to update with each change
	software_product = models.CharField(
		max_length=2,
		choices = SOFTWARE_CHOICES,
		default = BRINK,
		help_text='Select the software regarding this KBS Document',
		verbose_name='Software Product',
	)
	favorited = models.BooleanField(default=False, verbose_name='Favorited?', editable=False)
	views = models.IntegerField(default=0, help_text='Number of times this document has been viewed.', editable=False) 
	
	#Uploaded Documents


	def __str__(self):
		return self.title

	#def __unicode__(self):
	#	return self.title + ' -- ' + self.date_modified

class Files(models.Model):
	document = models.ForeignKey(Document)
	file = models.FileField()
	upload_date = models.DateField(auto_now=True, editable=False)

	def __str__(self):
		return self.file.name
