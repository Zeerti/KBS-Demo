from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from kbs_view.models import Document, Files
from django.views import generic

from django.views.generic.base import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView

from kbs_view.forms import MyForm



def index(request):
	document_list = Document.objects.all().order_by('title')
	num_documents = Document.objects.all().count()
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] =  num_visits + 1
	context_dict = {'boldmessage': "SITE IS CURRENTLY UNDER CONSTRUCTION! PLEASE ALLOW 360 ANT LIGHT YEARS FOR COMPLETION",
					'documents': document_list,
					'num_documents':num_documents,
					'num_visits': num_visits }

	return render(request, 'index.html', context_dict)

def about(request):
	return render(request, 'about.html')


class DocumentListView(LoginRequiredMixin ,generic.ListView):
	model = Document
	#context_object_name = 'my_context_name'  #Your own name for the list as a template variable
	#queryset = Document.objects.filter(title__icontains='test')[:5] #get 5 documents that contain the title war
	#template_name = 'kbs_view/my_template_name_list.html' #specify your own template name/location

	#this override allows you to pass additional content variables to the template
	'''
	 def get_context_data(self, **kwargs):
        Call the base implementation first to get a context
        context = super(BookListView, self).get_context_data(**kwargs)
        Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context
	'''
     #ALWAYS DO AS FOLLOWS WHEN USING THIS METHOD
     	#1. Get existing content from super class
     	#2. Add new context information
     	#3. Return new updated context


class DocumentDetailView(LoginRequiredMixin, generic.DetailView, FormView):
	model = Document

	template_name = "kbs_view/document_detail.html"
	form_class = MyForm
	success_url ="/"
	
	def document_detail_view(request, pk):
		try:
			document_id=Document.objects.get(pk=pk)
		except Document.DoesNotExist:
			raise Http404("Document does not exist")

		#document_id=get_object_or_404(Document, pk=pk)

		return render(
			request,
			'kbs_view/document_detail.html',
			context={'document':document_id},

		)


