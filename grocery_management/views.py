from django.shortcuts import redirect, render
from django.contrib import messages

from grocery_management.models import Product

# Create your views here.

def product_create(request):
    if request.method == 'POST':
        name            = request.POST.get('name')
        price_purchase  = float(request.POST.get('purchase_price'))
        price_selling   = float(request.POST.get('selling_price'))
        quantity        = int(request.POST.get('quantity'))

        item_product = Product(
          name            = name, 
          price_purchase  = price_purchase,
          price_selling   = price_selling,
          quantity        = quantity,
        )

        item_product.save()

        messages.success(request, 'Product added successfully')

        return redirect('/')

    return render(request, 'product_create.html' ,{})

def product_list(request):
    items_product = Product.objects.all()

    total_revenue = sum(product.price_selling * product.quantity_sold for product in items_product)

    total_profit = sum((product.price_selling - product.price_purchase) * product.quantity_sold for product in items_product)

    return render(request, 'product_list.html' ,{
        'items_product': items_product,
        'total_revenue': total_revenue,
        'total_profit': total_profit
    })

def product_update(request, product_id):
    item_product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        item_product.name            = request.POST.get('name')
        item_product.price_purchase  = float(request.POST.get('purchase_price'))
        item_product.price_selling   = float(request.POST.get('selling_price'))
        item_product.quantity        = int(request.POST.get('quantity'))
        item_product.quantity_sold   = int(request.POST.get('sold_quantity'))
        item_product.save()

        messages.success(request, 'Product updated successfully')

        return redirect('/')

    return render(request, 'product_update.html' ,{'item_product': item_product})

def product_delete(request, product_id):
    item_product = Product.objects.get(id=product_id)
    item_product.delete()

    messages.success(request, 'Product deleted successfully')
    return redirect('/')

def product_sell(request, product_id):
    item_product = Product.objects.get(id=product_id)

    quantity = int(request.GET.get('quantity'))

    item_product.quantity -= quantity
    item_product.quantity_sold += quantity
    item_product.save()

    messages.success(request, 'Product sold successfully')
    return redirect('/')
