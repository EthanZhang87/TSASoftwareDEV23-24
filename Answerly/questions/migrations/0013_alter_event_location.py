# Generated by Django 4.2.3 on 2023-10-22 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0012_alter_question_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=200),
        ),
    ]
