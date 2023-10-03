# TCP

Hvad er TCP

- TCP - Transmission Control Protocol
- Vigtig protokol indenfor internettet (IP - Internet Protocol)
- Giver pålidelig, ordered og fejlkontrol over internettet
- Værktøj som giver os muligheden for at bygge pålidelige netværksapplikationer

## Problemet det løser

- Hvordan snakker computere med hinanden?
- Vi vil være sikre på at den anden computer modtager vores pakker
  - I rigtig rækkefølge
  - Med fejlkontrol

## Hvad er TCP?

- TCP er en protokol
- Protokol er en regelsæt for hvordan vi kommunikerer
- Overordnet - vi bruger typisk TCP når vi vil sende data over internettet

## Protokollen

Computer A vil gerne sende "Hello World" til computer B

Computer A er client - Computer B er server

Her er en tabel over hvordan det foregår hvor hver række er en pakke

| Computer A | Computer B | Beskrivelse |
| ---------- | ---------- | ----------- |
| SYN        |            | SYN (synchronize) - A vil gerne snakke med B |
|            | SYN, ACK   | SYN-ACK - B siger ja tak til at snakke med A |
| SYN, ACK   |            | A siger ja tak til at snakke med B |
|            | ACK        | ACK - B siger ja tak til at snakke med A |
| DATA       |            | A sender data til B |
|            | DATA       | B siger ja tak til at snakke med A |
| FIN        |            | A siger at den er færdig med at snakke med B |
|            | FIN        | B siger at den er færdig med at snakke med A |
| FIN, ACK   |            | A siger at den er færdig med at snakke med B |
|            | FIN, ACK   | B siger at den er færdig med at snakke med A |

## Hvad er en pakke?

Hver besked - om det er data, eller en protokol besked - er en pakke.

Pakkens indhold er opdelt i 3 dele

- Header
- Payload
- Trailer

### Header

Headeren indeholder information om pakken

- Hvor stor er pakken
- Hvor skal pakken hen
- Hvor kommer pakken fra

### Payload

Payload er selve beskeden

### Trailer

Markerer slutningen på pakken

- Indeholder typisk en checksum
  - En checksum er en måde at tjekke om pakken er korrekt
  - Hvis checksummen ikke stemmer overens med pakken, så er der sket en fejl
  - Så kan vi sende pakken igen ved at sende en NAK (Negative Acknowledgement)

## Hvordan forbinder vi til en server?

Vi kan bruge et værktøj såsom `netcat` til at forbinde til en server

```bash
nc 127.0.0.1 1234
```

Åbner en rå TCP forbindelse til `127.0.0.1` på port `1234`
