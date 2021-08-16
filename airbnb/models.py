from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
from django.urls.base import clear_url_caches
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel,TreeForeignKey
# Create your models here.

class Ciudades(MPTTModel):
    name=models.CharField(verbose_name=('Ciudades'),max_length=255,unique=True)
    slug=models.SlugField(verbose_name="url",max_length=255,unique=True)
    parent=TreeForeignKey('self',on_delete=models.CASCADE,null=True,blank=True, related_name="children")
    is_active=models.BooleanField(default=True)
    class MPTTMeta:
        order_insert_by=['name']
    class Meta:
        verbose_name='Ciudades'
    def get_absolute_url(self):
        return reverse("airbnb:ciudades_list", args=[self.slug])
    def __str__(self):
        return self.name


class Cities(models.Model):
    title=models.CharField(max_length=255,verbose_name="title")
    slug=models.SlugField(max_length=255,unique=True)
    ciudades=models.ForeignKey(Ciudades,on_delete=models.RESTRICT)
    price=models.FloatField(max_length=255)
    detalles=models.CharField(max_length=255,verbose_name=('detalles'))
    description=models.TextField(verbose_name=("Descripcion"))
    created_at=models.DateTimeField(auto_now_add=True,editable=False)
    
    class Meta:
        ordering=("-created_at",)
        verbose_name=_("City")
        verbose_name_plural=_("Cities")

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self):
        return self.title


class ProductImage (models.Model):
    product=models.ForeignKey(Cities,on_delete=models.CASCADE,related_name='image')
    image=models.ImageField(upload_to='images/',help_text=_("Upload a product image"),default="images/default.png",)
    is_feature = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True,editable=False)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name=_("Product Image")
        verbose_name_plural=_("Products Image")

    

    