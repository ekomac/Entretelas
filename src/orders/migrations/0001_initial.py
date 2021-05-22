# Generated by Django 2.2.2 on 2021-05-21 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('costs', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price_per_size', models.DecimalField(decimal_places=2, max_digits=50)),
                ('size', models.DecimalField(decimal_places=2, max_digits=50)),
            ],
            options={
                'verbose_name': 'Fabric',
                'verbose_name_plural': 'Fabrics',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('last_edited', models.DateTimeField(auto_now=True, verbose_name='last edition')),
                ('expiration_date', models.DateTimeField(default=None, verbose_name='expiration date')),
                ('state', models.CharField(choices=[('ER', 'Esperando respuesta'), ('AC', 'Aceptado'), ('MK', 'En confección'), ('FI', 'Terminado')], default='ER', max_length=1)),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='customers.Customer')),
                ('fabrics', models.ManyToManyField(to='orders.Fabric')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=50)),
                ('date', models.DateTimeField(default=None, verbose_name='date')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='orders.Order', verbose_name='order')),
            ],
            options={
                'verbose_name': 'Fabric',
                'verbose_name_plural': 'Fabrics',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('component_1_multiply_by', models.CharField(choices=[('AL', 'Alto'), ('AN', 'Ancho'), ('PE', 'Perímetro'), ('NA', 'Nada')], max_length=2)),
                ('component_1_factor', models.DecimalField(decimal_places=2, default='NA', max_digits=50)),
                ('component_1_tolerance', models.DecimalField(decimal_places=2, default='NA', max_digits=50)),
                ('component_2_multiply_by', models.CharField(choices=[('AL', 'Alto'), ('AN', 'Ancho'), ('PE', 'Perímetro'), ('NA', 'Nada')], max_length=2)),
                ('component_2_factor', models.DecimalField(decimal_places=2, default='NA', max_digits=50)),
                ('component_2_tolerance', models.DecimalField(decimal_places=2, default='NA', max_digits=50)),
                ('component_3_multiply_by', models.CharField(choices=[('AL', 'Alto'), ('AN', 'Ancho'), ('PE', 'Perímetro'), ('NA', 'Nada')], max_length=2)),
                ('component_3_factor', models.DecimalField(decimal_places=2, default='NA', max_digits=50)),
                ('component_3_tolerance', models.DecimalField(decimal_places=2, default='NA', max_digits=50)),
                ('making_multiply_by', models.CharField(choices=[('AL', 'Alto'), ('AN', 'Ancho'), ('PE', 'Perímetro'), ('NA', 'Nada')], max_length=2)),
                ('making_factor', models.DecimalField(decimal_places=2, default='NA', max_digits=50)),
                ('making_tolerance', models.DecimalField(decimal_places=2, default='NA', max_digits=50)),
                ('width', models.DecimalField(decimal_places=2, max_digits=10)),
                ('height', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('component_1_raw_material', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='item_raw_material_comp_1', to='costs.Cost', verbose_name='Materia prima componente 1')),
                ('component_2_raw_material', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='item_raw_material_comp_2', to='costs.Cost', verbose_name='Materia prima componente 2')),
                ('component_3_raw_material', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='item_raw_material_comp_3', to='costs.Cost', verbose_name='Materia prima componente 3')),
                ('making_cost', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='item_making_cost', to='costs.Cost', verbose_name='Costo confección')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
    ]