# Shell navigation

Stier:
- Absolutte (starter med `/`)
- Relative (i forhold til PWD)
    - Kan vises explicit ved at starte med `./`
    - Kan referere højere op i hierakiet med `../`
- Shell kan expande `~` til brugerens homedir eller `~user` til users homedir (en absolut sti)

## Nyttige kommandoer

- `cd` - change directory (uden argumenter kommer man tilbage til ens homedir)
- `pwd` - print working directory
- `mkdir` - opret mappe/katalog/directory
- `rmdir` - fjern (tom) mappe
- `cp` - copy; kopier fil
- `mv` - move; flyt eller omdøb fil/mappe
- `chmod` - change mode; ændrer fil-rettigheder (permissions)

Nogle kommandoer er "shell built-ins", men de fleste er "binaries" (binære programmer).
Hvis en kommando skrives uden en sti ledes efter filer med execute-permissions i alle
biblioteker nævnt i `$PATH`-variablen. NOTE: Normalt er `.` _ikke_ med i PATH.
Kommandoen `which` fortæller hvor en given executable binary findes (i PATH).

## Man pages

Kan være lidt svære at forstå:
https://manpages.opensuse.org/Tumbleweed/coreutils-doc/index.html

Danske oversættelser er ikke nødvendigvis meget bedre:
https://manpages.opensuse.org/Tumbleweed/man-pages-da/index.html

## Øvelser

1. Opret en mappe under dit homedir, der hedder `test mappe`
1. Skift ind i mappen
1. Opret en mappe her, der hedder `level2`, og skift ind i den
1. Lav en fil, der hedder `test`, med følgende indhold:
    ```
    #!/bin/sh
    D=$(date '+%T')
    echo Klokken er $D ${PWD} $0
    ```
1. Prøv at køre scriptet (gotcha: der er også et program, der hedder test)
1. Tildel execute-permissions til scriptet
1. Kør scriptet
1. Kør scriptet igen, men omdirrigér (redirect) output til filen `testfil.txt` under `test mappe`
1. Opret en ny mappe `next level` under `test mappe`
1. Flyt scriptet fra `level2` til `next level` og omdøb det til `klokken_er.sh`
1. Gå ind i `test mappe/level2` og kør scriptet derfra
1. Kør scriptet igen, med output omdirrigeret til filen `test.txt` (i `level2`)
