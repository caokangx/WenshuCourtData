# Generated by Django 3.0.6 on 2020-05-18 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docId', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=99999)),
                ('court', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('causeOfAction', models.CharField(max_length=100)),
                ('processing', models.CharField(max_length=100)),
                ('litigant', models.CharField(max_length=100)),
                ('productName', models.CharField(max_length=100)),
                ('criteria', models.CharField(max_length=100)),
                ('publishDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.Document')),
            ],
        ),
    ]
