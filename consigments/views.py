from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Consigments, Areas
from .forms import ConsigmentForm, FilterAreaForm

# Create your views here.
def cons_list(request, order=None, filters=None):
    order = request.GET.get('order')
    filters = request.GET.get('filters')
    if order == None:
        order = 'letter_code'
    cons = Consigments.objects.order_by(order)
    if filters != None:
        filters_id = get_object_or_404(Areas, name=filters)
        cons = cons.filter(business_area=filters_id)
    areas = Areas.objects.all()
    return render(request, 'consigments/cons_list.html', {'cons': cons, 'areas': areas})

@login_required
def add_cons(request):
    if request.method == "POST":
        form = ConsigmentForm(request.POST)
        if form.is_valid():
            cons = form.save(commit=False)
            cons.modified_by = request.user
            cons.modified_date = timezone.now()
            cons.save()
            return redirect('cons_list')
    else:
        form = ConsigmentForm()
    return render(request, 'consigments/add_cons.html', {'form': form})

@login_required
def edit_cons(request, pk):
    cons = get_object_or_404(Consigments, pk=pk)
    if request.method == "POST":
        form = ConsigmentForm(request.POST, instance=cons)
        if form.is_valid():
            cons = form.save(commit=False)
            cons.modified_by = str(request.user)
            cons.modified_date = timezone.now()
            cons.save()
            return redirect('cons_list')
    else:
        form = ConsigmentForm(instance=cons)
    return render(request, 'consigments/add_cons.html', {'form': form})
