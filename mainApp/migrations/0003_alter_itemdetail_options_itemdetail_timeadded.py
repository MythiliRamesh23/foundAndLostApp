# Generated by Django 4.0 on 2022-01-01 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_itemdetail_delete_itemdetails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemdetail',
            options={'ordering': ['-timeAdded']},
        ),
        migrations.AddField(
            model_name='itemdetail',
            name='timeAdded',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
