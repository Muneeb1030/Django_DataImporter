from django.shortcuts import render

def importdata(request):
    return render(request, 'importer/importdata.html')