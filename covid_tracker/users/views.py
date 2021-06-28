import traceback
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import *
from utils.exceptions import *
from users.services.user_services import UserService
from utils.helper import serializer_error_message
import traceback
import logging
logger = logging.getLogger('django')

class UserRegisterView(APIView):

    def post(self, request):
        serialized_data = UserRegisterSerializer(data=request.data)

        if not serialized_data.is_valid():
            return InvalidInput(serializer_error_message(serialized_data.errors))
        
        user_name, mobile, pin_code = [serialized_data.data[key] for key in ['name', 'phoneNumber', 'pinCode']]
        
        try:
            user_id = UserService().register_user(user_name, mobile, pin_code)

            logger.info(f'UserRegistration Successful for username: {user_name}')

            return Response({
                'status': 200,
                'message': 'Registration Successful',
                'data': {"userId": user_id}
            })

        except Exception as exc:
            logger.exception(f'UserRegistration Failed due to: {exc.message}')
            return Response({
                'status': 500,
                'message': 'Registration Failed',
                'data': {'error': exc.message}
            })


class UserAdminRegisterView(APIView):

    def post(self, request):
        serialized_data = UserRegisterSerializer(data=request.data)

        if not serialized_data.is_valid():
            raise InvalidInput(serializer_error_message(serialized_data.errors))
        
        user_name, mobile, pin_code = [serialized_data.data[key] for key in ['name', 'phoneNumber', 'pinCode']]
        
        try:
            admin_id = UserService().register_user(user_name, mobile, pin_code, True)

            logger.info(f'UserRegistration Successful for username: {user_name}')

            return Response({
                'status': 200,
                'message': 'Registration Successful',
                'data': {"adminId": admin_id}
            })
        except Exception as exc:
            logger.exception(f'UserRegistration Failed due to: {exc.message}')
            return Response({
                'status': 500,
                'message': 'Registration Failed',
                'data': {'error': exc.message}
            })


class UserAssessmentView(APIView):

    def post(self, request):
        serialized_data = UserAssessmentSerializer(data=request.data)

        if not serialized_data.is_valid():
            raise InvalidInput(serializer_error_message(serialized_data.errors))
        
        user_id, symptoms, travel_hostory, covid_contact = [serialized_data.data[key] for key in ['userId', 'symptoms', 'travelHistory', 'contactWithCovidPatient']]
        
        try:
            risk_percentage = UserService().record_user_assessment(user_id, symptoms, travel_hostory, covid_contact)

            logger.info(f'UserAssessment Successful for userId: {user_id}')

            return Response({
                'status': 200,
                'message': 'UserAssessment Recorded Successfully',
                'data': {"riskPercentage": risk_percentage}
            })

        except Exception as exc:
            traceback.print_exc()
            logger.exception(f'UserAssessment Failed due to: {exc.message}')
            return Response({
                'status': 500,
                'message': 'UserAssessment Failed',
                'data': {'error': exc.message}
            })



class UsereCovidResultView(APIView):

    def put(self, request):
        serialized_data = UserCovidResultSerializer(data=request.data)

        if not serialized_data.is_valid():
            raise InvalidInput(serializer_error_message(serialized_data.errors))
        
        user_id, admin_id, result = [serialized_data.data[key] for key in ['userId', 'adminId', 'result']]
        
        try:
            updated_status = UserService().update_covid_result(user_id, admin_id, result)

            logger.info(f'User Covid Result Updated Successfully for username: {user_id}')

            return Response({
                'status': 200,
                'message': 'Covid Result Updation Successful',
                'data': {"updated": updated_status}
            })
        except Exception as exc:
            logger.exception(f'User Covid Result Updation Failed due to: {exc.message}')
            return Response({
                'status': 500,
                'message': 'User Covid Result Failed',
                'data': {'error': exc.message}
            })
