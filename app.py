"""
import sys

def application(environ, start_response):
    status = '200 OK'
    output = '\n'.join(['Hello World!', f"Version : {sys.version}",
                        f"Executable : {sys.executable}"])

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
"""

"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

this_file = "venv/bin/activate_this.py"
exec(open(this_file).read(), {'__file__': this_file})

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
