### to add image field in admin panel.
- STATICFILES_DIRS = [ BASE_DIR / STATIC_URL ]
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / MEDIA_URL  in settings.py
- from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    in urls.py
- then media ve static folders were created
- then python -m pip install Pillow.  
- makemigrations and migrate
- admin panelin yapisini degistirdigimiz icin admin.py de ekleme yapiyoruz. ('image',)
- ürün detaylara girince resim gözükmesi icin harici mir method yazmamiz lazim. model.py a yaziyoruz. digerleri admin.py a yzilmisti.
- kodun güvenli oldugunu göstermek icin methodu mark_safe sarmalina aliyoruz.

### TEMPLATES
- to create a Templates folder.
- varligindan Djangoyu haberdar etmek icin settings.py line 63 

### THIRD PARTS PACKAGES
- pip install django-admin-list-filter-dropdown    to installed apps    'django_admin_listfilter_dropdown',
- from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
- list_filter = [('name', DropdownFilter), 'is_in_stock', 'create_date', 'update_date']
- list_filter = [('product', RelatedDropdownFilter)]
- pip install django-admin-rangefilter 
- from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter 
- list_filter = [('name', DropdownFilter), 'is_in_stock', ('create_date', DateRangeFilter), ('update_date', DateTimeRangeFilter)]
- pip install django-import-export      in installed app    'import_export',
- from import_export import resources
- from import_export.admin import ImportExportModelAdmin
- Import-Export ModelResource:
class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
-class ProductAdmin(ModelAdmin):
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    # Tablo sutunları (model field names)
    list_display = ['id', 'name', 'is_in_stock', 'create_date', 'update_date']
- pip install django-grappelli   Bu en basta olmak zorunda installed app te de urls de de.   'grappelli', # En üstte olacak.
- path('grappelli/', include('grappelli.urls')), # En üstte olacak.

