from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255) # trường name có kiểu char và độ dài 255

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Categories' #cung cấp một số cấu hình bổ sung cho mô hình. Trong trường hợp này, chúng ta đặt verbose_name_plural là 'Categories' để chỉ định tên hiển thị của mô hình khi hiển thị nhiều đối tượng danh mục.

    def __str__(self):
        return self.name #Phương thức str() được sử dụng để định nghĩa cách đại diện chuỗi của đối tượng Category khi được in ra. Trong trường hợp này, nó trả về giá trị của trường name, tức là tên của danh mục.
     
class Items(models.Model):
    category = models.ForeignKey(Category, related_name='item', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)