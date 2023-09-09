from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .clubinfo import ClubInfoModelAdmin
from .group import SectionGroupModelAdmin
from .lesson import LessonModelAdmin
from .partner import PartnerModelAdmin
from .personal import PersonalModelAdmin
from .post import PostModelAdmin
from .section import SectionModelAdmin
from .job import JobModelAdmin

admin.site.register(LogEntry)
