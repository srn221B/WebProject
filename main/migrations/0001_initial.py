# Generated by Django 2.2.6 on 2019-11-16 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents_name', models.CharField(max_length=255, verbose_name='作品名')),
            ],
            options={
                'db_table': 'ContentsList',
            },
        ),
    ]
