# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import loader,Context
from django.http import HttpResponse,Http404
from demo.models import TBook,TLoaninfo,TUser
from django.http import HttpResponseRedirect
import time,datetime
import random
def editBookResult(request):
    errors = []
    if 'bookname' in request.GET:
        bookname = request.GET['bookname']
    if 'bookid' in request.GET:
        bookid = request.GET['bookid']   
    if 'author' in request.GET:
        author = request.GET['author']    
    if 'press' in request.GET:
        press = request.GET['press']    
    if 'qty' in request.GET:
        qty = request.GET['qty']
   
    if not bookid:
            errors.append('图书编号不能为空')
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
        error = '修改图书信息成功！'
        tempBook=TBook
        tempBook.bookid= request.GET['bookid']
        tempBook2 = TBook.objects.get(bookid=tempBook.bookid)
        tempBook2.bookname= request.GET['bookname']   
        tempBook2.author= request.GET['author']
        tempBook2.press= request.GET['press']
        tempBook2.qty= request.GET['qty'] 
        tempBook2.state=1
        tempBook2.changedate=(datetime.datetime.now())
        tempBook2.changer='admin'   
        tempBook2.save()
        posts = tempBook.objects.all()
        t =loader.get_template('books.html')
        c =Context({'posts':posts,'errors': error})
        return HttpResponse(t.render(c))
    else:
        tempBook=TBook
        tempBook.bookid= request.GET['bookid']
        tempBook3 = TBook.objects.get(bookid=tempBook.bookid)
        t =loader.get_template('editBooks.html')
        c =Context({'post':tempBook3,'errors': errors})
        return HttpResponse(t.render(c))