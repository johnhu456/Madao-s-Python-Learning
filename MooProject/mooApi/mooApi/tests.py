from django.conf import settings
settings.configure()
import sys
import os
import django
django.setup()
from Spyder import actressSpyder


def startTest():
    django.setup()
    reload(sys)
    sys.setdefaultencoding('utf-8')
    actressSpyder.getActrssList()


# Create your tests here.
