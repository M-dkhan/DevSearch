# Generated by Django 3.2.7 on 2021-10-01 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20210930_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='projects.Tag'),
        ),
    ]
