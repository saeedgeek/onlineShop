# Generated by Django 2.2 on 2020-02-02 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('top_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('weight', models.SmallIntegerField()),
                ('color', models.CharField(choices=[('rd', 'red'), ('gl', 'gold'), ('bk', 'black'), ('wt', 'white'), ('gn', 'green'), ('pr', 'purple')], max_length=200)),
                ('price', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Category')),
            ],
        ),
        migrations.CreateModel(
            name='laptop',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.Product')),
                ('cpu', models.CharField(max_length=50)),
                ('ram', models.CharField(max_length=50)),
                ('hard', models.CharField(max_length=50)),
                ('os', models.CharField(max_length=50)),
            ],
            bases=('content.product',),
        ),
        migrations.CreateModel(
            name='mobile',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.Product')),
                ('cpu', models.CharField(max_length=50)),
                ('ram', models.CharField(max_length=50)),
                ('hard', models.CharField(max_length=50)),
                ('os', models.CharField(choices=[('an', 'android'), ('is', 'ios'), ('wp', 'windows phone')], max_length=50)),
            ],
            bases=('content.product',),
        ),
        migrations.CreateModel(
            name='Product_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.SmallIntegerField()),
                ('crt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Cart')),
                ('prdc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Product')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(through='content.Product_Cart', to='content.Product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile'),
        ),
    ]
