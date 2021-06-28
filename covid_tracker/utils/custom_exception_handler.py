from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import MethodNotAllowed, Throttled

import logging
import traceback
logger = logging.getLogger('django')

def exception_handler(exc, context):
    if isinstance(exc, MethodNotAllowed):
        return Response({
            "status": "error",
            "message": 'Method Not Allowed',
            "data": None
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    if not isinstance(exc, Exception):
        # this is an unknown exception
        logger.error(
            "API EXCEPTION",
            extra={
                "api_exception": {
                    "message": str(exc),
                    "traceback": ''.join(traceback.format_tb(exc.__traceback__))
                }
            }
        )

        response = Response({
            "status": "error",
            "message": "An internal server error occured",
            "data": None,
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        response = Response({
            "status": "Value Error",
            "message": exc.__dict__,
            "data": None
        }, status=500)
    return response