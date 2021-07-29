# 21.07.29
# WEB API를 시작하기 위한 클래스 정의

from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# Serialization 
# 데이터는 참조 형식(ex: 포인터), 값 형식으로 사용 됨
# 디스크에 저장하기 위해서는 값 형식으로만 저장이 가능 (참조형식은 메모리 주소가 달라지면 알 수 없음)
# 데이터 직렬화(Serialization)을 통해 텍스트 또는 바이너리 등의 형태가 되는 데
# 이러한 형태가 저장하거나 통신 시 파싱이 가능한 유의미한 데이터가 된다.  

# 커스텀 소스
# class SnippetSerializer(serializers.Serializer):

#     # 내부적으로 Djongo의 Form 클래스를 사용함 
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template':'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         # validated_data 기반으로, Snippet 인스턴스 생성
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # validated_data 기반으로, instance를 업데이트
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance

# UsingModelSerializers 이 후 ModelSerializer 사용
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']