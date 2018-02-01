from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self,  **kwargs):
        context = super(IndexView, self).get_context_data()
        return context


