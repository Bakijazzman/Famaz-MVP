# Generated by Django 4.2.11 on 2024-05-09 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_item_quantity_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='this is a test-description for the page'),
            preserve_default=False,
        ),
    ]
