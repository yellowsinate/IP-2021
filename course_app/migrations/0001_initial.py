# Generated by Django 3.1.5 on 2021-01-11 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название кафедры')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название мероприятия')),
                ('date', models.DateField(verbose_name='Дата мероприятия')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название факультета')),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_number', models.IntegerField(verbose_name='Кол-во курируемых работ')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=10, verbose_name='Номер группы')),
                ('project_number', models.IntegerField(verbose_name='Кол-во работ')),
                ('average_mark', models.FloatField(verbose_name='Средняя оценка')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название университета')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=120, verbose_name='Фамилия')),
                ('email', models.CharField(max_length=120, verbose_name='Email')),
                ('stud_or_stuff', models.CharField(max_length=20, verbose_name='Студент или Преподаватель')),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.department')),
                ('events', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course_app.event')),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.faculty')),
                ('university_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.university')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255, verbose_name='Название проекта')),
                ('use_scope', models.TextField(verbose_name='Область применения')),
                ('completion_date', models.DateField(verbose_name='Дата выполнения')),
                ('mark', models.IntegerField(verbose_name='Оценка')),
                ('mentor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course_app.mentor')),
                ('student_id', models.ManyToManyField(to='course_app.Student')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='mentors',
            field=models.ManyToManyField(to='course_app.Mentor'),
        ),
        migrations.AddField(
            model_name='event',
            name='students',
            field=models.ManyToManyField(to='course_app.Student'),
        ),
    ]
