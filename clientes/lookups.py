from ajax_select import register, LookupChannel
from .models import Cliente, Endereço


@register('endereco')
class NomeClienteLookup(LookupChannel):

    model = Endereço

    def get_query(self, q, request):
        return self.model.objects.filter(rua__icontains=q).order_by('rua')[:50]

    def format_item_display(self, item):
        return u"<span class='nome'>%s</span>" % item.rua