from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/')
def customer_list(request):
    context={
        'customers': customer.objects.all()
    }
    return render(request,'customer.html',context)

@login_required(login_url='/')
def customer_add(request):
    form = product_forms(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/orders/all/customers/')
    return render(request, 'customer_add.html', {'customer_form': form})

@login_required(login_url='/')
def customer_delete(request,id):
    selected_customer=customer.objects.get(id = id)
    selected_customer.delete()
    return redirect('/orders/all/customers/')

@login_required(login_url='/')
def customer_update(request,id):
    selected_customer=customer.objects.get(id = id)
    form = product_forms(request.POST or None, instance=selected_customer)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/orders/all/customers/')
    return render(request, 'customer_add.html', {'customer_form': form})

@login_required(login_url='/')
def orders_add(request):

    context={
        'order_form':order_form()}
    
    if request.method=='POST':
        selected_data=product.objects.get(id=request.POST['product_ref'])
        amount=float(selected_data.price) * float(request.POST['quantity'])
        gst_amount=amount * selected_data.tax/100
        bill_amount=amount + gst_amount
        new_order=orders(customer_ref_id=request.POST['customer_ref'],product_ref_id=request.POST['product_ref'],order_num=request.POST['order_num'],order_date=request.POST['order_date'],quantity=request.POST['quantity'],amount=amount,gst_amount=gst_amount,bill_amount=bill_amount)
        new_order.save()
        return redirect('/orders/view_orders/')
        

    return render(request,'orders_form.html',context)

@login_required(login_url='/')
def all_orders(request):
    context={
        'all_orders':orders.objects.all()
    }

    return render(request,'orders.html',context)

@login_required(login_url='/')
def delete_orders(request,id):
    order=orders.objects.get(id=id)
    order.delete()
    return redirect('/orders/view_orders/')

@login_required(login_url='/')
def update_orders(request,id):
    order=orders.objects.get(id=id)
    context={
        'order_form':order_form(instance=order)
    }

    if request.method=='POST':
        selected_data=product.objects.get(id=request.POST['product_ref'])
        amount=float(selected_data.price) * float(request.POST['quantity'])
        gst_amount=amount * selected_data.tax/100
        bill_amount=amount + gst_amount
        order_filter=orders.objects.filter(id=id)
        order_filter.update(customer_ref_id=request.POST['customer_ref'],product_ref_id=request.POST['product_ref'],order_num=request.POST['order_num'],order_date=request.POST['order_date'],quantity=request.POST['quantity'],amount=amount,gst_amount=gst_amount,bill_amount=bill_amount)
        return redirect('/orders/view_orders/')        
    
    return render(request,'orders_form.html',context)