# Generated by Django 2.2.6 on 2019-11-28 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20191128_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review_ratings',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
