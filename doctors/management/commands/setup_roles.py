from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create default role groups: doctor and administrator."

    def handle(self, *args, **options):
        created_groups = []
        for group_name in ("doctor", "administrator"):
            _, created = Group.objects.get_or_create(name=group_name)
            if created:
                created_groups.append(group_name)

        if created_groups:
            self.stdout.write(
                self.style.SUCCESS(f"Created groups: {', '.join(created_groups)}")
            )
        else:
            self.stdout.write(self.style.WARNING("Groups already exist."))

