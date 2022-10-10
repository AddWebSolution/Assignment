from django.contrib import admin
from .models import (
    UserMaster,
    ProgramMaster,
    UserProgram,
)

# Register your models here.
admin.site.register(UserMaster)
admin.site.register(ProgramMaster)
admin.site.register(UserProgram)
