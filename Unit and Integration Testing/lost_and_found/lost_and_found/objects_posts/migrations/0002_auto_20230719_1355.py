# Generated by Django 3.2.3 on 2023-07-19 10:55

from django.db import migrations, models
import lost_and_found.objects_posts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('objects_posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author_phone',
            field=models.CharField(max_length=10, validators=[lost_and_found.objects_posts.validators.validate_phone]),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
