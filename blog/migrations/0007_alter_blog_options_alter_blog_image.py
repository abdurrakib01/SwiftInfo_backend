# Generated by Django 4.1.3 on 2022-12-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['time']},
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='assets/topic3.png', upload_to='Blog_Image'),
        ),
    ]
