from django.shortcuts import render

# Create your views here.
def road_map(request):
    return render(request, 'roadmap/HTML.html')