"""
To use jinja2 change TEMPLATE_ENGINE to jinja2 and
add jinja2 to requirements.txt
"""
TEMPLATE_ENGINE='rivr'

"""
The following can be changed to a view, middleware or router.
"""
from urls import router
VIEW=router
