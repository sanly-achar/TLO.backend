# Generated by Django 4.1 on 2022-08-15 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlo_ru', '0006_contacts_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='news', verbose_name='LOGO'),
        ),
    ]
