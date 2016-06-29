from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length = 150)
    content = models.TextField()
    timestamp =models.DateField()

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','content','timestamp') 
    

class TBook(models.Model):
    bookid = models.IntegerField(db_column='BOOKID', primary_key=True)  # Field name made lowercase.
    bookname = models.CharField(db_column='BOOKNAME', max_length=50)  # Field name made lowercase.
    qty = models.IntegerField(db_column='QTY')  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=50)  # Field name made lowercase.
    press = models.CharField(db_column='PRESS', max_length=50)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=5)  # Field name made lowercase.
    createdate = models.DateField(db_column='CREATEDATE')  # Field name made lowercase.
    creater = models.CharField(db_column='CREATER', max_length=50)  # Field name made lowercase.
    changedate = models.DateField(db_column='CHANGEDATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    changer = models.CharField(db_column='CHANGER', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_book'


class TUser(models.Model):
    userid = models.IntegerField(db_column='USERID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=50)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=5)  # Field name made lowercase.
    createdate = models.DateField(db_column='CREATEDATE')  # Field name made lowercase.
    creater = models.CharField(db_column='CREATER', max_length=50)  # Field name made lowercase.
    changetime = models.DateField(db_column='CHANGETIME', blank=True, null=True)  # Field name made lowercase.
    changer = models.CharField(db_column='CHANGER', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_user'
        
        
class TLoaninfo(models.Model):
    loanid = models.IntegerField(db_column='LOANID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    bookid = models.IntegerField(db_column='BOOKID')  # Field name made lowercase.
    fromdate = models.DateField(db_column='FROMDATE')  # Field name made lowercase.
    todate = models.DateField(db_column='TODATE')  # Field name made lowercase.
    realdate = models.DateField(db_column='REALDATE', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=5)  # Field name made lowercase.
    cretetime = models.DateField(db_column='CRETETIME', max_length=50)  # Field name made lowercase.
    creater = models.CharField(db_column='CREATER', max_length=50)  # Field name made lowercase.
    changedate = models.DateField(db_column='CHANGEDATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    changer = models.CharField(db_column='CHANGER', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_loaninfo'

admin.site.register(BlogPost, BlogPostAdmin)   