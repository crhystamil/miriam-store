from django.shortcuts import render, redirect, get_object_or_404
from .models import Brand, Product, Inventory, Sale, Seller
from django.db.models import Sum, F
from .forms import SellForm 

def home(request):
    return render(request, 'index.html', {'title':'Inicio'})

def service(request):
    return render(request, 'services.html', {'title':'Servicios'})

def contact(request):
    return render(request, 'contact.html', {'title':'Contactanos'})

def products(request):
    brands = Brand.objects.all()
    products = Inventory.objects.filter(state="1", quantity__gte=1)
    return render(request, 'products.html', {'title':'Productos', 'brands':brands, 'products':products})

def product_detail(request, product_id):
    product = Inventory.objects.get(product__id=product_id, state="1")
    brands = Brand.objects.all()
    return render(request, 'detail_product.html', {'title':'Detalles', 'product':product, 'brands':brands})

def brand_list(request, brand_id):
    list_p = Product.objects.filter(brand=brand_id)
    product = Inventory.objects.filter(product__id__in=list_p, state="1")
    brands = Brand.objects.all()
    return render(request, 'products.html', {'title':'Marcas','products':product, 'brands':brands})

def search(request):
    item = request.GET.get('item')
    products = Product.objects.filter(name__icontains=item)
    inventory = Inventory.objects.filter(product__id__in=products, state="1")
    brands = Brand.objects.all()
    return render(request, 'products.html', {'title':'Productos','brands':brands,'products':inventory})
    
   
def list_inventory_seller(request):
    name = request.GET.get('name')
    if name == 'a9d3ebb8f7a244085bd3de59a73a9093':
        inventory = Inventory.objects.all()
        return render(request, 'list_inventory_seller.html', {'title':'Lista de Inventario', 'inventory':inventory})
    else:
        return redirect('home')

def list_inventory(request):
    if request.user.is_staff:
        inventory = Inventory.objects.filter(state='1').order_by('quantity')
        return render(request, 'list_inventory.html', {'title':'Lista de Inventario', 'inventory':inventory})
    else:
        return redirect('home')


def sell(request):
    if request.user.is_staff:
        seller = Seller.objects.all()
        sales = Sale.objects.filter(seller__id__in=seller, status='2')
        return render(request, 'sell.html',{'title':'Ventas', 'sales':sales, 'sellers':seller})
    else:
        return redirect('home')

def sellu(request):
    if request.user.is_staff:
        seller = Seller.objects.all()
        sales = Sale.objects.filter(seller__id= request.GET.get('id'), status='2')
        profit = sales.aggregate(Sum('profit_seller'))['profit_seller__sum'] or 0
        return render(request, 'sell.html',{'title':'Ventas', 'sales':sales, 'sellers':seller, 'profit':profit, 'id_seller' :request.GET.get('id')})
    else:
        return redirect('home')

def new_sell(request):
    if request.method == 'POST':
        if request.user.is_staff and request.user.username == request.POST['registredby']:
            form = SellForm(request.POST)
            if form.is_valid():
                q = Inventory.objects.get(pk=request.POST['product_inv']).quantity - int(request.POST['quantity_sold'])
                Inventory.objects.filter(pk=request.POST['product_inv']).update(quantity=q)
                form.save()
                return redirect('sell')
            else:
                return redirect('sell')
        else:
            return redirect('home')
    else:
        if request.user.is_staff:
            products = Inventory.objects.filter(state='1', quantity__gte=1)
            seller = Seller.objects.all()
            return render(request, 'new_sell.html', {'products': products, 'sellers':seller})
        return redirect('home')


def calculate_profit_seller(request):
    if request.method == 'POST' and request.user.username == 'crhyst':
        seller_id = request.POST['seller_id']
        sales = Sale.objects.filter(seller__id=seller_id, status = '2')
        for sale in sales:
            sell_id = sale.id
            price_inv = sale.product_inv.price_seller
            sale_quantity = sale.quantity_sold
            sale_price_sell = sale.selling_price
            profit = (sale_quantity * sale_price_sell) - (price_inv * sale_quantity) 
            Sale.objects.filter(pk=sell_id).update(profit_seller=profit)
        return redirect("/sellu/?id="+request.POST['seller_id'])
    else:
        return redirect('home')

