# Generated by Django 4.2.16 on 2024-12-02 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_tbl_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Adminreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminreg_name', models.CharField(max_length=50)),
                ('adminreg_email', models.CharField(max_length=50)),
                ('adminreg_password', models.CharField(max_length=50)),
            ],
        ),
    ]
