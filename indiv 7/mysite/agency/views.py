from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect

from .form import AgencyForm
from .models import Agency


def index(request):
    agency_list = Agency.objects.all()
    context = {
        "agency_list": agency_list,
    }
    return render(request, 'agency/index.html', context)

def detail(request, agency_id):
    agency = get_object_or_404(Agency, id=agency_id)
    return render(request, "agency/detail.html", {"agency": agency})


def edit_agency(request, agency_id):
    agency = get_object_or_404(Agency, id=agency_id)
    if request.method == 'POST':
        form = AgencyForm(request.POST, instance=agency)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AgencyForm(instance=agency)
    return render(request, 'agency/edit_agency.html', {'form': form})

def add_agency(request):
    if request.method == 'POST':
        form = AgencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AgencyForm()
    return render(request, 'agency/add_agency.html', {'form': form})