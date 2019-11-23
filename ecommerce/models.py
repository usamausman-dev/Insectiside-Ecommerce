from django.db import models
from PIL import Image

# Create your models here.

class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=20)

    def __str__(self):
        return self.categoryName

class Products(models.Model):
    productId = models.AutoField(primary_key=True)
    productImg = models.ImageField(upload_to='Products', default='default.png')
    productTitle = models.CharField(max_length=50)
    productDescription = models.TextField()
    productRatings = models.FloatField()
    productSales = models.IntegerField()
    marketPrice = models.FloatField()
    discountedPrice = models.FloatField()
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.productTitle

    def save(self):
        super().save()

        img = Image.open(self.productImg.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.productImg.path)

# class Comments(models.Model):
#     commentId = models.AutoField(primary_key=True)
#     commentText = models.TextField()
#     productId = models.ForeignKey(Products, on_delete=models.CASCADE)

# class Cart(models.Model):
#     cartId = models.AutoField(primary_key=True)
#     productId = models.ForeignKey(Products, on_delete=models.CASCADE)