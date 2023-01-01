from django.http import JsonResponse
from .models import CrudAPI
from .serializers import CrudSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def crud_list(request, format=None):
    # get all the crud_api
    # serialize them
    # return json

    if request.method == 'GET':
        crudapi = CrudAPI.objects.all()
        serializer = CrudSerializer(crudapi, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CrudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def crud_detail(request, id, format=None):
    try:
        crudapi = CrudAPI.objects.get(pk=id)
    except CrudAPI.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CrudSerializer(crudapi)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CrudSerializer(crudapi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        crudapi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)