# Generated by Django 3.1.1 on 2020-10-17 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hackathon', '0006_auto_20201016_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathon',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hackathons', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hackproject',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hackprojects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hackprojectscore',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hackprojectscores', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hackprojectscorecategory',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hackprojectscorecategories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hackteam',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hackteams', to=settings.AUTH_USER_MODEL),
        ),
    ]