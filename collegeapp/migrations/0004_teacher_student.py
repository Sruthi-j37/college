# Generated by Django 4.2.7 on 2023-11-26 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0003_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teachername', models.CharField(max_length=255)),
                ('age', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('image', models.FileField(null=True, upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('joiningdate', models.DateField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collegeapp.course')),
            ],
        ),
    ]
