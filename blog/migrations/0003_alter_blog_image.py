# Generated by Django 4.1.3 on 2022-11-29 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='topic3.png', null=True, upload_to='Blog_Image'),
        ),
    ]
