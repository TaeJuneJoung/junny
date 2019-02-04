from django.contrib import admin

from .models import Junny
# Register your models here.

class JunnyModelAdmin(admin.ModelAdmin):
    readonly_fields = ('access_time',)#변수명을 저렇게 정해줘야함
    #readonly_fields 수정을 할수없는 변수명에 대해서는 저렇게 사용하기로 함

admin.site.register(Junny, JunnyModelAdmin)
