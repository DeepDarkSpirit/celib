# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import loader,Context
from django.http import HttpResponse,Http404
from demo.models import BlogPost,TBook,TLoaninfo,TUser
from django.http import HttpResponseRedirect
import time,datetime
import random
def loanResult(request):
    errors = []
    if 'bookid' in request.GET:
        bookid = request.GET['bookid']
    if 'userid' in request.GET:
        userid = request.GET['userid']   
    if 'fromdate' in request.GET:
        fromdate = request.GET['fromdate']    
    if 'todate' in request.GET:
        todate = request.GET['todate']
    if 'remark' in request.GET:
        remark = request.GET['remark']   
    if not bookid:
            errors.append('请选择借阅书编号')
    if bookid == 'standard':
            errors.append('请选择借阅书编号 ')
    if not userid:
            errors.append('请选择借阅人编号')
    if userid == 'standard':
            errors.append('请选择借阅人编号 ')
    if not fromdate:
            errors.append('请选择借阅登记时间')
    if fromdate == '':
            errors.append('请选择借阅登记时间')
    if not todate:
        errors.append('请选择预计归还时间') 
    if todate == '':
            errors.append('请选择预计归还时间')
    if len(remark) > 200:
            errors.append('备注不能超过200个字符！')
    if  len(errors)==0:        
        tempLoaninfo=TLoaninfo()
        tempLoaninfo.userid= request.GET['userid']
        tempLoaninfo.bookid= request.GET['bookid']
        tempLoaninfo.remark= request.GET['remark']
        begin = request.GET['fromdate']
        end = request.GET['todate']
        tempLoaninfo.fromdate= (datetime.datetime.strptime(begin , '%Y-%m-%d')).date()
        tempLoaninfo.todate= (datetime.datetime.strptime(end , '%Y-%m-%d')).date()    
        tempLoaninfo.cretetime=(datetime.datetime.now())
        tempLoaninfo.creater='admin'
        tempLoaninfo.loanid=random.randint(2,1000)
        tempLoaninfo.save()
    posts = TLoaninfo.objects.all()
    userposts = TUser.objects.all()
    bookposts = TBook.objects.all()        
    return render_to_response('loans.html',{'errors':errors,'posts':posts,'userposts':userposts,'bookposts':bookposts})
