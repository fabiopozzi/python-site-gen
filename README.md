# Il mio sito personale
In questo repository sto sperimentando la creazione di un generatore di siti statici usando python che sia:
* minimalista
* adatto alle mie esigenze

Il templating delle pagine è basato su [Jinja](https://jinja.palletsprojects.com).

Il formato dei contenuti è [markdown](http://daringfireball.net/projects/markdown).

In questo modo posso disaccoppiare lo stile e la struttura dei vari elementi dai contenuti che vado a scrivere.

Mi sono affidato ad un layout ultra semplice basato su [Pure](https://purecss.io/) per creare un semplice layout a due colonne.
Per quanto riguarda la visualizzazione delle tracce GPX sto facendo uso di [LeafletJS](https://leafletjs.com) e [OpenstreetMap](https://www.openstreetmap.org) convertendo le tracce GPX in formato [GeoJSON](https://geojson.org) che viene poi visualizzato nelle pagine.
Ogni traccia e' descritta da un file JSON in cui sono inseriti alcuni metadati quali ad esempio:
- lunghezza traccia
- dislivello positivo
- dislivello negativo
- durata del giro
- nome della traccia gpx

A partire da questo file il sistema genera le pagine HTML che visualizzano queste informazioni e la traccia.

La struttura del sito sarà creata in base alla suddivisione in cartelle, ma senza categorie o concetti troppo elaborati.

Le statistiche degli accessi web sono raccolte grazie a [Goatcount](https://www.goatcounter.com) una piattatorma open source e meno invasiva degli altri servizi di analytics.

## Note

### Generazione stile code highilighting
Fatto con pygmentize
```
pygmentize -S default -f html -a .codehilite > codehighlight.css
```
