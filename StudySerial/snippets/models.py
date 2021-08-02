# 21.07.29
# Snippet에 대한 DB TABLE 모델 정의 
 
from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


# (21.07.29) 어떤 내용인지 공부는 필요 
# 간결한 코드 작성 법 참고 필요 
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item,item) for item in get_all_styles()])

class Snippet(models.Model):
    owner = models.ForeignKey('auth.User',related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']

    # save 처리하는 함수에 대해서 더 공부가 필요 
    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title' : self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                    full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

