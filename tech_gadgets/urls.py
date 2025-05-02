from django.urls import path
# .view bedeutet, dass man im aktuellen Ordner guckt
from .views import start_page_view, single_gadget_int_view, single_gadget_slug_view, single_gadget_post_view, single_gadget_view, GadgetView, RedirectToGadgetView


# Reihenfolge ist wichtig
urlpatterns = [
    # path('', start_page_view),
    path('', RedirectToGadgetView.as_view()),
    path('<int:gadget_id>', RedirectToGadgetView.as_view()),    # vorher slugify und dann Weiterleitung zur URL
    # path('gadget/', single_gadget_view),
    path('gadget/', GadgetView.as_view()),
    # path('gadget/', single_gadget_post_view), # wird zusammengefasst mit GET und POST
    # path('gadget/<str:gadget_id>', single_gadget_view),   # Type darf kein String sein, außer er kann in int umgewandelt werden
    path('gadget/<int:gadget_id>', single_gadget_int_view),  # Type muss definiert werden, da sonst Error "list indices must be integers or slices, not str"
    # path('gadget/<slug:gadget_slug>', single_gadget_slug_view, name="gadget_slug_url"), # wird zusammengefasst mit GET und POST
    # path('gadget/send_gadget/', single_gadget_post_view)  # testet das Senden von Daten in der Konsole
    path('gadget/<slug:gadget_slug>', GadgetView.as_view(), name="gadget_slug_url")
]