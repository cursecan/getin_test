# Generated by Django 2.2.6 on 2019-10-23 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('uid', models.UUIDField(default=uuid.UUID('db31c7bc-7edb-49b0-9816-f48e92e96327'), editable=False, unique=True)),
                ('no_telp', models.CharField(blank=True, max_length=16)),
                ('gender', models.CharField(choices=[('P', 'Pria'), ('W', 'Wanita')], default='P', max_length=1)),
                ('is_dirver', models.BooleanField(default=False)),
                ('no_kendaraan', models.CharField(blank=True, max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
