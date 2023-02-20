from django.db import models

from django.urls import reverse

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=250, db_index=True)

    slug = models.SlugField(max_length=250, unique=True)


    #In django adminstration change name catogories because django always add F in model name by default.
    class Meta:

        verbose_name_plural = 'categories'
    #In django adminstration change name your add items because items name always like item (1) ...by defualt.
   
    def __str__(self):
        return self.name


    def get_absolute_url(self):

        return reverse('list-category',args=[self.slug])




class Product(models.Model):

    #FK
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null = True, default='')

    title = models.CharField(max_length=250)

    brand = models.CharField(max_length=250, default='un-branded')

    decription = models.TextField(blank=True)

    slug = models.SlugField(max_length=250)

    price = models.DecimalField(max_digits=4, decimal_places=2)

    image = models.ImageField(upload_to='images/', default='')
    class Meta:

        verbose_name_plural = 'products'
    
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        #reverse('路徑名稱',slug參數)
        return reverse('product-info',args=[self.slug])