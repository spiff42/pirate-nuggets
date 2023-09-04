
# filstrømme, file streams

## hvad er en fil?

filer åbnes fra et program som en strøm (read eller write)

Programmer på Linux har 3 automatiske filstrømme; stdin, stdout, stderr

- stdin: bruges til inddata (fx. scanf, fgets)
- stdout: bruges til normale uddata (som regel printf, puts)
- stderr: bruges til fejlbeskeder fra programmet.

## hello world

se 1_hello_world.c

compile:
```
gcc -Wall --static 1_hello_world.c -o hello

./hello

strace ./hello
```

0=stdin, 1=stdout, 2=stderr

Omdirigering til fil:
   >  opretter/overskriver fil (stdout)
   2>  opretter/overskriver fil (stderr)
   >> tilføjer/append (stdout)

NOTE: strace skriver til stderr.

```
strace ./hello >/dev/null
strace ./hello 2>/dev/null
```

Nogle programmer opfører sig forskelligt hvis output omdirrigeres.

```
ls
ls > filer.txt
cat filer.txt
```

hvad gør cat-programmet?

```
man cat
```

## pipes

Pipes `|` bruges til at sende stdout fra et program som inddata til et andet
program.

eksempel:
```
ls | cat
```

andre filter-programmer:

- grep
- sort
- uniq
- tac
- sed

Eller skriv dine egne i awk, perl eller andet.

Eksempel på pipelining:

```
cat /etc/passwd | cut -d: -f7 | sort | uniq -c
```

## buffering
stdout er linjebuffered ved output til terminal, stor buffer ved omdirrigering

```
./2_print_delay.py
./3_print_delay.py
./4_print_delay.py
./2_print_delay.py | cat
```

stderr er ikke buffered (vi vil gerne have fejlbeskeder ud med det samme)


