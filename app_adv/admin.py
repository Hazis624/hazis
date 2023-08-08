from django.contrib import admin
from .models import Advertisements
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','price','auction','created_date']
    list_filter = ['auction','created_at']
    actions = ['make_auction_as_false','make_auction_as_true']
    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self,request,queryset):
        queryset.update(austion = False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(austion=True)
    fieldsets = (('Общее',{'fields':('title','description'),}),
                 ('Финансы',{'fields':('price','auction'),
                             'classes':('collapse')})
    )
admin.site.register(Advertisements,AdvertisementAdmin)
# Register your models here.
