# Generated by Django 3.2.16 on 2023-07-05 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal', models.TextField(blank=True, max_length=100, null=True)),
                ('year', models.TextField(blank=True, max_length=10, null=True)),
                ('title', models.TextField(blank=True, max_length=500, null=True)),
                ('author', models.TextField(blank=True, max_length=300, null=True)),
                ('link', models.TextField(blank=True, max_length=300, null=True)),
                ('photo', models.ImageField(blank=True, default='#', upload_to='publication/')),
            ],
            options={
                'verbose_name': 'Publication',
                'verbose_name_plural': 'Publication',
                'db_table': 'publication',
            },
        ),
    ]
