from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count

from .models import CIR, Clockwork, Changes, Updates, Queries, Answers, Defects
# Create your views here.
#manager info
def manager_dash(request):
    cirs = CIR.objects.filter(allocated=False)
    clockwork = Clockwork.objects.all()
    updates = Updates.objects.all()
    your_people = Changes.objects.values('allocated').annotate(total_points=Sum('point'), count=Count('name_of_change')) #name, sum points group by name
    deadlines = Changes.objects.filter(status='Open')

    return render(request, 'dashboard/manager.html', {'cirs': cirs, 'clockwork': clockwork, 'updates': updates, 'people': your_people, 'deadlines': deadlines})

#technician info
