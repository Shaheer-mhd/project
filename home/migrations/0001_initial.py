# Generated by Django 4.0.1 on 2022-03-24 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Place', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Ph', models.IntegerField()),
                ('Height', models.IntegerField()),
                ('Weight', models.IntegerField()),
            ],
        ),
    ]
