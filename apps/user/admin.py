from django.contrib import admin

from apps.user.models import User, VerifyEmail


admin.site.register(User)
admin.site.register(VerifyEmail)
