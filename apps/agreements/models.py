from django.core.exceptions import ValidationError
from django.db import models

from apps.users.models import Sponsor


class Agreement(models.Model):
    sponsor = models.ForeignKey('users.Sponsor', on_delete=models.PROTECT,
                                limit_choices_to={'status': Sponsor.StatusChoices.TASDIQLANGAN},
                                related_name='agreement')
    student = models.ForeignKey('users.Student', on_delete=models.PROTECT, related_name='agreement')
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def clean(self):
        super().clean()
        obj = Agreement.objects.filter(sponsor_id=self.sponsor.id, student_id=self.student.id).last()
        if not obj:
            if 0.0 >= self.sponsor.amount - self.sponsor.spand_amount:
                raise ValidationError({'sponsor': 'the sponsor has run out of money'})

            if self.sponsor.amount - self.sponsor.spand_amount < self.amount:
                raise ValidationError({'sponsor': 'the sponsor does not pay'})

            if self.student.contract - self.student.sponsored_amount <= self.amount:
                raise ValidationError({'student': 'this money is a lot for a student'})

            if self.student.contract - self.student.sponsored_amount <= 0:
                raise ValidationError({'student': 'This student has enough money'})
        else:
            if self.sponsor.amount - self.sponsor.spand_amount < self.amount:
                raise ValidationError({'sponsor': 'the sponsor does not pay'})

    def save(self, *args, **kwargs):
        amount = self.amount
        self.student.sponsored_amount += amount
        self.student.save()
        self.sponsor.spand_amount += amount
        self.sponsor.save()

        super().save(*args, **kwargs)


class PlaceOfStudy(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
