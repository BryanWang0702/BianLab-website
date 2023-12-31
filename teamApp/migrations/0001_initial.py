# Generated by Django 3.2.16 on 2023-07-06 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=50, null=True)),
                ('photo', models.ImageField(blank=True, default='#', upload_to='team/')),
                ('position', models.TextField(blank=True, max_length=100, null=True)),
                ('background', models.TextField(blank=True, max_length=500, null=True)),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('email', models.TextField(blank=True, max_length=50, null=True)),
                ('detail', models.TextField(blank=True, max_length=5000, null=True)),
                ('researchInterest', models.TextField(blank=True, max_length=500, null=True)),
                ('interest', models.TextField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Team',
                'db_table': 'team',
            },
        ),
    ]
