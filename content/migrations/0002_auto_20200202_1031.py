# Generated by Django 2.2 on 2020-02-02 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='top_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Category'),
        ),
    ]
