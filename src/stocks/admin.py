from django.contrib import admin
from .models import *

admin.site.register(Exchange)
admin.site.register(Symbol)
admin.site.register(Stock)
admin.site.register(YFExports)
