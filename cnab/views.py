from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Cnab
from transactions.models import Transaction
from .serializers import CnabSerializer, TransactionSerializer
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser, JSONParser
from datetime import datetime
import datetime as dt
from django.forms.models import model_to_dict

from rest_framework.views import APIView, Request, Response, status


class CnabView(APIView):
    parser_classes = [MultiPartParser,JSONParser, FormParser, FileUploadParser]

    def get(self, request:Request) -> Response:
        queryset = Cnab.objects.all()

        serializer = CnabSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request:Request) -> Response:
        if request.FILES.get("file"):
                uploaded_file = request.FILES["file"].read()
                splited_lines = uploaded_file.decode("utf-8").splitlines()
                response = []
                for line in splited_lines:
                    cnab_type = line[0:1]
                    cnab_date = datetime.strptime(line[1:9], '%Y%m%d').strftime('%Y-%m-%d')
                    cnab_value = line[9:19]
                    cnab_cpf = line[19:30]
                    cnab_card = line[30:42]
                    cnab_time_info = line[42:48]
                    cnab_hour = cnab_time_info[0:2]
                    cnab_minute = cnab_time_info[2:4]
                    cnab_second = cnab_time_info[4:6]
                    cnab_time = dt.time(int(cnab_hour), int(cnab_minute), int(cnab_second))
                    cnab_owner = line[48:62]
                    cnab_store = line[62:81]

                    transaction = Transaction.objects.get(pk=int(cnab_type))

                    data = {"date": cnab_date, "value": cnab_value, "cpf": cnab_cpf, "card": cnab_card, "hour": cnab_time, "owner": cnab_owner, "store_name": cnab_store}
                    serializer = CnabSerializer(data=data, context={"transaction_id": int(cnab_type)})
                    serializer.is_valid(raise_exception=True)
                    serializer.save(transaction=transaction)
                    response.append(serializer.data)
                    
                    
                return Response(response, status.HTTP_201_CREATED)
        
        return Response("Invalid CNAB file", status.HTTP_404_NOT_FOUND)