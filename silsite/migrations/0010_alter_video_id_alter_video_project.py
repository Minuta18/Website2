# Generated by Django 4.0.4 on 2022-06-09 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('silsite', '0009_video_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='video',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silsite.project'),
        ),
    ]