# 21.07.29
# Snippet에 대한 DB TABLE 모델 정의 
 
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# (21.07.29) 어떤 내용인지 공부는 필요 
# 간결한 코드 작성 법 참고 필요 
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item,item) for item in get_all_styles()])

class Snippet(models.Model):
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']

