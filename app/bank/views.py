from datetime import datetime

from django.shortcuts import get_object_or_404

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins

from bank.serializers import AccountSerializer
from bank.models import Account
from bank.permissions import IsOwnerOfObject


class AccountListAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated, IsOwnerOfObject)
    
    """ In this section, the account is created and also 
    the list of all customer accounts is displayed """
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AccountAPIDetailView(mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated, IsOwnerOfObject)

    """ This section displays the details display - 
    update and delete data"""
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
