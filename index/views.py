from django.shortcuts import render
from django.views.generic import FormView

from index.models import Card, Expansion
from index.forms import RotationRouletteForm

from urllib.parse import urlparse
from index.utils import b64todigit

class IndexView(FormView):
    template_name = "index.html"
    form_class = RotationRouletteForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        card_ids = urlparse(form.cleaned_data['url']).path.split("/")[-1].split(".")[2:]
        card_ids = [ b64todigit(card_id) for card_id in card_ids ]
        cards_expansions = set([ card.card_set for card in Card.objects.filter(pk__in=card_ids) ])
        expansions = set(form.cleaned_data['expansions'])

        if cards_expansions > expansions:
            extra_expansions = cards_expansions - expansions
            self.info = "Extra expansions: "
            for extra_expansion in extra_expansions:
                self.info += " " + extra_expansion.name + ";"

            return self.form_invalid(form)

        return super().form_valid(form)

# Create your views here.
