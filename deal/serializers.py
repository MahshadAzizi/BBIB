from rest_framework import serializers
from .models import Deal


class DealSerializer(serializers.ModelSerializer):
    branch_code = serializers.CharField(source='user.branch_code')
    wage = serializers.DecimalField(source='calculate_wage', max_digits=20, decimal_places=2)
    national_code = serializers.CharField(source='user.national_code')

    class Meta:
        model = Deal
        fields = ['id', 'national_code', 'branch_code', 'wage']
