from django.db import models

class User(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=120)
    second_name = models.CharField(verbose_name='Фамилия', max_length=120)
    email = models.CharField(verbose_name='Email', max_length=120)
    faculty_id = models.ForeignKey(to='Faculty', to_field='id', on_delete=models.CASCADE)
    university_id = models.ForeignKey(to='University', to_field='id', on_delete=models.CASCADE)
    department_id = models.ForeignKey(to='Department', to_field='id', on_delete=models.CASCADE)
    stud_or_stuff = models.CharField(verbose_name='Студент или Преподаватель', max_length=20)
    events = models.ManyToManyField(to='Event')
    def __str__(self):
       return self.first_name + ' ' + self.second_name + ' ' + self.email + ' ' + str(self.faculty_id) + ' ' + str(self.university_id) + ' ' + str(self.department_id) + ' ' + self.stud_or_stuff

class Faculty(models.Model):
    name = models.TextField(verbose_name='Название факультета')
    def __str__(self):
       return self.name +''

class University(models.Model):
    name = models.TextField(verbose_name='Название университета')
    def __str__(self):
           return self.name +''

class Department(models.Model):
    name = models.TextField(verbose_name='Название кафедры')
    def __str__(self):
           return self.name +''

class Project(models.Model):
    project_name = models.CharField(verbose_name='Название проекта', max_length=255)
    use_scope = models.TextField(verbose_name='Область применения')
    completion_date = models.DateField(verbose_name='Дата выполнения')
    mentor_id = models.ForeignKey(to='Mentor', to_field='id', null=True, on_delete=models.CASCADE)
    student_id = models.ManyToManyField(to='Student')
    mark = models.IntegerField(verbose_name='Оценка')
    def __str__(self):
           return self.project_name +''

class Event(models.Model):
    name = models.CharField(verbose_name='Название мероприятия', max_length=100)
    date = models.DateField(verbose_name='Дата мероприятия')
    mentors = models.ManyToManyField(to='Mentor')
    students = models.ManyToManyField(to='Student')
    def __str__(self):
           return self.name +' ' + str(self.date)

class Student(models.Model):
    group = models.CharField(verbose_name='Номер группы', max_length=10)
    project_number = models.IntegerField(verbose_name='Кол-во работ')
    average_mark = models.FloatField(verbose_name='Средняя оценка')
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    def __str__(self):
           return self.group + ' ' + str(self.user_id)

class Mentor(models.Model):
    project_number = models.IntegerField(verbose_name='Кол-во курируемых работ')
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    def __str__(self):
           return str(self.project_number) + ' ' + str(self.user_id)
