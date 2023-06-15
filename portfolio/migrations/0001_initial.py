# Generated by Django 4.2.1 on 2023-06-06 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('conteudo', models.TextField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.area')),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('LIKE', 'Like'), ('DISLIKE', 'Dislike')], max_length=10)),
                ('artigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.artigo')),
            ],
        ),
        migrations.CreateModel(
            name='DonoBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('blog', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portfolio.blog')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('artigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.artigo')),
            ],
        ),
        migrations.AddField(
            model_name='artigo',
            name='autores',
            field=models.ManyToManyField(to='portfolio.autor'),
        ),
    ]