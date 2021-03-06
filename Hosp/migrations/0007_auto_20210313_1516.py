# Generated by Django 3.1.4 on 2021-03-13 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hosp', '0006_auto_20210306_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medname', models.CharField(max_length=50)),
                ('medmg', models.CharField(max_length=50)),
                ('dose', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='dose',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='medmg',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='medname',
        ),
    ]
