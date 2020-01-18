from django.contrib import admin
from .models import Gamesblog

# Register your models here.

class GamesblogAdmin(admin.ModelAdmin):
    list_display = ('TITLE', 'Published', 'views')
    list_filter = ('pub_date',)
    search_fields = ('title','description')

    def Published(self,obj):
        pub = obj.pub_date_short
        return obj.pub_date.strftime('%b %e %Y')

    def TITLE(self, obj):
        ctitle = obj.title.upper()
        return ctitle

admin.site.register(Gamesblog, GamesblogAdmin)
