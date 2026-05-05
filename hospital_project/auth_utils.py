from django.contrib.auth.mixins import UserPassesTestMixin


def is_doctor(user):
    return user.is_authenticated and user.groups.filter(name="doctor").exists()


def is_administrator(user):
    return user.is_authenticated and user.groups.filter(name="administrator").exists()


class GroupRequiredMixin(UserPassesTestMixin):
    group_name = None

    def test_func(self):
        if not self.request.user.is_authenticated or not self.group_name:
            return False
        return self.request.user.groups.filter(name=self.group_name).exists()

