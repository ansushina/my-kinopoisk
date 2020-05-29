from django.views.generic import FormView

from coureser.common.paginator import paginate
from coureser.forms.SearchForm import SearchForm
from coureser.models.Film import Film


class SearchView(FormView):
    template_name = 'search.html'
    form_class = SearchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        querydict = self.request.GET
        films = Film.objects.search_with_filters(querydict)
        films, p = paginate(films, self.request, 20)
        context['films'] = films
        context['form'] = self.form_class(querydict)
        return context