# Generated by Django 5.0.2 on 2024-02-25 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bngjobs',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='hydjobs',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='punejobs',
            name='address',
            field=models.TextField(),
        ),
    ]
