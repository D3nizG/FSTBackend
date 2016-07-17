from django.contrib import admin
from fstmobile.models import Contact
from fstmobile.models import FAQ
from fstmobile.models import News
from fstmobile.models import Scholarship

# Register your models here.
admin.site.register(Contact)
admin.site.register(FAQ)
admin.site.register(News)
admin.site.register(Scholarship)
