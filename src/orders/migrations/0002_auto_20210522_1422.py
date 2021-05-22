# Generated by Django 2.2.2 on 2021-05-22 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'Payment', 'verbose_name_plural': 'Payments'},
        ),
        migrations.AlterField(
            model_name='order',
            name='expiration_date',
            field=models.DateField(default=None, verbose_name='expiration date'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateField(default=None, verbose_name='date'),
        ),
    ]