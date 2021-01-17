from .models import User, Mentor, Event

print(User.objects.all())
print(User.objects.filter(first_name="Владимир"))
print(Event.objects.all().filter(name='День рождения!'))