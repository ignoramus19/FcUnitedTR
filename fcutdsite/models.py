from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class News(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Author")
    title = models.CharField(max_length = 50,verbose_name = "Title")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Created Date")
    news_image = models.FileField(blank = True,null = True,verbose_name="Adding Picture")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']






