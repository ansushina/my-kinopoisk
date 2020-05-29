from django.views.generic import TemplateView

from coureser.models.Film import Film


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_films'] = Film.objects.new_top()
        context['most_commented'] = Film.objects.most_commented()
        context['most_rating'] = Film.objects.most_rating()
        return context