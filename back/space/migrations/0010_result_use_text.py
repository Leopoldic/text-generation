# Generated by Django 3.1.2 on 2021-07-05 11:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('space', '0009_auto_20210703_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='use_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generate_text', models.CharField(max_length=10000)),
                ('bleu', models.IntegerField()),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('term_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='space.use_text')),
            ],
        ),
    ]