from django.db import models
from django.utils import timezone

class Brand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.ManyToManyField(Brand)
    tag = models.TextField()
    def __str__(self):
        return f"{self.id} - {self.name}"

class ImageProduct(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='media/')
    def __str__(self):
        return f"Imagen de {self.product.name}"

class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    cost = models.DecimalField(max_digits=10, decimal_places=1)
    price_seller = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    state = models.TextField(max_length=100, choices=[("1","Disponible"),("2","No Disponible")],default='1')
    created = models.DateField(default=timezone.now, editable=False)
    def __str__(self):
        return f"{self.id} - {self.product} - quantity: {self.quantity}, price: {self.price}"

class Seller(models.Model):
    name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, null=True)
    passwd = models.CharField(max_length=100, null=True)
    def __str__(self):
        return f"{self.id} - {self.username}"

class Sale(models.Model):
    product_inv = models.ForeignKey(Inventory, related_name='ventas', on_delete=models.CASCADE)
    seller =  models.ForeignKey(Seller, related_name='ventas', on_delete=models.CASCADE, null=True)
    created = models.DateField(default=timezone.now, editable=False)
    quantity_sold = models.PositiveIntegerField()
    profit_seller = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    profit = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    status = models.TextField(max_length=100, choices=[("1","pagado"),("2","no pagado")], default="2")
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    registredby = models.CharField(max_length=100, default="nobody")
    def __str__(self):
        return f"Venta de {self.seller.name} {self.product_inv.product.name} - {self.created}"


