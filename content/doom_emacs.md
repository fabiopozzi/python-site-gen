title: Doom Emacs
date: 17-09-2020
slug: doom-emacs
category: emacs
image_url: doom-emacs.jpg
summary: Ormai da qualche mese ho iniziato ad usare <a href="https://github.com/hlissner/doom-emacs">Doom Emacs</a>, un framework di configurazione per l&#8217;editor <a href="https://www.gnu.org/software/emacs/">GNU Emacs</a>

Ormai da qualche mese ho iniziato ad usare <a href="https://github.com/hlissner/doom-emacs">Doom Emacs</a>, un framework di configurazione per <a href="https://www.gnu.org/software/emacs/">GNU Emacs</a>.

<a href="https://www.gnu.org/software/emacs/">GNU Emacs</a> è un editor di testo con una lunga storia, creato da Richard Stallman negli anni '80.

Doom Emacs rappresenta una piattaforma software che permette di gestire la configurazione dell'editor e di adattarla alle nostre esigenze.

Questo significa che vi è una configurazione di base che fornisce delle impostazioni di default moderne e che ne migliorano l'usabilità.

Inoltre è stato adottato un sistema di gestione dell'installazione pacchetti dichiarativo:
è quindi possibile specificare in un file di configurazione quali pacchetti vogliamo installare (e quale versione).

Ultima caratteristica importante: il framework si occupa di gestire l&#8217;aggiornamento delle estensioni installate e del framework stesso.

Questo significa che avremo a disposizione molte funzionalità in più rispetto all&#8217;editor base, con anche una configurazione di base ragionata e curata.

Tra i plugin disponibili quelli che uso con più soddisfazione e che valgono il tempo dedicato al setup sono:

* <strong>evil-mode</strong>: permette di usare i keybindings di <a href="https://www.vim.org">vim</a> al posto dei classici di emacs
* <strong><a href="https://orgmode.org">org-mode</a></strong>: ci permette di organizzare appunti, documenti o liste di attività di ogni genere tramite documenti in formato testuale. Difficile riassumere in poche parole quanto possa essere utile.
* <strong>magit</strong>: una interfaccia per <a href="https://git-scm.com">git</a> completa e perfettamente integrata con l'editor
* <strong><a href="https://emacs-lsp.github.io/lsp-mode/">lsp</a></strong>: permette di integrare in Emacs il <a href="https://github.com/Microsoft/language-server-protocol/">Language Server Protocol</a> fornendo quindi completamento automatico e documentazione inline per molti linguaggi di programmazione

Da vecchio utente <a href="https://www.vim.org">Vim</a> ho trovato uno strumento potente e più integrato, pur mantenendo la possibilità di editing modale che ho sempre trovato geniale.

Questo mi ha anche permesso di iniziare ad apprezzare <a href="https://orgmode.org">org-mode</a> per la gestione degli appunti e della pianificazione delle mie attività.

Anche la possibilità di separare i file aperti in "workspaces" permette di contestualizzare i file aperti: possiamo avere un workspace per ogni progetto e quindi passare facilmente da un progetto ad un altro, oppure tra un contesto d'uso ed un altro.
