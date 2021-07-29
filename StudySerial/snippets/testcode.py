# python manage.py shell 에서 실행하는 python 스크립트

# 사용 방법
# manage.py 가 있는 path에서 실행 
# python manage.py shell < .\snippets\testcode.py

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print("hello, world")\n')
snippet.save()

serializer = SnippetSerializer(snippet)
serializer.data

content = JSONRenderer().render(serializer.data)
content

import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

serializer = SnippetSerializer(data=data)
serializer.is_valid()

serializer.validated_data

serializer.save()

serializer = SnippetSerializer(Snippet.objects.all(), many=True)
serializer.data