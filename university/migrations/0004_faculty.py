# Generated by Django 5.0.2 on 2024-11-20 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title_uz', models.CharField(max_length=255)),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='faculty/image/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
