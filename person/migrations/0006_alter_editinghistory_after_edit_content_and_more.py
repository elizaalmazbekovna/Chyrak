# Generated by Django 4.1.7 on 2023-05-23 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_alter_editinghistory_date_of_editing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editinghistory',
            name='after_edit_content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='editinghistory',
            name='before_edit_content',
            field=models.TextField(default=''),
        ),
    ]
