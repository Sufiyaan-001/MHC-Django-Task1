from django.shortcuts import render,get_object_or_404, redirect
from .models import groces
# Create your views here.
def groceries_list(request):
    query = request.GET.get('q', '')
    groc = groces.objects.filter(Name__icontains=query)
    return render(request,'groc_list.html',{'groces':groc})
def groceries_add(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Type = request.POST.get('Type')
        Quality = request.POST.get('Quality')
        Quantity = request.POST.get('Quantity')
        Vendor = request.POST.get('Vendor')
        Price = request.POST.get('Price')
        groces.objects.create(
        Name=Name,
        Type=Type,
        Quality=Quality,
        Quantity=Quantity,
        Vendor=Vendor,
        Price=Price
        )
        return redirect('grocs-data')
    return render(request, 'groc_form.html')
def groceries_edit(request, pk):
    groc = get_object_or_404(groces, pk=pk)
    if request.method == 'POST':
        groc.Name = request.POST.get('Name')
        groc.Type = request.POST.get('Type')
        groc.Quality = request.POST.get('Quality')
        groc.Quantity = request.POST.get('Quantity')
        groc.Price = request.POST.get('Price')
        groc.Vendor = request.POST.get('Vendor')
        groc.save()
        return redirect('grocs-data')
    return render(request, 'groc_form.html', {'groces': groc})
def groceries_delete(request, pk):
    groc = get_object_or_404(groces, pk=pk)
    if request.method == 'POST':
        groc.delete()
        return redirect('grocs-data')
    return render(request, 'groc_delete.html', {'groces': groc})