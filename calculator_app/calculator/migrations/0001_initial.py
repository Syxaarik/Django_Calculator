# Generated by Django 5.1.4 on 2024-12-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='calc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count1', models.IntegerField(default=0)),
                ('count2', models.IntegerField(default=0)),
                ('app', models.CharField(max_length=2)),
            ],
        ),
    ]
