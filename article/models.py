from django.db import models

# Create your models here.
class article(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='Yazar')
    title = models.CharField(max_length=50,verbose_name='Baslik')
    content = models.TextField(verbose_name='Icerik')
    createdDate = models.DateTimeField(auto_now_add=True,verbose_name='OlusturulmaTarihi')
    def __str__(self):
        return self.title
