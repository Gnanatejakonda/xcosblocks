from simulationAPI.serializers import TaskSerializer
from simulationAPI.tasks import process_task
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from celery.result import AsyncResult
import uuid
import logging


logger = logging.getLogger(__name__)


class XmlUploader(APIView):
    '''
    API for XmlUpload

    Requires a multipart/form-data POST Request with Xml file in the
    'file' parameter
    '''
    permission_classes = (AllowAny,)
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, *args, **kwargs):
        logger.info('Got POST for Xml upload: data=%s', request.data)
        serializer = TaskSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            task_id = serializer.data['task_id']
            logger.info('task_id=%s %s', task_id, type(task_id))
            celery_task = process_task.apply_async(
                kwargs={'task_id': str(task_id)}, task_id=str(task_id))
            response_data = {
                'state': celery_task.state,
                'details': serializer.data,
            }
            return Response(response_data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CeleryResultView(APIView):
    """

    Returns Simulation results for 'task_id' provided after
    uploading the xml
    /api/task/<uuid>

    """
    permission_classes = (AllowAny,)
    methods = ['GET']

    def get(self, request, task_id):

        if isinstance(task_id, uuid.UUID):
            celery_result = AsyncResult(str(task_id))
            response_data = {
                'state': celery_result.state,
                'details': celery_result.info
            }
            return Response(response_data)
        else:
            raise ValidationError('Invalid uuid format')
