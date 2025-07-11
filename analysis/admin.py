from django.contrib import admin

from analysis.models import person
from analysis.models import faq
from analysis.models import latest_news
from analysis.models import blogs
from analysis.models import tutorials
from analysis.models import experts
from analysis.models import myreview
from analysis.models import contact_us
from analysis.models import userregister
from analysis.models import helpsupport







# Register your models here.

admin.site.register(person)
admin.site.register(faq)
admin.site.register(latest_news)
admin.site.register(blogs)
admin.site.register(tutorials)
admin.site.register(experts)
admin.site.register(myreview)
admin.site.register(contact_us)
admin.site.register(userregister)
admin.site.register(helpsupport)





