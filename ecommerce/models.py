from django.db import models

# Create your models here.

class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=20)

class Products(models.Model):
    productId = models.AutoField(primary_key=True)
    productTitle = models.CharField(max_length=50)
    productDescription = models.TextField()
    productRatings = models.FloatField()
    productPrice = models.FloatField()
    productSales = models.IntegerField()
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comments(models.Model):
    commentId = models.AutoField(primary_key=True)
    commentText = models.TextField()
    productId = models.ForeignKey(Products, on_delete=models.CASCADE)

class Cart(models.Model):
    cartId = models.AutoField(primary_key=True)
    productId = models.ForeignKey(Products, on_delete=models.CASCADE)