# Generated by Django 3.0.7 on 2020-06-16 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='twitter',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
