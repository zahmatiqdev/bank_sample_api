from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from bank.models import Account


class AccountSerializer(serializers.ModelSerializer):
    """Serializer for the Account object"""

    class Meta:
        model = Account
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}

    def validate_iban(self, iban):
        """According to banking information, the causal code is 22 characters.
        In this section, it must be checked that the first two characters must be strings"""
        if len(iban) != 22:
            raise serializers.ValidationError("This IBAN is invalid.")
            
        # Sample of IBAN: "DE89370400440532013000"
        # Check if this is a number or a letter
        country_code = iban[:2].isalpha()
        if not country_code:
            raise serializers.ValidationError("The country code of IBAN is invalid.")
        return iban

    def validate_first_name(self, first_name):
        if len(first_name) <= 2:
            raise serializers.ValidationError("This name is too short.")
        return first_name
    
    def validate_last_name(self, last_name):
        if len(last_name) <= 2:
            raise serializers.ValidationError("This family is too short.")
        return last_name
    
    def validate(self, attrs):
        """Avoid duplicate information."""
        first_name = attrs.get('first_name')
        last_name = attrs.get('last_name')
        iban = attrs.get('iban')
        qs = Account.objects.filter(first_name=first_name, last_name=last_name, iban=iban)
        if qs.exists():
            raise serializers.ValidationError("This information already exists")
        return attrs
