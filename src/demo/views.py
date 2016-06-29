#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import loader,Context
from django.http import HttpResponse,Http404
from demo.models import TBook,TLoaninfo,TUser
import datetime
from django.http import HttpResponseRedirect
import random
import re
# Create your views here.

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('请输入搜索关键字')
        elif len(q) > 20:
            errors.append('请不要输入超过20个字符')
        else:
            books = TBook.objects.filter(bookname__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html', 
        {'errors': errors})
def loanlist(request):
    posts = TLoaninfo.objects.all()
    userposts = TUser.objects.all()
    bookposts = TBook.objects.all()        
    return render_to_response('loanlist.html',{'posts':posts,'userposts':userposts,'bookposts':bookposts})

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))



def home(request):
    posts = TBook.objects.all()
    t =loader.get_template('home.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def newBooks(request):
    posts = TBook.objects.all()
    t =loader.get_template('newBooks.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def editBooks(request):
    tempBook=TBook
    tempBook.bookid= request.GET['bookid']
    tempBook2 = TBook.objects.get(bookid=tempBook.bookid)
    t =loader.get_template('editBooks.html')
    c =Context({'post':tempBook2})
    return HttpResponse(t.render(c))
def deleBooks(request):
    errors = '删除图书成功！'
    tempBook=TBook
    tempBook.bookid= request.GET['bookid']
    tempBook2 = TBook.objects.get(bookid=tempBook.bookid)
    tempBook2.state=0
    tempBook2.changedate=(datetime.datetime.now())
    tempBook2.changer='admin'   
    tempBook2.save()
    posts = tempBook.objects.all()
    t =loader.get_template('books.html')
    c =Context({'posts':posts,'errors': errors})
    return HttpResponse(t.render(c))

def deleUsers(request):
    errors = '删除员工成功！'
    tempUser=TUser
    tempUser.userid= request.GET['userid']
    tempUser2 = TUser.objects.get(userid=tempUser.userid)
    tempUser2.state=0
    tempUser2.changedate=(datetime.datetime.now())
    tempUser2.changer='admin'   
    tempUser2.save()
    posts = tempUser.objects.all()
    t =loader.get_template('users.html')
    c =Context({'posts':posts,'deleerror': errors})
    return HttpResponse(t.render(c))

def books(request):
    posts = TBook.objects.all()
    t =loader.get_template('books.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def returnbooks(request):
    tempReturnbook = TLoaninfo()
    tempReturnbook.loanid= request.GET['loanid']
    tempReturnbook2 = TLoaninfo.objects.get(loanid=tempReturnbook.loanid)
    tempReturnbook2.realdate=(datetime.datetime.now())   
    tempReturnbook2.save()  
    return HttpResponseRedirect('/loans/')


def loans(request):
    posts = TLoaninfo.objects.all()
    userposts = TUser.objects.all()
    bookposts = TBook.objects.all()
    t =loader.get_template('loans.html')
    c =Context({'posts':posts,'userposts':userposts,'bookposts':bookposts})
    return HttpResponse(t.render(c))

def users(request):
    posts = TUser.objects.all()
    t =loader.get_template('users.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def newUserResult(request):
    errors = []
    if 'username' in request.GET:
        username = request.GET['username']
    if 'mobile' in request.GET:
        mobile = request.GET['mobile']     
    if not username:
            errors.append('员工姓名不能为空')    
    if len(username) > 50:
            errors.append('员工姓名不能超过50个字符！！')  
    pattern=re.compile(r"^(13[0-9]{9})|(15[89][0-9]{8})$")    
    if not pattern.match(mobile):   
        errors.append('请输入正确的手机号码。')    
    if  len(errors)==0:      
        tempUser=TUser()
        tempUser.userid=random.randint(2,10000)
        tempUser.username= request.GET['username']
        tempUser.mobile= request.GET['mobile']
        tempUser.state=1
        tempUser.createdate=(datetime.datetime.now())
        tempUser.creater='admin'
        ####    
        tempUser.save()
    posts = TUser.objects.all()
    t =loader.get_template('users.html')
    c =Context({'posts':posts,'errors': errors})
    return HttpResponse(t.render(c))

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
