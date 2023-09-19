title: Linux kernel
class: animation-fade
layout: true

.bottom-bar[
  Intro til Linux kernelen
]

---

class: impact

# {{title}}

## Introduktion

---

# Hvad er en kernel?

- Kernen af et operativsystem
- Står for at håndtere interaktionen mellem hardware og software

<center>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Kernel_Layout.svg/2560px-Kernel_Layout.svg.png" height="400">
</center>

---

# Kernelens opgaver

- Håndtere hardware
- Håndtere processer
- Håndtere hukommelse
- Håndtere filer / filsystemer
- Håndtere netværk
- Håndtere sikkerhed

---

# User space vs. kernel space

- Hukommelse er opdelt i to dele
- Kernel space: Kernen af operativsystemet
- User space: Alt andet
- Sikkerhed: User space kan ikke tilgå kernel space direkte
- Kernel space kan tilgå user space
- Kernel space har fuld kontrol over hardware
- User space har begrænset kontrol over hardware

---

# Systemkald (syscall)

- Måden hvorpå user space kan kommunikere med kernel space

```
| Systemkald | Nummer | Beskrivelse   |
|------------|--------|---------------|
| read       | 0      | Læs fra fil   |
| write      | 1      | Skriv til fil |
| open       | 2      | Åbn fil       |
| close      | 3      | Luk fil       |
| ...        | ...    | ...           |
| execve     | 59     | Kør program   |
```

---

# Hvordan kalder man et systemkald?

- Typisk gennem et "wrapper" library
- Abstraherer systemkaldet

```c
#include <unistd.h>
#include <sys/syscall.h>

void main() {
    syscall(SYS_write, 1, "Hello world!\n", 13);
}
```

--

```c
#include <stdio.h>

void main() {
    puts("Hello world!");
}
```

---

# Sikkerhed

.col-6[

- Ring 0: Kernel space
  - Har fuld kontrol over hardware
  - Kan tilgå alt
  - Kan gøre alt
  - Kører med højeste privilegier

<center>
  <img src="https://blog.codinghorror.com/content/images/uploads/2008/01/6a0120a85dcdae970b0120a86db3ea970b-pi.png" height="260">
</center>
]

.col-6[

- Ring 1-2:
  - Kører med lavere privilegier
  - Kan ikke tilgå alt
  - Typisk brugt til hardware-drivere
  - Kører i kernel space
- Ring 3: User space
  - Kan ikke tilgå kernel space direkte
  - Kan ikke tilgå hardware direkte
  - Kører med laveste privilegier
]

---

# Sårbarheder og exploits

- Kernel space er meget kompleks
- Der kan være fejl i koden til en driver
- Der kan være fejl i koden til selve kernen
- Disse fejl kan udnyttes til at få adgang til kernel space
- Dette kan bruges til at få fuld kontrol over systemet
  - Fuld kontrol over hardware og software
- Super farligt!

---

# Afslutning

## Hvad er Linux?

--

- En kernel
- Ikke et operativsystem
  - Linux distributioner er operativsystemer
