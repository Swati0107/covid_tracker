from users.models import *
from utils.exceptions import UserDoesNotExist

class UserService():

    def register_user(self, user_name, mobile, pincode, role=None):
        if role:
            user = User.objects.get_or_create(name=user_name, mobile_number=mobile, pincode=pincode, role='admin')
        else:
            user = User.objects.get_or_create(name=user_name, mobile_number=mobile, pincode=pincode)

        return user[0].id

    def record_user_assessment(self, user_id, symptoms, travel_hostory, covid_contact):
        try:
            user = User.objects.get(id=user_id)
            covid_symptom, created = UserSymptom.objects.get_or_create(user_id=user, symptoms=symptoms, travel_hostory=travel_hostory, covid_contact=covid_contact)
            covid_risk = covid_symptom.covid_risk
            return covid_risk
        except User.DoesNotExist as exec:
            raise UserDoesNotExist()
        
    def update_covid_result(self, user_id, admin_id, result):
        try:
            user = User.objects.get(id=user_id)
            admin = User.objects.get(id=admin_id)
            user_covid = CovidResult.objects.filter(user_id=user, admin_id=admin).update(covid_result=result)
            return True
        except User.DoesNotExist as exec:
            raise UserDoesNotExist()