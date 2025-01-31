# Generated by Django 5.1.5 on 2025-01-31 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('사업자등록번호', models.CharField(max_length=20, unique=True)),
                ('업체명', models.CharField(max_length=255, unique=True)),
                ('대표명', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('공고번호', models.CharField(max_length=50, unique=True)),
                ('입찰년도', models.IntegerField()),
                ('공고제목', models.TextField()),
                ('발주처', models.TextField()),
                ('지역제한', models.CharField(max_length=50)),
                ('기초금액', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('예정가격', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('예가범위', models.CharField(blank=True, max_length=50, null=True)),
                ('A값', models.DecimalField(decimal_places=2, max_digits=15)),
                ('투찰률', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('참여업체수', models.IntegerField()),
                ('공고구분표시', models.CharField(blank=True, max_length=100, null=True)),
                ('정답사정률', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('순위', models.IntegerField()),
                ('투찰금액', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('가격점수', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('예가대비투찰률', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('기초대비투찰률', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('기초대비사정률', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('추첨번호', models.CharField(blank=True, max_length=30, null=True)),
                ('낙찰여부', models.BooleanField(default=False)),
                ('투찰일시', models.DateTimeField(blank=True, null=True)),
                ('비고', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.notice')),
            ],
        ),
    ]
