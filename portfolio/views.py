
# Create your views here.

from django.shortcuts import render

def home_page_view(request):
	return render(request, 'portfolio/home.html')
