# Generated by Django 4.0.1 on 2022-03-25 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='Name',
            new_name='NAMAM',
        ),
        migrations.AlterField(
            model_name='member',
            name='Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
