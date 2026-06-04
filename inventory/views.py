from urllib import request

from .forms import *
from .models import *

from django.shortcuts import render,redirect

# Create your views here.


def product_page(request):
    form = product_forms(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/inventory/product/view/')

    context = {
        'product_form': form
    }

    return render(request, 'product_form.html', context)

def  product_view(request):

    context={
        'all_product':product.objects.all()

    }
    return render(request,'product.html',context)
def delete_product(request,id):
    selected_products=product.objects.get(id = id)
    selected_products.delete()
    return redirect('/inventory/product/view/')
def update_product(request,id):
    selected_products=product.objects.get(id = id)
    
    context={
        'product_form':product_forms(instance=selected_products)
    }
   
    if request.method == 'POST':
            form = product_forms(request.POST, instance=selected_products)
            if form.is_valid():
                form.save()
                return redirect('/inventory/product/view/')
    return render(request,'product_form.html',context)

    
    