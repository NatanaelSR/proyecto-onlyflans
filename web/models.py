import uuid
from django.db import models

from django.db import models
from django.utils.text import slugify

class Flan(models.Model):
    TAG_CHOICES = [
        ('Gourmet', 'Gourmet'),
        ('Más Vendido', 'Más Vendido'),
        ('Sin Azúcar', 'Sin Azúcar'),
        ('Edición Especial', 'Edición Especial'),
        ('Novedad', 'Novedad'),
        ('Tradicional', 'Tradicional'),
    ]
       
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(blank=True)
    is_private = models.BooleanField(default=False)
    precio = models.IntegerField(default=0)
    
    tag = models.CharField(
        max_length=30,
        choices=TAG_CHOICES,
        default='Gourmet',
        verbose_name='Etiqueta / Tag'
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()