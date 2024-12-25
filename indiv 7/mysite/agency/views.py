from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect

from .form import AgencyForm
from .models import Agency, Employer, Contract


def index(request):
    agency_list = Agency.objects.all()
    employee_list=Employer.objects.all()
    contract_list=Contract.objects.all()
    context = {
        "agency_list": agency_list,
        "employee_list": employee_list,
        "contract_list":contract_list,
    }
    return render(request, 'agency/index.html', context)

def agency_detail(request, agency_id):
    agency = get_object_or_404(Agency, id=agency_id)
    return render(request, "agency/agency_detail.html", {"agency": agency})

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employer, id=employee_id)
    return render(request, "agency/employee_detail.html", {"employee": employee})

def contract_detail(request, contract_id):
    contract = get_object_or_404(Contract, id=contract_id)
    return render(request, "agency/contract_detail.html", {"contract": contract})


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