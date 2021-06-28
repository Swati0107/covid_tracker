from django.db import models
from django.db.models.deletion import DO_NOTHING
from phonenumber_field.modelfields import PhoneNumberField
from django_mysql.models import ListCharField

class User(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = PhoneNumberField()
    pincode = models.IntegerField()
    role = models.CharField(max_length=100, default='user')

    class Meta:
        db_table = 'users'


class UserSymptom(models.Model):
    user_id = models.ForeignKey(User, on_delete=DO_NOTHING)
    symptoms = ListCharField(base_field=models.CharField(max_length=255), max_length=255)
    travel_hostory = models.BooleanField(default=False)
    covid_contact = models.BooleanField(default=False)
    covid_risk = models.IntegerField(default=5)

    class Meta:
        db_table = 'user_symptoms'

    def save(self, *args, **kwargs):
        if len(self.symptoms) == 0 and not (self.travel_hostory) and not (self.covid_contact):
            self.covid_risk = 5
        elif self.travel_hostory or self.covid_contact:
            if len(self.symptoms) == 1: 
                self.covid_risk = 50
            elif len(self.symptoms) == 2:
                self.covid_risk = 75
            elif len(self.symptoms) > 2:
                self.covid_risk = 95
        super(UserSymptom, self).save(*args, **kwargs)


class CovidResult(models.Model):
    user_id = models.ForeignKey(User, on_delete=DO_NOTHING, related_name='user_id')
    admin_id = models.ForeignKey(User, on_delete=DO_NOTHING, related_name='admin_id')
    covid_result = models.CharField(max_length=100)

    class Meta:
        db_table = 'covid_results'


class Zone(models.Model):
    pincodes = models.IntegerField()
    zone_status= models.BooleanField()

    class Meta:
        db_table = 'zones'
