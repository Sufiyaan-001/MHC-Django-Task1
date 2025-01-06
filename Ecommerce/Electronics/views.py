from django.shortcuts import render,get_object_or_404, redirect
from .models import elecs
# Create your views here.
def elecs_list(request):
    query = request.GET.get('q', '')
    ele = elecs.objects.filter(Name__icontains=query)
    return render(request,'elec_list.html',{'elec':ele})
def elecs_add(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Type = request.POST.get('Type')
        Description=request.POST.get('Description')
        Rating = request.POST.get('Rating')
        Price = request.POST.get('Price')
        elecs.objects.create(
        Name=Name,
        Type=Type,
        Description=Description,
        Rating=Rating,
        Price=Price
        )
        return redirect('ele-data')
    return render(request, 'elec_form.html')
def elecs_edit(request, pk):
    ele = get_object_or_404(elecs, pk=pk)
    if request.method == 'POST':
        ele.Name = request.POST.get('Name')
        ele.Type = request.POST.get('Type')
        ele.Description = request.POST.get('Description')
        ele.Price = request.POST.get('Price')
        ele.Rating = request.POST.get('Rating')
        ele.save()
        return redirect('ele-data')
    return render(request, 'elec_form.html', {'elec': ele})
def elecs_delete(request, pk):
    ele = get_object_or_404(elecs, pk=pk)
    if request.method == 'POST':
        ele.delete()
        return redirect('ele-data')
    return render(request, 'elec_delete.html', {'elec': ele})