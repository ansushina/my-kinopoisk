from coureser.common.paginator import paginate
from coureser.forms.SearchForm import SearchForm
from coureser.models.Film import Film
from django.http import QueryDict
from django.views.generic import FormView


class SearchView(FormView):
    template_name = 'search.html'
    form_class = SearchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        films = Film.objects.search_with_filters(self.request.GET)
        films, p = paginate(films, self.request, 20)
        params = QueryDict(query_string=self.request.GET.urlencode(), mutable=True)
        if params.__contains__('page'):
            params.pop('page')
        if films.has_previous():
            films.previous_page_link = str(films.previous_page_number()) + '&' + params.urlencode()
        if films.has_next():
            films.next_page_link = str(films.next_page_number()) + '&' + params.urlencode()

        context['form'] = self.form_class(self.request.GET)
        context['films'] = films
        return context
