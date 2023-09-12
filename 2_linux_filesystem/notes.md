# Linux file system

- Case sensitive
- Ingen drevbogstaver, logisk filsystem
- Root filsystem (ikke root-bruger)
- Andre filsystemer mountes på et katalog/bibliotek/directory 
(skjuler midlertidigt filer der måtte findes i biblioteket).

Eksempel:
```
ls -la /mnt/eksempel
sudo mount -t tmpfs -o size=32M,user none /mnt/eksempel
touch /mnt/eksempel/fil_paa_ramdisk
ls -la /mnt/eksempel
sudo umount /mnt/eksempel
ls -la /mnt/eksempel
```

## Forskellige kataloger

`/` : root filesystem (rod-filsystem)

`/etc` : Konfigurationsfiler

`/home` : Home-directories (hjemmekataloger)

`/root` : Home-directory for root-brugeren

`/mnt` : Midlertidigt mount-point (eller mount-points, fx /mnt/floppy, /mnt/tmp)

`/media` : Automatiske mount points for CD, DVD, USB

`/bin` : Basale systemværktøjer (/bin/sh, /bin/ls, etc.) Tilgængelige inden /usr er mountet.

`/sbin` : Systemværktøjer (mange kræver root)

`/lib` : Libraries tilgængelige inden /usr er mountet.

`/usr` : /usr/bin, /usr/sbin, /usr/lib

`/usr/local` : Programmer og filer installeret uden package-manager (bin, etc, lib, doc)

`/var` : Filer, der ændrer sig over tid, fx logfiler (/var/log), mailkø (/var/mail), mv.

`/tmp` og `/var/tmp` : Midlertidige filer, der kan slettes af systemet, fx ved opstart eller efter et givent stykke tid.

---

`/dev` : Specielle filer der giver adgang til hardwareenheder (harddisk, lydkort, osv.)

`/proc` : Interface til kernens liste over kørende processer

`/sys` : Interface til kernens representation af hardware


## Hjemmekatalog (home directory)

Alle brugere har et hjemmekatalog, defineret af det 6. felt i /etc/password (brugerdatabasen).

- For almindelige brugere er det normalt under /home, fx. /home/pirat for brugeren med brugernavnet pirat.
- For superbrugeren (root) er hjemmekatalogeget normalt /root, som findes på root-filsystemet (`/`), og derfor er tilgængeligt inden /home er mountet.

## Kommandoer

- `pwd` : Print Working Directory
- `cd` : Change Directory
- `ls` : LiSt files

---

- Kommandoen `cd` uden argumenter tager dig tilbage til dit hjemmekatalog
- Kommandoen `cd ..` tager dig et niveau op i hierakiet.
- Kommandoen `cd sti` tager dig til `sti`, som kan være en absolut eller relativ sti.

En absolut sti starter med `/`. Relative stier er i forhold til nuværende arbejdskatalog (pwd).

Shell'en kan expande `~` til den absolutte sti til en brugers hjemmekatalog.
`~` alene ekspanderer til den aktuelle brugers hjemmekatalog, `~bruger` 
ekspanderer til bruger's hjemmekatalog:
- `cat ~/.ssh/known_hosts` 
- `ls ~` expanderer til den aktuelle brugers hjemmekatalog
- `cd ~` er det samme som `cd` uden argumenter
- `ls ~bob` viser brugeren bobs hjemmekatalog

## Skjulte filer

Filer der starter med `.` vises ikke normalt af ls. Disse kaldes normalt
dot-files.

NB: ls viser heller ikke `.` og `..` medmindre man bruger `-a`.

Nogle programmer har brugerspecifikke konfigurationsfiler. Disse gemmes
normalt i en dot-file i brugerens hjemmekatalog (fx `/home/pirat/.bashrc`).
Hvis der er flere separate konfigurationsfiler til det samme program bruges
et skjult katalog (hvor navnet starter med `.`, som fx `/home/pirat/.ssh/`.


