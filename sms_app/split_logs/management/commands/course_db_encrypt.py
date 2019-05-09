import os
import datetime
import logging
import pathlib

from django.conf import settings
from django.db import connections
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from split_logs.models import Course, CourseDump, Organisation
from split_logs.models import ACTIVE, NOT_ACTIVE, YES, NO

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Course DB encrypt files'

    def add_arguments(self, parser):
        parser.add_argument('--limit', type=int, default=3)

    def handle(self, *args, **options):
        limit = options['limit']
        cnt = 0
        files = CourseDump.objects.filter(is_encypted=NO)
        for cd in files:
            print(cd)
