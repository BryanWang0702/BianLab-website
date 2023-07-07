from django.db import models

# Create your models here.


class News(models.Model):
    # 新闻图片
    photo = models.ImageField(upload_to='news/', blank=False, default='#')
    # 新闻标题
    title = models.TextField(max_length=200, blank=False, null=True)
    # 新闻正文
    text = models.TextField(max_length=5000, blank=False, null=True)
    # 时间
    time = models.TextField(max_length=50, blank=False, null=True)

    class Meta:
        verbose_name = verbose_name_plural = 'News'  # 在管理后台看到的表名
        db_table = 'news'  # 在数据库中看到的表名
