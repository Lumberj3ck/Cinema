# Generated by Django 4.2.3 on 2023-07-28 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FilmLibrary', '0003_film_rating_counts_alter_film_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='age',
            field=models.CharField(default=34, max_length=200),
        ),
        migrations.AlterField(
            model_name='actor',
            name='biography',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='actor',
            name='career',
            field=models.CharField(default='Актер', max_length=200),
        ),
        migrations.AlterField(
            model_name='actor',
            name='date_of_birth',
            field=models.CharField(default=' ', max_length=100, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='url',
            field=models.URLField(default=' '),
        ),
        migrations.AlterField(
            model_name='director',
            name='age',
            field=models.CharField(default=34, max_length=200),
        ),
        migrations.AlterField(
            model_name='director',
            name='biography',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='director',
            name='career',
            field=models.CharField(default='Актер', max_length=200),
        ),
        migrations.AlterField(
            model_name='director',
            name='date_of_birth',
            field=models.CharField(default=' ', max_length=100, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='director',
            name='url',
            field=models.URLField(default=' '),
        ),
        migrations.AlterField(
            model_name='film',
            name='budget',
            field=models.IntegerField(default=12000000, verbose_name='Бюджет'),
        ),
        migrations.AlterField(
            model_name='film',
            name='country',
            field=models.CharField(default='Франция', max_length=200, verbose_name='Страна выхода'),
        ),
        migrations.AlterField(
            model_name='film',
            name='description',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.URLField(blank=True, default=' '),
        ),
        migrations.AlterField(
            model_name='film',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=6, max_digits=5),
        ),
        migrations.AlterField(
            model_name='film',
            name='rating_counts',
            field=models.IntegerField(default=1233, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='year',
            field=models.IntegerField(default=2023),
        ),
    ]
