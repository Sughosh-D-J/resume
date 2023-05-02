from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class BasicDetails(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone = models.IntegerField()
    email1 = models.EmailField()
    email2 = models.EmailField(default='',null=True,blank=True)
    linkedin = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    photo = models.ImageField(null=False,blank=False)
    resume = models.FileField(blank=True,null=True,upload_to='media',default='')


    def __str__(self) -> str:
        return self.name
    
    def get_image(self):
        if self.photo:
            return 'https://resume-384810.uc.r.appspot.com'+self.photo.url
        return ''
    
    def get_resume(self):
        if self.resume:
            return 'https://resume-384810.uc.r.appspot.com'+self.resume.url
        
        return ''

class Skills(models.Model):
    name = models.CharField(max_length=500)
    photo = models.ImageField(null=True,blank=True)
    details = models.CharField(max_length=100,default='',null=True,blank=True)
    rate = models.IntegerField(blank=True,null=True,default=0)
    
    def __str__(self) -> str:
        return self.name
    
    def get_image(self):
        if self.photo:
            return 'https://resume-384810.uc.r.appspot.com'+self.photo.url
        return ''
    

class Experiance(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100,default='')
    details = models.CharField(max_length=500)
    joining_date = models.DateField(blank=True, null=True)
    leaving_date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.company

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(blank=True,null=True)
    link1 = models.CharField(max_length=100,default='', blank=True, null=True)
    link2 = models.CharField(max_length=100,default='',blank=True, null=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name
    
    def get_image(self):
        if self.image:
            return 'https://resume-384810.uc.r.appspot.com'+self.image.url
        return ''
    
    def return_url(self):
        if self.link1:
            return self.link1
        
        if self.link2:
            return self.link2
    
    
class Extra(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    


class Education(models.Model):
    name_of_college = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    course = models.CharField(max_length=100,default='')
    year_of_joining = models.DateField(blank=True, null=True)
    year_of_passing = models.DateField(blank=True, null=True)
    cgpa = models.DecimalField(max_digits=10,decimal_places=1,null=True,blank=True)
    university = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.degree


class Certification(models.Model):
    name = models.CharField(max_length=100)
    provider = models.CharField(max_length=100)
    duration = models.CharField(max_length=100,default='',null=True,blank=True)
    certificate_id = models.CharField(max_length=100,default='',null=True,blank=True)
    details = models.CharField(max_length=250,null=True,blank=True)
    link1 = models.CharField(max_length=100,null=True,blank=True)
    link2 = models.CharField(max_length=100,null=True,blank=True)


    def __str__(self) -> str:
        return self.name

