# Generated by Django 4.2.3 on 2023-10-25 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0017_questionimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionimage',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='question_images'),
        ),
    ]
