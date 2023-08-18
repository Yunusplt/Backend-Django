from django.contrib import admin   #! 0908 tabulerinline admin icinde geliyor. 
from .models import *
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter  #!1008 third party app
from django.contrib.admin.options import ModelAdmin             #!0908 ModelAdmin inherit etmek icin import ettik. 
#!1008 image list_display e eklendi. daha sonra gerek kalmadi silindi. 
#!1008 fieldsset de de slug in üstüne image ekledim. 
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from import_export import resources
from import_export.admin import ImportExportModelAdmin


#!1008 baslik degisme 
admin.site.site_title = 'Clarusway Title'          #!title   favicon yani
admin.site.site_header = 'Clarusway Header'         #!page title    header
admin.site.index_title = 'Clarusway Index Page'     #! index subtitle  admin homepage de gözükür...
#-------------------------------------------------

#-----------------------------------------------------------------------
# Category
#-----------------------------------------------------------------------
admin.site.register(Category)                  #!ManytoMany 
#todo adminde görmüyoruz productlar araasinda neden cünkü defaulti degistirdik . benim istedigim fieldlari gösteriyor. bunuda eklemem lazim 
#-----------------------------------------------------------------------
# Product
#-----------------------------------------------------------------------
class ReviewInline(admin.TabularInline):  #!en son burayi olusturuyoruz. 
    model = Review   #!ForeignKey model Name 
    extra = 1        #! bos gelen yorum alani sayisi
    classes = ['collapse']

#!1008
# Import-Export ModelResource:
class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
#!--------------------------------------------

# class ProductAdmin(ModelAdmin):                                  #! bir class icinde baska bir classi cagirdik. ModelAdmin i inherit ettik.     
# class ProductAdmin(ModelAdmin):
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    #list_display = ('name','description','is_in_stock')         #! inherit ettigim classdaki bir methodu tekrardan tanimlamaya override denir. iste burasi. 
    list_display = ['id', 'name', 'is_in_stock', 'create_date', 'update_date']   #! list de kullanabilirim, tuple da olabilir. bunlar modeldeki fieldnameler
    list_editable = ['is_in_stock']                          #! direk tablo üzerinde degisiklik yapmamiza izin veririr.admin panelde.
    list_display_links = ['id','name']                           #! tiklayinca detaylara gitmek icin link verir. linkte bulunan editable da bulunamaz. name yukardaki listede olamaz yani
    #list_filter = ['is_in_stock', 'create_date', 'update_date']  #! admin panelde sag tarafta filtre blogu cikiyor. 
    #!1008
    list_filter = [('name', DropdownFilter), 'is_in_stock', ('create_date', DateRangeFilter), ('update_date', DateTimeRangeFilter)]
    search_fields = ['id','name']                                #! isme ve id ye göre search yapma olanagi verir. 
    search_help_text = ['Arama yapmak icin burayi kullaniniz']   #! adminde search kutusu altina bilgilendirme yazisi atar.
    # ordering = ['-id']                                              #!default siralama.  descending order
    ordering = ['id']                                              #!default siralama.  ascending order.
    list_per_page = 20                                           #! sayfa basina düsen veri.
    list_max_show_all = 200
    date_hierarchy = 'create_date'                               #! tarihe göre filtreleme, Tarihfield olmak zorunda
   # Resim gösterme read_only olarak çağır: #!1008
    readonly_fields = ["view_image"]
    # Otomatik kaıyıt oluştur:
    prepopulated_fields = {'slug' : ['name']}
    # fields = (                                                   #! form detay görüntüleme layout
    #     ('name', 'is_in_stock'),
    #     ('slug'),
    #     ('description'),
    # )
#! fieldsets ve fields ikisi ayni anda kullanilmaz... üsttekini yoruma aliyoruz simid
    fieldsets=(                                                  #!Layout yapar. bölümleri basliklara göre ayirir. detayli.
        (
            'General Settings', {
                'fields':(
                     ('name', 'is_in_stock'),
                     ('image','view_image'),    #!1008
                     ('slug',),
                     ('categories'),
                )
            }
        ),
        (
           'Optional Settings', {
                'classes':['collapse'],                #! Optional Settings alani kapali olarak gelsin. ['wide'] default degeri.
                'fields':(
                     ('description'),
                ),
                'description':'You can use this section for optional settings'   #! aciklama ekler. 
            }
        )
    )
    # filter_vertical = ['categories']
    filter_horizontal = ['categories']
    inlines=[ReviewInline]


#!action kismi icin model yaziyoruz.
#!2 tane method yaziyoruz.
    def set_stock_in(self,request,queryset):        #! function ismi osman da olabilir
        count=queryset.update(is_in_stock=True)      #!mesela 5 tane update ettim diyecek onu count a atiyoruz.
        self.message_user(request, f'{count} adet "Stokta Var" olarak işaretlendi.')

    def set_stock_out(self,request,queryset):       #! function ismi osman da olabilir
        count=queryset.update(is_in_stock=False)      #!mesela 5 tane update ettim diyecek onu count a atiyoruz.
        self.message_user(request, f'{count} adet "Stokta Var" olarak işaretlendi.')

    actions = ('set_stock_in', 'set_stock_out')

    set_stock_in.short_description = 'İşaretli ürünleri stoğa ekle'
    set_stock_out.short_description = 'İşaretli ürünleri stoktan çikar'
    #! modelde olmayan veriyi method olusturarak yeni bir sütun olusturuyoruz. ve list_display e ekliyoruz. 
    def added_days_ago(self, object):
        from django.utils import timezone
        different = timezone.now() - object.create_date
        return different.days
    
    # list_display = ['id', 'name', 'is_in_stock', 'create_date', 'update_date','added_days_ago']
    added_days_ago.short_description = 'Days'        #!1008 isimleri kisalttik 
    list_display += ['added_days_ago']

        # Kaçtane yorum var:
    def how_many_reviews(self, object):
        count = object.reviews.count()
        return count
    how_many_reviews.short_description = 'Reviews'   #!1008 
    list_display += ['how_many_reviews']

    
    # Listede küçük resim göster:  #!1008
    def view_image_in_list(self, obj):               #! bu basligi uzun uzun ekleme 108 satira bak. 
        from django.utils.safestring import mark_safe
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} style="height:30px; width:30px;"></img>')
        return '-*-'

    view_image_in_list.short_description = 'Image'          #! baslik olarak bu yazsin, list_displaydeki image e gerek kalamdi sil. cünkü resim fieldsi ekledik burda yaziya gerek yok. 2 fileds olacakti resim icin 
    list_display = ['view_image_in_list'] + list_display    #!en basa eklemek istedigimiz icin += yaptik....
    #-----------------------------------------------------------


admin.site.register(Product, ProductAdmin)                      #! product admin yazdigimiz yerde default olarak ModelAdmin vardi. 
    



#----------------------------------------------------------------------
# Review
#----------------------------------------------------------------------

class ReviewAdmin(ModelAdmin):
    list_display = ("__str__",'created_date')
    raw_id_fields = ('product',)







# admin.site.register(Review) #!Foreignkey 
admin.site.register(Review,ReviewAdmin) #!Foreignkey 

#!üst tablodan alt tabloya ait verileri cekmek istiyorum TabularInline kullaniyorum. PrimaryKey ForeignKey iliskisi. 