import requests
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api_questions.serializers import MyInputSerializer, QuestionsSerializer
from questions.models import Questions

URL = 'https://jservice.io/api/random?count='


@api_view(['POST'])
def questions(request):
    count_questions = 0
    serializer = MyInputSerializer(data=request.data)
    if serializer.is_valid():
        count = serializer.data['questions_num']
        tp_api = URL + str(count)
        response_data = requests.get(tp_api).json()
        for res_data in response_data:
            if not Questions.objects.filter(
                text_question=res_data['question']
            ).exists():
                question = Questions(
                    id_question=res_data['id'],
                    text_question=res_data['question'],
                    text_answer=res_data['answer'],
                    created_at=res_data['created_at'],
                )
                question.save()
                count_questions += 1
        result = count - count_questions
        if result != 0:
            return requests.post(reverse(
                'questions',
                kwargs={'questions_num': result}))

        last_obj = Questions.objects.last()
        if last_obj is None:
            return None
        else:
            serializer_for_last_obj = QuestionsSerializer(
                instance=last_obj
            )
            return Response(serializer_for_last_obj.data,
                            status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
