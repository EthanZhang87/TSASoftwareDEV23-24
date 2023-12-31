# Generated by Django 4.2.3 on 2023-10-22 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0014_question_participants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='response',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='event',
            name='created',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
