from django.shortcuts import render
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required
from .models import Album, Image

# Create your views here.


# a view to handle album upload
@login_required
def album(request):
	Image