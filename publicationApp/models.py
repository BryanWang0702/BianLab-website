from django.db import models


# Create your models here.

class Publication(models.Model):
    # 期刊
    journal = models.TextField(max_length=100, blank=False, null=True)
    # 年份
    year = models.TextField(max_length=10, blank=False, null=True)
    # 论文题目
    title = models.TextField(max_length=500, blank=False, null=True)
    # 作者
    author = models.TextField(max_length=300, blank=False, null=True)
    # 文章链接
    link = models.TextField(max_length=300, blank=False, null=True)
    # 缩略图路径
    photo = models.ImageField(upload_to="publication/", blank=False, default='#')

    class Meta:
        verbose_name = verbose_name_plural = 'Publication'  # 在管理后台看到的表名
        db_table = 'publication'  # 在数据库中看到的表名
