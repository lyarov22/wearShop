# Generated by Django 4.2.5 on 2023-12-05 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userSystem', '0006_alter_profile_name_alter_profile_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='surname',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]