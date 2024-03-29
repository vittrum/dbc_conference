# Generated by Django 3.1.7 on 2021-04-05 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_info', models.CharField(max_length=300)),
                ('is_approved', models.BooleanField(blank=True, default=None, null=True)),
                ('draft', models.BooleanField(default=True)),
                ('type', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'thesises',
            },
        ),
        migrations.CreateModel(
            name='ThesisReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('comment', models.CharField(default='no comment added', max_length=300)),
                ('thesis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thesis.thesis')),
            ],
            options={
                'db_table': 'thesises_reviews',
            },
        ),
    ]
