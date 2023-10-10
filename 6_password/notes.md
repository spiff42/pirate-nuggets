# /etc/passwd

Filen `/etc/passwd` indeholder brugerdatabasen på et UNIX eller Linux system. Hver linje i filen indeholder oplysninger for en account, bestående af 7 felter adskilt af `:`

- Brugernavn (login)
- Krypteret password
- user-id (numerisk)
- gruppe-id (numerisk)
- Full name, kommentarer (eller GECOS)
- Home directory
- Kommandofortolker/shell

(Se yderligere oplysninger i `man 5 passwd`)


## Brugernavn

Brugernavn bruges på login-prompten, men er også det, der vises af fx. ls
som ejer af en fil.

## Password

Oprindeligt stod det hashede password som felt nr. 2, men for at beskytte
systemet bedre har man indført "shadow passwords", hvor feltet i `/etc/passwd` blot indeholder `x`, og den rigtige password hash står i filen `/etc/shadow`. (Se shadow passwords nedenfor)

## User-ID

Når der oprettes almindelig bruger tildeles næste ledige user-id, normalt startende fra 1000.

Når der oprettes en systembruger tildeles normalt UID under 1000.

## Group-ID

Tildeles for almindelige brugere normalt fra 1000, og systembrugere under 1000.

Dette er brugerens "primære" gruppe. Den oprettes i `/etc/group`, og her kan der ligeledes tildeles sekundære grupper til brugere.

## Full name (GECOS)

Dette felt indeholder brugerens fulde navn (evt. kontor, telefonnummer, osv.), eller en kommentar for systembrugere.

## Home directory

Er det bibliotek, hvor shellen starter efter brugeren er logget ind.

## Shell

Den kommandofortolker/shell/skal brugeren benytter. Fx `/bin/bash` eller `/bin/zsh`.
Skal fremgå i `/etc/shells`



# Shadow passwords

Alle brugere kan læse `/etc/passwd`, men ikke `/etc/shadow`.

```
ls -la /etc/{passwd,shadow}
-rw-r--r-- 1 root root   2948 Oct 10 15:25 /etc/passwd
-rw-r----- 1 root shadow 1562 Oct 10 15:23 /etc/shadow
```


Programmer der skal tilgå shadow-filen må derfor være suid (set-uid):
```
ls -la /usr/bin/{passwd,su}
-rwsr-xr-x 1 root root 59976 Nov 24  2022 /usr/bin/passwd
-rwsr-xr-x 1 root root 55672 Feb 21  2022 /usr/bin/su
```

Shadow-filen indeholder 9 felter:

- første felt er brugernavnet (som `/etc/passwd`)
- andet felt er password hash
- resterende felter styrer hvornår password kan/skal skiftes, udløber, osv.

## Password hash

Hvis password hash feltet er `*` kan brugeren ikke logge ind med password.

Hvis password hash feltet starter med `!` er password midlertidigt lukket.

Password er hashet med et salt. Hvorfor bruger vi salt?

Der findes forskellige hashes, der kan benyttes.

Eksempel på linje fra `/etc/shadow`:

```
test:$y$j9T$M2gCowZVGLmsSGP2GGnKo.$Fv2ER4kISNDaIjFrGdtLN.JlVpuKKI.3RTZSDHGfhtA:19640:0:99999:7:::
```

Password hash består af 4 dele:

- Første del (`$y`) angiver yes-crypt hashen (se også `man 5 crypt`)
- Anden del (`$j9t`) sætter parametre (CPU, memory krav)
- Tredie del (`$M2gCowZVGLmsSGP2GGnKo.`) er salt
- Sidste del er password hash.

# Demo

```
su - test
```


