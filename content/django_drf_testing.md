title: Testing Django Rest Framework ModelViewSet
date: 10-12-2021
slug: django-drf-testing
category: django
image_url: drf.jpg
summary: Note sul testing di ModelViewSets in <a href="https://www.django-rest-framework.org/">Django Rest Framework</a>


State lavorando ad una applicazione web in cui frontend e backend sono
disaccoppiati (Frontend con VueJS e backend con Django Rest Framework).

Avete deciso di sviluppare una parte delle API sfruttando il ModelViewSet di DRF.

Avete anche la necessità di aggiungere delle action custom al ViewSet.
Seguendo la documentazione scrivete del codice simile a questo nella vostra
`views.py`:

```python
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from app.models import Persona, Azioni
from app.api.serializers import PersonaSerializer, AzioniSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    @action(detail=True)
    def azioni(self, request, pk=None):
        qlist = Azioni.objects.filter(persona__id=pk)
        serializer = AzioniSerializer(qlist, many=True)
        return Response(serializer.data)
```
Avete infatti due modelli, Persona ed Azioni, che sono legati da una relazione
uno-a-molti.
In questo caso in pratica ogni Persona avrà molte azioni associate.

A questo punto definite le API relative a Persona in urls.py in questo modo:
```python
from django.urls import path, include
from rest_framework import routers
from app.api import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'persona', views.PersonaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```
Elegantissimo.

Lo provate e funziona.
Riuscite a raggiungere le url

+ `/api/persona` che vi mostra tutta la lista degli oggetti (List)
+ `/api/persona/1` che vi mostra le informazioni su una singola persona, dato
  il suo ID
+ `/api/persona/1/azioni` che vi mostra le azioni legate ad una particolare
  persona, dato il suo ID

Da buoni sviluppatori volete testare il tutto, o meglio, avreste dovuto
scrivere il test ancor prima del codice.

Quindi cercate come fare e vi accorgete che sull'internet non trovate nulla,
finite per cercare di capirlo direttamente dai test di <a href="https://www.django-rest-framework.org/">Django Rest Framework</a>
e finite per invocare divinità invano.

Infine, la soluzione vi raggiunge:

```python
        view = PersonaViewSet()
        router = routers.DefaultRouter(trailing_slash=False)

        view.basename = router.get_default_basename(PersonaViewSet)
        view.request = None

        detail_view = PersonaViewSet.as_view({'get': 'azioni'})

        url = view.reverse_action('azioni', args=[id_persona])
        request = self.factory.get(url)

        force_authenticate(request, user=self.user)
        response = detail_view(request, pk=self.user.pk)
        self.assertEqual(len(response.data), 2)
        [...]
```

Le prime due righe istanziano il ViewSet come classe così come una istanza del
DefaultRouter (che ci servirà per ottenere parte dell'URL del nostro endpoint).

Le successive due righe sono state prese dritte dai test di Django Rest
Framework e permettono di fare in modo che la successiva chiamata a
`reverse_action()` funzioni a dovere.

A questo punto dobbiamo ottenere una view di PersonaViewSet che permetta di
richiedere la nostra funzione custom, invece del solito `{'get': 'list'}` o
`{'get': 'detail'}` a cui siamo abituati.

Infine chiameremo `reverse_action` come da <a href="https://www.django-rest-framework.org/api-guide/viewsets/#reversing-action-urls">documentazione DRF</a>

A quel punto è fatta, chiamiate `factory.get(url)` dove `factory` in realtà è
una istanza di `APIRequestFactory()`.

Il resto vi serve nel caso le vostre API siano accessibili solo da utenti
autenticati, in quel caso dovrete forzare l'autenticazione della richiesta
facendo riferimento ad un utente che avete creato nel `setUp()` dei test.

A quel punto potete finalmente chiamare la view e controllare il risultato.
