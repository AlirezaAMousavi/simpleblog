# Generated by Django 5.1 on 2024-09-11 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_id_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id_code',
            field=models.CharField(default=1676856977392, max_length=20, unique=True),
        ),
    ]
