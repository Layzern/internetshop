# Generated by Django 5.1.1 on 2024-09-11 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magaz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
    ]
