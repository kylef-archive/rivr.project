import rivr

router = rivr.Router(
    (r'^$', rivr.TemplateView.as_view(template_name='index.html'))
)
