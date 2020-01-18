from django.contrib import admin

# Register your models here.
from .models import Appsblog

class AppsblogAdmin(admin.ModelAdmin):
    list_display = ('TITLE', 'Published', 'views')
    list_filter = ('pub_date',)
    search_fields = ('title','description')

    def Published(self,obj):
        pub = obj.pub_date_short
        return obj.pub_date.strftime('%b %e %Y')

    def TITLE(self, obj):
        ctitle = obj.title.upper()
        return ctitle

admin.site.register(Appsblog, AppsblogAdmin)
