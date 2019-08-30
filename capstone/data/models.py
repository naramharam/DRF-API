from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.models import AbstractUser


class Other(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    contents = models.TextField()
    location = models.CharField(max_length=50)
    sub_location = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Jaega(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    contents = models.TextField()
    location = models.CharField(max_length=50)
    sub_location = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class professional(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    contents = models.TextField()
    location = models.CharField(max_length=50)
    sub_location = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class community(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    contents = models.TextField()
    location = models.CharField(max_length=50)
    sub_location = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Facility(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    contents = models.TextField()
    location = models.CharField(max_length=50)
    sub_location = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class all(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    contents = models.TextField()
    location = models.CharField(max_length=50)
    sub_location = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class UserModel(models.Model):
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    user_id = models.EmailField()
    gender = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    sub_location = models.CharField(max_length=10)
    priority_volunteer = models.CharField(max_length=10)
    # 이름
    # 아이디
    # 성별
    # 지역
    # 시구군
    # 비밀번호
    # 선호봉사종류

#
# def save(self, *args, **kwargs):
#     lexer = get_lexer_by_name(self.language)
#     linenos = 'table' if self.linenos else False
#     options = {'title': self.title} if self.title else {}
#     formatter = HtmlFormatter(style=self.style, linenos=linenos,
#                               full=True, **options)
#     self.highlighted = highlight(self.code, lexer, formatter)
#     super(facilty, self).save(*args, **kwargs)
#     super(other, self).save(*args, **kwargs)
#     super(community, self).save(*args, **kwargs)
#     super(professional, self).save(*args, **kwargs)
#     super(jaega, self).save(*args, **kwargs)