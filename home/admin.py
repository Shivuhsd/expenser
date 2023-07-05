from django.contrib import admin
from . models import Expense, Code, Feedback

# Register your models here.

admin.site.register(Expense)
admin.site.register(Code)
admin.site.register(Feedback)