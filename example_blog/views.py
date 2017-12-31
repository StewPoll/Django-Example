from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Very basic index page. Not going to do anything fancy, just going to
    :param request:
    :return:
    """
    return render(request, template_name='index.html')