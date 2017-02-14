from django.shortcuts import render

from .models import GlobalObjects, Category
# Create your views here.
def globlist(request):
    glob_list = GlobalObjects.objects.all()
    category = Category.objects.all()
    
    return render(request, 'glob_obj/glob_list.html', {'glob_list': glob_list, 'cats': category})

def search(request):
    filters = request.GET['q']
    query = GlobalObjects.objects.filter(eng__contains=filters)
    category = Category.objects.all()
    
    return render(request, 'glob_obj/glob_list.html', {'glob_list': query, 'cats': category})