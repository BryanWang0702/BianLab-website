from django.db import models

# Create your models here.


class Research(models.Model):
    # 研究方向标题
    title = models.TextField(max_length=200, blank=False, null=True)
    # 研究方向具体介绍
    detail = models.TextField(max_length=5000, blank=False, null=True)

    class Meta:
        verbose_name = verbose_name_plural = 'Research'  # 在管理后台看到的表名
        db_table = 'research'  # 在数据库中看到的表名
