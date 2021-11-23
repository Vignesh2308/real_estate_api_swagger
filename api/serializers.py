from rest_framework import serializers
from .models import Agent


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('agent_id', 'agent_email', 'agent_contact', 'agent_name', 'customer_id')