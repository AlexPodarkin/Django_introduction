# Generated by Django 4.2.5 on 2023-10-03 15:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp5', '0002_category_productadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='productadmin',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productadmin',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='productadmin',
            name='price',
            field=models.DecimalField(decimal_places=2, default=999.99, max_digits=8),
        ),
        migrations.AddField(
            model_name='productadmin',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productadmin',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=5.0, max_digits=3),
        ),
    ]