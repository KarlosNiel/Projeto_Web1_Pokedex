# Generated by Django 5.1.3 on 2024-11-14 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_web1', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='gen',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.FileField(upload_to='static/assets/images/pokemons'),
        ),
    ]
