# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import loader,Context
from django.http import HttpResponse,Http404
from demo.models import TBook,TLoaninfo,TUser
from django.http import HttpResponseRedirect
import time,datetime
import random
def newBookResult(request):
    errors = []
    if 'bookname' in request.GET:
        bookname = request.GET['bookname']
    if 'author' in request.GET:
        author = request.GET['author']    
    if 'press' in request.GET:
        press = request.GET['press']    
    if 'qty' in request.GET:
        qty = request.GET['qty']
   
    if not bookname:
            errors.append('书名不能为空')
    if not author:
            errors.append('作者不能为空')
    if not press:
            errors.append('出版社不能为空')
    if not qty:
            errors.append('数量不能为空')
            
    if len(bookname) > 50:
            errors.append('书名不能超过50个字符！！')
    if len(author) > 50:
            errors.append('作者不能超过50个字符！！')
    if len(press) > 50:
            errors.append('出版社不能超过50个字符！！')
    if len(qty) > 50:
            errors.append('数量不能超过50个字符！！')
    
    if  len(errors)==0:   
        errors = '新增图书成功！'
        tempBook=TBook()
        tempBook.bookid=random.randint(2,10000) 
        tempBook.bookname= request.GET['bookname']
        tempBook.author= request.GET['author']
        tempBook.press= request.GET['press']
        tempBook.qty= request.GET['qty']
        tempBook.state=1
        tempBook.createdate=(datetime.datetime.now())
        tempBook.creater='admin'  
        tempBook.save()
        posts = tempBook.__class__.objects.all()
        t =loader.get_template('books.html')
        c =Context({'posts':posts,'errors': errors})
        return HttpResponse(t.render(c))
    else:
        posts = TBook.objects.all()
        t =loader.get_template('newBooks.html')
        c =Context({'posts':posts,'errors': errors})
        return HttpResponse(t.render(c))