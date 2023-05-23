# Generated by Django 4.2.1 on 2023-05-22 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbank', '0011_alter_cliente_is_active_alter_cliente_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='cliente',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='username',
        ),
        migrations.AddField(
            model_name='cliente',
            name='nome',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]