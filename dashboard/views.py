from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count

from .models import CIR, Clockwork, Changes, Updates, Queries, Answers, Defects
from .forms import CirForm, ChangeForm
# Create your views here.
#manager info
def manager_dash(request):
    cirs = CIR.objects.filter(allocated=False)
    clockwork = Clockwork.objects.all()
    updates = Updates.objects.all()
    your_people = Changes.objects.values('allocated').annotate(total_points=Sum('point'), count=Count('name_of_change')) #name, sum points group by name
    deadlines = Changes.objects.filter(status="op")

    return render(request, 'dashboard/manager.html', {'cirs': cirs, 'clockwork': clockwork, 'updates': updates, 'people': your_people, 'deadlines': deadlines})

def tech_dash(request):
    changes = Changes.objects.filter(allocated = 'Ferenc')
    cirs = CIR.objects.filter(allocated_to = 1)
    queries = Defects.objects.all()
    return render(request, 'dashboard/technicians.html', {'changes': changes, 'cirs': cirs, 'queries': queries})

def your_changes(request, name):
    changes = Changes.objects.filter(allocated = name)
    return render(request, 'dashboard/your_changes.html', {'changes': changes, 'name': name })

def change_detail(request, pk):
    change = get_object_or_404(Changes, pk=pk)
    return render(request, 'dashboard/change_detail.html', {'change': change})

def cir_detail(request, pk):
    cir = get_object_or_404(CIR, pk=pk)
    if request.method == "POST":
        form = CirForm(request.POST, instance=cir)
        if form.is_valid():
            cir = form.save(commit=False)
            cir.save()
            return redirect('dashboard/cir_detail.html', pk=cir.pk)
    else:
        form = CirForm(instance=cir)
    return render(request, 'dashboard/cir_detail.html', {'form': form})
