# Generated by Django 4.1 on 2022-08-27 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notations', '0003_alter_notes_reminder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='reminder',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]