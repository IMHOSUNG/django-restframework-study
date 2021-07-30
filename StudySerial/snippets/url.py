# 21.07.30
# Snippet의 View에 접근할 수 있게 URL 설정

from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/api/', views.snippet_list_api),
    path('snippets/api/<int:pk>', views.snippet_detail_api)
]

urlpatterns = format_suffix_patterns(urlpatterns)