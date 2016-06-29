from django.contrib import admin
from demo.models import  TBook,TLoaninfo,TUser
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('bookname', 'author', 'press')
    search_fields = ('bookname', 'author')
    list_filter = ('createdate',)
    date_hierarchy = 'createdate'
    ordering = ('-createdate',)

##admin.site.register(TBook)
admin.site.register(TBook, BookAdmin)
admin.site.register(TLoaninfo)
admin.site.register(TUser)
