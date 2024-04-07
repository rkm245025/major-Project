from django.contrib import admin
from . models import Branch, Program,Year,Material,News
# Register your models here.
admin.site.register(Branch)
admin.site.register(Program)
admin.site.register(Year)
admin.site.register(Material)
admin.site.register(News)