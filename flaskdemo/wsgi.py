# """
# WSGI config for reportMailer project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
# """

import os,sys,site

# #from django.core.wsgi import get_wsgi_application
site.addsitedir('/home/ubuntu/flsk/lib/python2.7/site-packages')
#sys.path.append('/home/ubuntu/flsk/flaskdemo/')
sys.path.append('/home/ubuntu++/flaskdemo/')
activate_env=os.path.expanduser("/home/ubuntu/flsk/bin/activate_this.py")
execfile(activate_env,dict(__file__=activate_env))
# #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reportMailer.settings")
#os.environ["DJANGO_SETTINGS_MODULE"]= "reportMailer.settings"

# #import django.core.handlers.wsgi
# #application=django.core.handlers.wsgi.WSGIHandler()
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()
sys.path.append('/home/ubuntu/flaskdemo')
from flaskdemo import app as application

"""
WSGI config for angtest project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

#import os

#from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reportMailer.settings")

#application = get_wsgi_application()
