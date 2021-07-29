# 21.07.30
# Snippet의 View에 접근할 수 있게 URL 설정

from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk/', views.snippet_detail),
]