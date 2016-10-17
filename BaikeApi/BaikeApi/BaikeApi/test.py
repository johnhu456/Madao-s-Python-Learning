import  sys

import django

from Spyder.JokesSpyder import JokesSpyder


def startTest():
    django.setup()
    reload(sys)
    sys.setdefaultencoding('utf-8')
    aSpyder = JokesSpyder()
    aSpyder.start(1)