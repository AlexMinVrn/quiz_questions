from rest_framework import serializers

from questions.models import Questions


class MyInputSerializer(serializers.Serializer):
    questions_num = serializers.IntegerField(max_value=100, min_value=1)


class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        exclude = ('id',)
