# 21.07.29
# API View 작성
# CSRF (크로스 사이트 요청 위조) : 사이트가 신뢰하는 사용자를 통해 공격자가 원하는 명령을 전송하는 공격

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

#TO-DO
#  HTTPS의 경우, Django RestFrameWork에서 바로 사용할 수 있는 지 확인 필요
@csrf_exempt
def snippet_list(request):
    # Snippets에 있는 모든 코드 리스트 출력, 또는 새로운 Snippets 생성
    if request.method == 'GET':
        # ORM : DB 쿼리를 쉽게 써주는 모듈
        snippets = Snippet.objects.all()
        # 다수 개가 나올 수 있으니까 many=True 셋팅
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        # 단일
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)
    # 일반적으로 Rest API에서 POST = Create , PUT = UPDATE와 매칭됨
    # POST는 요청 시 마다 새로운 리소스가 생성, PUT은 요청 시마다 생성 수정 담당하며 요청 시 마다 같은 리소스 반환
    elif request.method == 'PUT': 
        data = JSONParser().parse(request)
        # Updata의 경우는 기존 인스턴스를 미리 잡고, 거기에 Validataed_data를 넣음 
        # 기존 커스텀으로 만들었던 샘플 참고 필요 
        serializer = SnippetSerializer(snippet, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return HttpResponse(status=400)
    
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)



    