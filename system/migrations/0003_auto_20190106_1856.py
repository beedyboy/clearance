# Generated by Django 2.1.4 on 2019-01-06 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_departmentdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='SemesterData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SessionData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='semesterdata',
            name='sid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.SessionData'),
        ),
    ]