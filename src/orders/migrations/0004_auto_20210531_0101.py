# Generated by Django 2.2.2 on 2021-05-31 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabric',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fabrics', to='orders.Order'),
        ),
    ]