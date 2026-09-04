from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


from .models import Product, Cart

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        product=product,
        defaults={'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


def cart(request):
    cart_items = Cart.objects.all()

    total = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'products/cart.html', {
        'cart_items': cart_items,
        'total': total
    })


def delete_cart(request, pk):
    item = get_object_or_404(Cart, id=pk)
    item.delete()
    return redirect('cart')
