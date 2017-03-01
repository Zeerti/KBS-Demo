# Create your views here.
from django.http import Http404
from django.shortcuts import render
from .models import Album

#/music/
def index(request):
	all_albums = Album.objects.all()
	return render(request, 'music/index.html', { 'all_albums' : all_albums } )

#/music/<album_id>/
#/music/2/
def detail(request, album_id):
	try:
		album = Album.objects.get(pk = album_id)
	except Album.DoesNotExist:
		raise Http404("Album Does Not Exist")
	return render(request, 'music/detail.html', { 'album' : album })
