title: Nuovo thinkpad
date: 26-03-2021
slug: nuovo-thinkpad
category: thinkpad
image_url: thinkpad.jpg
summary: In vista del mio compleanno ho deciso che era finalmente ora di regalarmi un nuovo laptop.

In vista del mio compleanno ho deciso che era finalmente ora di regalarmi un nuovo laptop.
Ho deciso di tornare ad usare linux come s.o. di tutti i giorni, dopo qualche anno passato su OSX.

La mia attenzione è caduta quindi sui nuovi <a href="https://www.lenovo.com/it/it/thinkpad">Thinkpad</a>,
in particolare già pensavo di puntare ad uno della <a href="https://www.lenovo.com/it/it/laptops/thinkpad/t-series/c/thinkpadt">Serie T</a>.

Dopo aver letto innumerevoli recensioni, comparative, valutato il supporto a linux alla fine ho deciso che il modello sarebbe stato un thinkpad T14s.

Stile classico nero thinkpad, ma sottile e leggero (peso 1.27kg), batteria da 57Wh, schermo con discreta luminosità, lo trovo è davvero bello.

A quel punto la scelta era: una classica e rassicurante versione Intel oppure osare con la nuova versione AMD?

Inutile dire che ho osato l'acquisto della versione con <a href="https://www.amd.com/en/products/apu/amd-ryzen-7-pro-4750u">AMD Ryzen 7 PRO 4750U</a>.
Stiamo parlando di una CPU a 7nm, con 8 core / 16 threads e un TDP di 15W.

Sfruttando una promozione Lenovo ho acquistato la versione con 16GB di RAM, 1TB di SSD ad un prezzo onestissimo.

Il primo passo una volta arrivato a casa è stato quello di installare GNU/linux al posto di Windows 10.

Ho deciso di tornare a <a href="https://www.debian.org/">Debian stable</a> dopo aver usato per anni <a href="https://archlinux.org/">ArchLinux</a>: sono disposto a rinunciare alle ultime feature in cambio di una distribuzione stabile, affidabile e robusta. Vedremo come andrà.

Cerco di tenere aggiornata questa pagina con tutti i dettagli dell'installazione.

Il T14s non dispone di una porta ethernet, al tempo stesso l'installer di Debian stable non supporta la scheda Intel AX200 sia perchè recente, sia perchè il firmware non è free-software.

Ho trovato questo installer <a href="https://github.com/Head-on-a-Stick/newer-buster">newer buster</a> che dovrebbe supportare tutto l'hardware ma solo dopo aver aggirato il problema.

Ho quindi rispolverato la mia buon vecchia scheda WiFi USB Alfa che è sufficientemente datata da esser riconosciuta anche dall'installer.

A quel punto l'installazione è andata piuttosto liscia.

Ho optato per una installazione su LVM cifrato: tenetevi una partizione di boot grande QUANTO la RAM disponibile o avrete problemi nel caso decideste di voler ibernare
il sistema.


