from django.db import models
from datetime import datetime

# Create your models here.

class Tutorials(models.Model):
    title= models.CharField(max_length=300)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    description= models.TextField()
    link= models.CharField(max_length=200)

    def __str__(self):
        ctitle= self.title.upper()
        date= self.pub_date.strftime('%b %e, %Y')
        admintitle= ctitle+' ('+date+')'
        return admintitle

    def pub_date_short(self):
        return self.pub_date.strftime('%b %e %Y')

    def embededid(self):
        pos= self.link.find('=')
        id=self.link[pos+1:]
        return id
