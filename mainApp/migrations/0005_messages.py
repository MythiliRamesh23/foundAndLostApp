# Generated by Django 4.0 on 2022-01-01 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_itemdetail_item_status_alter_itemdetail_datefl_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Message')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.itemdetail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.user')),
            ],
        ),
    ]