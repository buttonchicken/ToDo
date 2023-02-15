from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from .serializers import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist

class AddTask(APIView):
    authentication_classes = [JWTAuthentication]
    def post(self,request):
        data = request.data
        try:
            task_data = data['task_data']
            task_obj = Task.objects.create(created_by = request.user, task_data=task_data)
            serializer = TaskSerializer(task_obj)
            return Response({"Success":True, "message":"Task created successfully","task":serializer.data},status = status.HTTP_200_OK)
        except:
            return Response({"Success":False, "message":"Please enter task data"},status=status.HTTP_400_BAD_REQUEST)

class MarkCompleted(APIView):
    authentication_classes = [JWTAuthentication]
    def put(self,request):
        data = request.data
        try:
            task_obj = Task.objects.filter(task_id = data['task_id'])
            if len(task_obj)==0:
                return Response({"Success":False, "message":"Invalid Task ID"},status=status.HTTP_400_BAD_REQUEST)
            elif task_obj[0].created_by != request.user:
                 return Response({"Success":False, "message":"you cannot edit a task you did not create"},status=status.HTTP_400_BAD_REQUEST)
            else:
                task_obj.update(status = "COMPLETED")
                return Response({"Success":True, "message":"Task marked completed !!"},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({"Success":False, "message":"Please enter Task ID"},status=status.HTTP_400_BAD_REQUEST)

class DeleteTask(APIView):
    authentication_classes = [JWTAuthentication]
    def delete(self,request):
        data = request.data
        try:
            task_obj = Task.objects.filter(task_id = data['task_id'])
            if len(task_obj)==0:
                return Response({"Success":False, "message":"Invalid Task ID"},status=status.HTTP_400_BAD_REQUEST)
            elif task_obj[0].created_by != request.user:
                 return Response({"Success":False, "message":"you cannot delete a task you did not create"},status=status.HTTP_400_BAD_REQUEST)
            else:
                task_obj.delete()
                return Response({"Success":True, "message":"Task deleted !!"},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({"Success":False, "message":"Please enter Task ID"},status=status.HTTP_400_BAD_REQUEST)

class ShowAllTask(APIView):
    authentication_classes = [JWTAuthentication]
    def get(self,request):
        task_objs = Task.objects.filter(created_by = request.user)
        data = TaskSerializer(task_objs,many = True).data
        return Response({"Success":True, "Tasks":data},status = status.HTTP_200_OK)
        