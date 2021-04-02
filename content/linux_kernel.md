title: Compilare il kernel linux
date: 02-04-2021
slug: kernel-build
category: linux
summary: Mettiamo di voler compilare "a mano" una versione del kernel linux per poi installarla. Vediamo come fare.

## 1: Ottenere i sorgenti del kernel 

Installiamo il pacchetto contenente i sorgenti del Linux kernel con già incluse le patch aggiunte da Debian (fix vari di bug e vulnerabilità di sicurezza).

```
$ sudo apt install linux-source-5.10
```

Questo comando dovrebbe portare anche all'installazione di alcune dipendenze che ci serviranno per poter compilare il kernel.
Verranno quindi scaricati ed installati (se non lo abbiamo già fatto) il compilatore gcc, i pacchettti binutils, make, bison, flex ed alcune librerie utili.

## Installiamo altre librerie utili

Installiamo anche le librerie ncurses, libelf e libssl (ci saranno utili più avanti) con il comando:

```
$ sudo apt install libncurses-dev libelf-dev libssl-dev
```

## Altre dipendenze necessarie

E' necessario installare anche delle utility necessarie per manipolare le informazioni di debug per generare simboli di debug e altro. Se siete su debian stable installate la versione da backports
```
$ sudo apt-get install -t buster-backports dwarves
```
                     
## Configuriamo il kernel

Troveremo i sorgenti scaricati in `/usr/src` quindi potremo decomprimerli nella directory corrente con

```
$ tar xaf /usr/src/linux-source-5.10.tar.xz
```
                     
Avremo quindi una nuova directory `linux-source-5.10` nella quale entriamo con il comando

```
$ cd linux-source-4.19
```

Definiamo una configurazione del kernel che parta da quella corrente, quindi usiamo l'opzione

```
$ make localmodconfig
```

Ci verrà chiesto se includere o ignorare nuove opzioni o il supporto a nuove periferiche che sono state aggiunte nel kernel che stiamo ricompilando (rispetto a quello che attualmente gira sul nostro PC).

Una volta risposto a queste domande (possiamo premere invio per far uso della opzione di default se non sappiamo cosa rispondere) otterremo un nuovo file `.config` che rappresenta la nostra nuova configurazione.

Ora possiamo visualizzare e modificare la configurazione del kernel che abbiamo definito con

```
$ make nconfig
```

A questo punto volendo possiamo rimuovere il supporto ad hardware che non possediamo, etc etc.

Faremo uso di F2 per ottenere più informazioni su una determinata opzione, mentre useremo F5 per risalire di un livello nel menù.

Quando abbiamo finito premiamo F6 per salvare la nuova configurazione (possiamo sovrascrivere la precedente o assegnare un nuovo nome) e poi usciamo con F9.

## Compiliamo e installiamo il kernel

Per compilare usiamo il comando

```
$ make deb-pkg
```

Alla fine del processo nella cartella superiore a questa dei sorgenti otterremo dei file <code>.deb</code>.
Se installiamo il kernel con

```
$ dpkg -i ../linux-4.19.118_4.19.118-1_amd64.deb
```

Al prossimo avvio del sistema potremo fare il boot con il nostro kernel compilato "a mano"!
