from django.http import HttpResponse

# Create your views here.
def home_page_view(request):
    return HttpResponse("This is the home page!")
