# Generated by Django 3.2.16 on 2023-07-07 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryExperiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='#', upload_to='gallery/experiment/')),
                ('text', models.TextField(max_length=500, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Experiment gallery',
                'verbose_name_plural': 'Experiment gallery',
                'db_table': 'galleryExperiment',
            },
        ),
        migrations.CreateModel(
            name='GalleryLife',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='#', upload_to='gallery/life/')),
                ('text', models.TextField(max_length=500, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Life gallery',
                'verbose_name_plural': 'Life gallery',
                'db_table': 'galleryLife',
            },
        ),
    ]
