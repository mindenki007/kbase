from django.contrib import admin
from .models import CIR, Clockwork, Changes, Updates, Queries, Answers, Defects
# Register your models here.

admin.site.register(CIR)
admin.site.register(Clockwork)
admin.site.register(Changes)
admin.site.register(Updates)
admin.site.register(Queries)
admin.site.register(Answers)
admin.site.register(Defects)
