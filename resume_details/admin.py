from django.contrib import admin
from .models import BasicDetails, Skills, Experiance, Extra, Project, Education, Certification

# Register your models here.

admin.site.register(BasicDetails)
admin.site.register(Skills)
admin.site.register(Experiance)
admin.site.register(Extra)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Certification)

