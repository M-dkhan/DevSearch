# Generated by Django 3.2.7 on 2021-09-30 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name_plural': 'Projects'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name_plural': 'Review'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': 'Tag'},
        ),
        migrations.AlterField(
            model_name='review',
            name='vote',
            field=models.CharField(blank=True, default=(('up_vote', 'Up Vote'), ('down_vote', 'Down Vote')), max_length=2, null=True),
        ),
    ]
