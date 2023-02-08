# Generated by Django 4.1.6 on 2023-02-03 16:02

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('googleMaps', '0003_alter_gmimage_latitude_alter_gmimage_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='gmimage',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gmimage',
            name='image',
            field=models.ImageField(upload_to=pathlib.PureWindowsPath('C:/Users/Sambr/OneDrive/Documents/DTD/TreesFromForrest/TreeVsForrest/base/media/images')),
        ),
    ]