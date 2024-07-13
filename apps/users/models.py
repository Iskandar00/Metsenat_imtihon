from django.core.exceptions import ValidationError
from django.db import models

from apps.users.validate import phone_number_validate


class Sponsor(models.Model):
    class TypeChoices(models.TextChoices):
        YURIDIK = 'Yuridik'
        JISMONIY = 'Jismoniy'

    class PaymentChoices(models.TextChoices):
        NAQD = 'Naqd'
        ONLINE = 'Online'

    class StatusChoices(models.TextChoices):
        YANGI = 'Yangi'
        MODERATSIYADA = 'Moderatsiyada'
        TASDIQLANGAN = 'Tasdiqlangan'
        BEKOR_QILINGAN = 'Bekor qilingan'

    sponsor_type = models.CharField(max_length=10, choices=TypeChoices.choices)
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13, validators=[phone_number_validate])
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    company_name = models.CharField(max_length=250, blank=True)
    payment_type = models.CharField(max_length=10, choices=PaymentChoices.choices)

    status = models.CharField(max_length=50, choices=StatusChoices.choices, default=StatusChoices.YANGI)
    spand_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name}'

    def clean(self):
        super().clean()
        if self.sponsor_type == self.TypeChoices.YURIDIK.value and not self.company_name:
            raise ValidationError({'company_name': 'it is mandatory to enter the name of the legal entity companya'})
        if self.sponsor_type == self.TypeChoices.JISMONIY.value and self.company_name:
            raise ValidationError({'company_name': 'individuals cannot enter a company name'})




class Student(models.Model):
    class LevelChoices(models.TextChoices):
        MAGISTER = 'Magiter'
        BAKALAVR = 'Bakalavr'

    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13, validators=[phone_number_validate])
    place_of_study = models.ForeignKey('agreements.PlaceOfStudy', on_delete=models.PROTECT)
    level = models.CharField(max_length=10, choices=LevelChoices.choices)

    contract = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    sponsored_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name}'
