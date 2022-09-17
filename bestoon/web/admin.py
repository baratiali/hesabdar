from django.contrib import admin # import admin
from .models import Expense # import Expense model from models.py
from .models import Income # import Income model from models.py
# Register your models here.
admin.site.register(Expense) # Register Expense model in admin panel
admin.site.register(Income) # Register Income model in admin panel