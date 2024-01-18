from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('brand/<int:brand_id>/', views.brand_list, name='brand_list'),
    path('search/', views.search, name='search'),
    path('sell/', views.sell, name='sell'),
    path('sellu/', views.sellu, name='sellu'),
    path('newSell/', views.new_sell, name='new_sell'),
    path('listinvsell/', views.list_inventory_seller, name='list_inv_sell'),
    path('listinv', views.list_inventory, name='list_inv'),
    path('genprof', views.calculate_profit_seller, name='genprof'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
