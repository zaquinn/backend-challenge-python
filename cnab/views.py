from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Cnab
from transactions.models import Transaction
from .serializers import CnabSerializer, TransactionSerializer
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser, JSONParser

from rest_framework.views import APIView, Request, Response, status


class CnabView(generics.ListCreateAPIView):
    queryset = Cnab.objects.all()
    serializer_class = CnabSerializer
    parser_classes = [MultiPartParser,JSONParser, FormParser, FileUploadParser]

    def post(self, request:Request, *args, **kwargs) -> Response:
        if request.FILES.get("file"):
                uploaded_file = request.FILES["file"].read()
                splited_lines = uploaded_file.decode("utf-8").splitlines()
                print(splited_lines)
                return Response("dentro loop", status.HTTP_201_CREATED)
        
        return Response("sucesso", status.HTTP_201_CREATED)
    
    # def perform_create(self, serializer):
    #     print(self.request.data)