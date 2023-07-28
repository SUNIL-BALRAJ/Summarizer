# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from .models import team
admin.site.register(team)

# from .models import UploadFile
# admin.site.register(UploadFile)

from .models import buy_energy
admin.site.register(buy_energy)


from .models import meter_analytics
admin.site.register(meter_analytics)

from .models import summary_file
admin.site.register(summary_file)

from .models import meta_video
admin.site.register(meta_video)

from .models import forum
admin.site.register(forum)

from .models import cloud
admin.site.register(cloud)