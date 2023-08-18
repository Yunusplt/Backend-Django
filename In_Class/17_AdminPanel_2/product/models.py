from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):                        #! 0908  12:17 
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name
    

class Product(models.Model):
    categories = models.ManyToManyField(Category, related_name="products")
    image=models.ImageField(null=True, blank=True, default="clarusway.png", upload_to="product/")    #! 1008 static ve media ya resim ekledikten sonra buradayiz.
    name = models.CharField(max_length=100)
    # description = models.TextField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)                               #!0908
    is_in_stock = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    
    def __str__(self):
        return self.name
    
    #!1008 Method for image
    def view_image(self):
        from django.utils.safestring import mark_safe
        if self.image:
            return mark_safe(f'<img src={self.image.url} style="max-height:100px; max-width:200px;"></img>')
        else:
            return mark_safe(f'<h2>No Image</h2>')


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    is_released = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.product.name} - {self.review}"  