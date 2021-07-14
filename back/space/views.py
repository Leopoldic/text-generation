import json

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from loguru import logger

from .serializers import UploadSerializer

from .algorithms.summarize import summarize
from .algorithms.gpt2 import generate, mode


# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')

        return Response(file_uploaded.read())

class UploadTexts(ViewSet):
    # serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        rez = []
        if len(request.data.get('text'))>0:
            text = summarize(request.data.get('text'))
        else:
            text = 'The '
        size = request.data.get('model').split('-')[1]
        word_num = request.data.get('word_num')
        text_num = request.data.get('text_num')
        for i in range(int(text_num)):
            new_text = generate(mode[size]['model'].to('cpu'),mode[size]['tokenizer'],text,entry_count=1,entry_length=int(word_num))
            rez.append(new_text)
        return Response(rez)
