# Generated by Django 5.0.6 on 2024-06-05 14:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('creat_game', models.CharField(max_length=100)),
                ('team', models.TextField(null=True)),
                ('team_positions', models.CharField(choices=[('support', 'Support'), ('mid', 'Mid'), ('tank', 'Tank')])),
                ('mid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mid_game', to=settings.AUTH_USER_MODEL)),
                ('support', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='support_game', to=settings.AUTH_USER_MODEL)),
                ('tank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tank_game', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
