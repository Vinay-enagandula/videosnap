
from accounts.models import Language
from accounts.models import Certification
from accounts.models import Experience
from accounts.models import Skill
from accounts.models import Education
from accounts.models import Profile
from accounts.models import Award
from accounts.models import Publication
from accounts.models import Course
from accounts.models import Project
from accounts.models import Achievement

import accounts
from django.contrib import admin
from .models import *
admin .site.register(Profile)
admin .site.register(Education)
admin .site.register(Experience)
admin .site.register(Skill)
admin .site.register(Certification)
admin .site.register(Language)
admin.site.register(Award)
admin.site.register(Publication)
admin.site.register(Course)
admin.site.register(Project)
admin.site.register(Achievement)