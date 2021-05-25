# Generated by Django 2.2.2 on 2021-05-24 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20210524_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_last_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_tel',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='order',
            name='expiration_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Fecha de expiración'),
        ),
    ]