from django.urls import path
# .view bedeutet, dass man im aktuellen Ordner guckt
from .views import start_page_view, single_gadget_view, single_gadget_slug_view, single_gadget_post_view  


# Reihenfolge ist wichtig
urlpatterns = [
    path('', start_page_view),
    # path('gadget/<str:gadget_id>', single_gadget_view),   # Type darf kein String sein, außer er kann in int umgewandelt werden
    path('gadget/<int:gadget_id>', single_gadget_view),  # Type muss definiert werden, da sonst Error "list indices must be integers or slices, not str"
    path('gadget/<slug:gadget_slug>', single_gadget_slug_view, name="gadget_slug_url"),
    path('gadget/send_gadget/', single_gadget_post_view)
]