from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from kbs_view.models import Document, Files

def index(request):
	# Request the context of the request.
    # The context contains information such as the client's machine details, for example.
	context = RequestContext(request)

	document_list = Document.objects.all()
	context_dict = {'boldmessage': "SITE IS CURRENTLY UNDER CONSTRUCTION! PLEASE ALLOW 360 ANT LIGHT YEARS FOR COMPLETION", 'documents': document_list } #Each comma indiates new information that needs to be passed. Can be infinitly long I think?

	
	#document_dict = {}

	return render(request, 'kbs_view/index.html', context_dict)

def about(request):
	
	context = RequestContext(request)

	return render(request, 'kbs_view/about.html')

def documents(request, document_name_url):

	context = RequestContext(request)

	document_name_url = document_name_url.replace('_', ' ')

	context_dict = {'document_name': document_name}

	try:
		#.get raises a DoesNotExist exception if document doesn't exist.null=
		#.get method returns one model instance or raises the exception
		document = Document.obgjects.get(name=document_name)

		#Retrieve all the associated Files
		#Filter returns >= 1 model instance
		files = Files.objects.filter(document=document)

		# We'll use this in the template to verify that the file exists.
		context_dict['files'] = files
		# We'll use this in the template to verify that the document exists.
		context_dict['document'] = document
	except Document.DoesNotExist:
		pass


	return render(request, 'kbs_view/documents.html', context_dict)