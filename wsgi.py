import os

from rivr.wsgi import WSGIHandler
import settings

view = settings.VIEW

template_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')
if settings.TEMPLATE_ENGINE == 'rivr':
    from rivr import TemplateMiddleware
    view = TemplateMiddleware(template_dir, view)
elif settings.TEMPLATE_ENGINE == 'jinja2':
    from rivr.jinja import JinjaMiddleware
    view = JinjaMiddleware(template_dir, view)

app = WSGIHandler(view)

if __name__ == '__main__':
    from rivr import serve
    serve(view)
