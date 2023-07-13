from django.db import models


# Create your models here.


class Team(models.Model):
    # 名字
    name = models.TextField(max_length=500, blank=False, null=True)
    # 照片
    photo = models.ImageField(upload_to="team/", blank=False, default='#')
    # 职位
    position = models.TextField(max_length=1000, blank=False, null=True)
    # 职位类型，用于代表PI，RA，Postdoc, phd
    positionType = models.TextField(
        help_text="0-visiting student, 1-research assistant, 2-lab manager, 3-Ph.D, 4-postDoc, 5-..., 10-PI",
        max_length=10, blank=False, null=True)
    # 教育或其他背景
    background = models.TextField(max_length=5000, blank=False, null=True)
    # 一句话
    bio = models.TextField(max_length=5000, blank=False, null=True)
    # 邮箱
    email = models.TextField(max_length=500, blank=False, null=True)
    # 详细介绍（跳转到具体页面需要展示）
    detail = models.TextField(max_length=500000, blank=False, null=True)
    # 研究方向
    researchInterest = models.TextField(max_length=500000, blank=False, null=True)
    # 兴趣爱好
    interest = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = verbose_name_plural = 'Team'  # 在管理后台看到的表名
        db_table = 'team'  # 在数据库中看到的表名
