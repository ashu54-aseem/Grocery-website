# Generated by Django 2.2.9 on 2020-01-31 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_product_detail_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_detail',
            name='quantity',
            field=models.CharField(max_length=20, null=True),
        ),
    ]