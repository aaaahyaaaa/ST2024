# Generated by Django 4.0.3 on 2024-05-10 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='List',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='lists.list'),
        ),
    ]
