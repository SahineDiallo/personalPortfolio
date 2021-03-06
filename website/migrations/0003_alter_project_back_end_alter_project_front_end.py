# Generated by Django 4.0.4 on 2022-04-29 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_technology_project_back_end_project_front_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='back_end',
            field=models.ManyToManyField(blank=True, related_name='back', to='website.technology'),
        ),
        migrations.AlterField(
            model_name='project',
            name='front_end',
            field=models.ManyToManyField(blank=True, related_name='front', to='website.technology'),
        ),
    ]
