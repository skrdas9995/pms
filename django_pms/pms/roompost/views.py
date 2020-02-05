from django.shortcuts import render, HttpResponse
from .forms import DoctorDetailsForm
# Create your views here.


def index(request):
    return render(request, 'index-2.html')


def doctorDetails(request):
    if request.POST:
        print(request.POST)
        form = DoctorDetailsForm(request.POST)
        if form.is_valid():
            print("sdfsadfsafsdfssssssssssssssssssssssssssssssssssssssssssssssssss")
            form.save(commit=False)
        return HttpResponse("success")
    else:
        return render(request,  'Doctor_add.html')