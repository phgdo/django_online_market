from django.contrib import admin
from .models import Category, Items
# Register your models here.
# đăng ký models vào trang admin để quản lý
admin.site.register(Category)
admin.site.register(Items)