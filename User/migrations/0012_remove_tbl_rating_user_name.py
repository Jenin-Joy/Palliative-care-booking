# Generated by Django 5.2 on 2025-04-19 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_tbl_rating_paliativecare_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_rating',
            name='user_name',
        ),
    ]
