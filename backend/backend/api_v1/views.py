from rest_framework import generics, pagination, permissions, status
from rest_framework.response import Response

from api_v1.serializeers import IndexSerializer
from users.models import MyUser
from django.db.models import Q


class Index(generics.GenericAPIView):
    """Возвращает список пользователей"""

    queryset = MyUser.objects.all().order_by('id')
    serializer_class = IndexSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = pagination.PageNumberPagination

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
            
        filter_kwargs = {}
        if 'city' in request.data:
            filter_kwargs['city'] = request.data['city']
        if 'purpose' in request.data:
            filter_kwargs['purpose'] = request.data['purpose']
        queryset = queryset.filter(**filter_kwargs)

        if 'instrument' in request.data:
            instrument_value = request.data['instrument']
            q_conditions = (
                Q(instrument_1=instrument_value) |
                Q(instrument_2=instrument_value) |
                Q(instrument_3=instrument_value)
            )
            queryset = queryset.filter(q_conditions)
        
        queryset = queryset.order_by('id')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
    
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
