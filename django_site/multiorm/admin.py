from django.contrib import admin

# Register your models here.
from django.core.paginator import Paginator

from multiorm import models

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','pub_date','publish','priceSuf')
    # list_display_links = ('name','price','pub_date','publish')
    list_editable = ('name','price','pub_date','publish')
    filter_horizontal = ('authors',)
    search_fields = ('id','name','price','publish__name',)
    # 分页，每页显示条数
    list_per_page = 3
    # 分页，显示全部（真实数据<该值时，才会有显示全部）
    list_max_show_all = 20
    # 分页插件
    paginator = Paginator

    list_filter = ('pub_date','publish')

    def priceSuf(self,obj):
        return str(obj.price)+"元"


admin.site.register(models.Book,BookAdmin)

@admin.register(models.Author)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','age')
    # list_display_links = ('name','age')
    list_editable = ('age',)
    list_display_links = ('name',)

admin.site.register(models.Publish)
