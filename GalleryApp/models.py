from django.db import models


# Create your models here.


class GalleryLife(models.Model):
    # 展示图片
    photo = models.ImageField(upload_to='gallery/life/', blank=False, default='#')
    # 图片简短介绍
    text = models.TextField(max_length=500, blank=False, null=True)
    # 上传时间
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = 'Life gallery'  # 在管理后台看到的表名
        db_table = 'galleryLife'  # 在数据库中看到的表名


class GalleryExperiment(models.Model):
    # 展示图片
    photo = models.ImageField(upload_to='gallery/experiment/', blank=False, default='#')
    # 图片简短介绍
    text = models.TextField(max_length=500, blank=False, null=True)
    # 上传时间
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = 'Experiment gallery'  # 在管理后台看到的表名
        db_table = 'galleryExperiment'  # 在数据库中看到的表名
