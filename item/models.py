from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255) # trường name có kiểu char và độ dài 255

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Categories' #cung cấp một số cấu hình bổ sung cho mô hình. Trong trường hợp này, chúng ta đặt verbose_name_plural là 'Categories' để chỉ định tên hiển thị của mô hình khi hiển thị nhiều đối tượng danh mục.

    def __str__(self):
        return self.name #Phương thức str() được sử dụng để định nghĩa cách đại diện chuỗi của đối tượng Category khi được in ra. Trong trường hợp này, nó trả về giá trị của trường name, tức là tên của danh mục.
     
class Items (models.Model):
    category = models.ForeignKey(Category, related_name='item', on_delete=models.CASCADE) #tạo khóa ngoài với category, related_name là đặt tên cho khóa ngoài, on_delete là khi xóa category thì items cũng bị xóa theo
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    