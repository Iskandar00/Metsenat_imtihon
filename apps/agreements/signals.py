import os
from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.agreements.models import Agreement
from apps.users.models import Sponsor


@receiver(pre_save, sender=Agreement)
def delete_photo_on_delete_user(instance, *args, **kwargs):
    obj = Agreement.objects.filter(sponsor_id=instance.sponsor.id, student_id=instance.student.id).last()
    if not obj:
        return instance
    amount = obj.amount
    sponsor = Sponsor.objects.filter(id=instance.sponsor.id).last()
    sponsor.spand_amount -= amount
    sponsor.save()
