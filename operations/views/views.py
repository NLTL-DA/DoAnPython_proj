from django.shortcuts import render

def operations_page(request):
    return render(request, "operations/operations_page.html")

def table_page(request):
    return render(request, "operations/table_page.html")