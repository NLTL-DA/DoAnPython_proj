from rest_framework import serializers
from .models import Staff


class StaffSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    user_full_name = serializers.CharField(source='user.get_full_name', read_only=True)

    class Meta:
        model = Staff
        fields = ['id', 'user', 'user_username', 'user_full_name', 'role', 
                'phone', 'address', 'salary', 'hire_date', 'is_active']
