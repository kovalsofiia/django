# Лабораторна робота 1 (Django)

## Тема
Базова структура проєкту та моделювання предметної області психіатричної лікарні.

## Структура застосунків
- `doctors` - сутність `Doctor`
- `appointments` - сутність `Appointment`

## Швидкий запуск
```bash
./venv/bin/python manage.py migrate
./venv/bin/python manage.py createsuperuser
./venv/bin/python manage.py runserver
```

Admin-панель: `http://127.0.0.1:8000/admin/`

## Наповнення тестовими даними через admin
1. Створіть декілька лікарів у розділі `Doctors`.
2. Створіть записи в `Appointments`, обираючи лікаря із вже створених.
3. Для частини записів заповніть `diagnosis` і `treatment_description`.

## Базові ORM-запити (для захисту)
Запустити shell:
```bash
./venv/bin/python manage.py shell
```

```python
from datetime import date
from django.utils import timezone
from doctors.models import Doctor
from appointments.models import Appointment

# 1) Фільтрація записів за датою прийому (на конкретний день)
Appointment.objects.filter(appointment_date__date=date(2026, 5, 5))

# 2) Лікарі зі стажем від 10 років
Doctor.objects.filter(experience_years__gte=10)

# 3) Усі записи конкретного лікаря
doctor = Doctor.objects.get(full_name="Іваненко Іван Іванович")
doctor.appointments.all()

# 4) Майбутні записи, відсортовані за датою
Appointment.objects.filter(appointment_date__gte=timezone.now()).order_by("appointment_date")
```

## Лабораторна 4: ролі, сесії, cookies

- Сесія:
  - при відкритті деталей запису зберігається `last_viewed_appointment_id`;
  - сторінка `appointments/last/` перекидає на останній переглянутий запис.
- Cookies:
  - фільтр `diagnosis` на сторінці короткого списку записів зберігається в cookie.
- Ролі через групи:
  - `doctor` - може редагувати записи до лікаря;
  - `administrator` - може додавати та редагувати лікарів.

Створити ролі:
```bash
./venv/bin/python manage.py setup_roles
```

Потім призначити групи користувачам через admin (`Users` -> `Groups`).
