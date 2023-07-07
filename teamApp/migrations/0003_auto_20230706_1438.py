# Generated by Django 3.2.16 on 2023-07-06 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamApp', '0002_team_positiontype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='background',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='bio',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='detail',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='email',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='interest',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(default='#', upload_to='team/'),
        ),
        migrations.AlterField(
            model_name='team',
            name='position',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='positionType',
            field=models.TextField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='researchInterest',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
