# Generated by Django 5.0.2 on 2024-11-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0002_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title_uz', models.CharField(blank=True, max_length=255, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('description_uz', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('link1', models.CharField(blank=True, max_length=255, null=True)),
                ('link2', models.CharField(blank=True, max_length=255, null=True)),
                ('pages', models.CharField(max_length=255)),
                ('files', models.ManyToManyField(blank=True, null=True, to='common.file')),
                ('images', models.ManyToManyField(blank=True, null=True, to='common.image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]