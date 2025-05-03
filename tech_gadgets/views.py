from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
import json     # pythonspezifischer Import
from django.utils.text import slugify   # aus jedem String wird ein Slug gemacht
from django.urls import reverse # gibt die URL zurück, zu der wir redirecten wollen
from django.views import View

from .dummy_data import gadgets     # importiert die Variable gadgets aus der Datei dummy_data aus dem aktuellen Verzeichnis .

from django.views.generic.base import RedirectView


# Create your views here.
def start_page_view(request):
    # return HttpResponse("Hey das hat doch gut funktioniert!")
    # return render(request, 'tech_gadgets/test_static.html')

    # Key wird an HTML-Template übergeben für For-Loop, Value ist die Variable
    return render(request, 'tech_gadgets/test.html', {'gadget_list': gadgets})


class RedirectToGadgetView(RedirectView):
    pattern_name = "gadget_slug_url"

    def get_redirect_url(self, *args, **kwargs):
        print("Hello")
        slug = slugify(gadgets[kwargs.get("gadget_id",3)]["name"])   # gadget_id muss aus den kwargs gezogen werden, Standard-ID=3
        # new_kwargs = {"gadget_slug": "ultraportable-laptop-z"}  # kwargs = key word arguments
        new_kwargs = {"gadget_slug": slug}
        return super().get_redirect_url(*args, **new_kwargs)




def single_gadget_int_view(request, gadget_id):
    # return HttpResponse(json.dumps(gadgets[0]), content_type="application/json")   # wandelt die Daten in JSON-Format um
    # return JsonResponse(gadgets[0])   # Umwandlung in JSON von Django
    # return JsonResponse({"test:": True})  # gibt JSON aus
    # return JsonResponse({"test:": gadget_id}) # für die Ausgabe der übergebenen ID
    # return JsonResponse(gadgets[gadget_id])

    if len(gadgets) > gadget_id:
        # der Value zum Key "Name" an der Stelle gadget_id wird zugewiesen und die Leerzeichen zu "-" gemacht (slugify)
        new_slug = slugify(gadgets[gadget_id]["name"])  
        # durch name="gadget_slug_url" wird auf die urlpattern zugegriffen, dort ist als view single_gadget_slug_view zugeordnet
        new_url = reverse("gadget_slug_url", args=[new_slug])
        # dann wird zu der URL umgeleitet, d.h. wenn eine 1 eingegeben wird, dann wird die URL durch den Namen an Stelle 1 im Array ausgetauscht
        return redirect(new_url)
        # return JsonResponse({"result": slugify(gadgets[gadget_id]['name'])})    # gibt den Value des Key 'name' an der Stelle 'gadget_id' aus
        # value = slugify(gadgets[gadget_slug]['name']) # slugify macht aus Leerzeichen in den Values ein '-', dadurch gibt es in URLs kein %20%
        # return HttpResponse(value)
    return HttpResponseNotFound("not found by me")  # falls der Index nicht gefunden wurde
    

# Beispiel smartthermostat-pro
def single_gadget_slug_view(request, gadget_slug):
    # gadget_match = {"result": "nothing"}    # Fallback-Wert falls nichts gefunden wird
    gadget_match = None
    for gadget in gadgets:  # geht das JSON-Array durch
        if slugify(gadget['name']) == gadget_slug:  # wenn der ge(slugify)te Name dem Wert in der URL entspricht
            gadget_match = gadget   # dann wird das JSON der Variablen zugewiesen

    if gadget_match:
        return JsonResponse(gadget_match)
    raise Http404()


def single_gadget_post_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"received data: {data}")
            return JsonResponse({"response": "Das war was."})
        except:
            return JsonResponse({"response": "Das war wohl nix."})
        



# GET und POST zusammengefasst in einer View
def single_gadget_view(request, gadget_slug=""):

    if request.method == "GET":
        gadget_match = None
        for gadget in gadgets:  # geht das JSON-Array durch
            if slugify(gadget['name']) == gadget_slug:  # wenn der ge(slugify)te Name dem Wert in der URL entspricht
                gadget_match = gadget   # dann wird das JSON der Variablen zugewiesen

        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404()
    

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"received data: {data}")
            return JsonResponse({"response": "Das war was."})
        except:
            return JsonResponse({"response": "Das war wohl nix."})
        



class GadgetView(View): # erbt von der Klasse View
    # vermeidet die Notwendigkeit einer IF-Abfrage, gadget_slug muss noch übergeben werden, self ist notwendig, weil es Funktion innerhalb einer Klasse ist
    def get(self, request, gadget_slug):     
        gadget_match = None
        for gadget in gadgets:  # geht das JSON-Array durch
            if slugify(gadget['name']) == gadget_slug:  # wenn der ge(slugify)te Name dem Wert in der URL entspricht
                gadget_match = gadget   # dann wird das JSON der Variablen zugewiesen

        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404()
    
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print(f"received data: {data}")
            return JsonResponse({"response": "Das war was."})
        except:
            return JsonResponse({"response": "Das war wohl nix."})
        