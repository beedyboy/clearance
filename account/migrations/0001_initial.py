# Generated by Django 2.1.4 on 2019-01-22 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.CharField(max_length=15, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'student'), (2, 'lecturer'), (3, 'bursary'), (4, 'system'), (5, 'admin')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('dept_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.DepartmentData')),
                ('semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.SemesterData')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]