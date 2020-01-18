from django.db import models
from datetime import datetime

class Appsblog(models.Model):
    title= models.CharField(max_length=300)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    image= models.ImageField(upload_to='images/')
    description= models.TextField(blank=True)
    features= models.TextField(blank=True)
    install_steps= models.TextField(blank=True)
    link= models.CharField(max_length=200)
    views = models.IntegerField(default=0)

    def __str__(self):
        ctitle= self.title.upper()
        date= self.pub_date.strftime('%b %e, %Y')
        admintitle= ctitle+' ('+date+')'
        return admintitle

    def summary(self):
        return self.description[:480]

    def pub_date_short(self):
        return self.pub_date.strftime('%b %e %Y')

    def category(self):
        return 'app'
