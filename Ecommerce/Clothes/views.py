from django.shortcuts import render,get_object_or_404, redirect
from .models import cloths
# Create your views here.
def clothes_list(request):
    query = request.GET.get('q', '')
    cloth = cloths.objects.filter(Name__icontains=query)
    return render(request,'cloths_list.html',{'cloths':cloth})
def clothes_add(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Type = request.POST.get('Type')
        Shipping_agent=request.POST.get('Shipping_agent')
        Size = request.POST.get('Size')
        Price = request.POST.get('Price')
        cloths.objects.create(
        Name=Name,
        Type=Type,
        Shipping_agent=Shipping_agent,
        Size=Size,
        Price=Price
        )
        return redirect('cloth-data')
    return render(request, 'cloths_form.html')
def clothes_edit(request, pk):
    cloth = get_object_or_404(cloths, pk=pk)
    if request.method == 'POST':
        cloth.Name = request.POST.get('Name')
        cloth.Type = request.POST.get('Type')
        cloth.Shipping_agent = request.POST.get('Shipping_agent')
        cloth.Price = request.POST.get('Price')
        cloth.Size = request.POST.get('Size')
        cloth.save()
        return redirect('cloth-data')
    return render(request, 'cloths_form.html', {'cloths': cloth})
def clothes_delete(request, pk):
    cloth = get_object_or_404(cloths, pk=pk)
    if request.method == 'POST':
        cloth.delete()
        return redirect('cloth-data')
    return render(request, 'cloths_delete.html', {'cloths': cloth})