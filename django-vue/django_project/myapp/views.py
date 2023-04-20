from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Dictionary
from .serializers import DictionarySerializer

from rest_framework import viewsets, filters
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.response import Response

class IndexView(TemplateView):
    template_name = 'index.html'

# 範囲指定時
class DictionaryViewSet(APIView):
    def get(self, request):
        morethan = request.GET.get('more')
        lessthan = request.GET.get('less')
        
        queryset = Dictionary.objects.filter(vocabindex__gte=morethan,vocabindex__lte=lessthan).values()
        return Response(queryset)

# 全リスト取得時
class DictionaryAllViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer

