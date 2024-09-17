# File permissions

## ls -l example

```
[spiff@ubuntu perms]$ ls -l
total 2
drwxr--r-- 3 spiff spiff 3 Sep 17 13:14 aaa
drwxr-xr-x 2 spiff spiff 2 Sep 17 12:47 bbb
-rw-rw-r-- 1 spiff cdrom 8 Sep 17 12:48 test1.txt
```

- 1 character for type of item
- 9 characters for permissions
- reference-count
- user
- group
- size
- modification date/time
- item name

## Normal file/directory permissions

3 groups (user, group, other) of 3 permission bits (read, write, execute)

Execute rights for scripts and binaries.

Binaries do not need read-permissions to work.

Scripts need read-permissions, but can be invoked with shell if no exec-permission.

Execute permissions on directory give access (cd).
Read permissions on directory is needed to read files.

## Setting permissions with chmod

Set no permissions for group and other: `chmod go= file.txt`

Add read permissions for everyone: `chmod +r file.txt`

Remove read permissions from other: `chmod o-r file.txt`

Add r+x for user and group, set no permissions for other: `chmod ug+rx,o= file.txt`

Who can change permissions?

What happens if user has fewer permissions than group?

## Changing owner or group

- `chgrp` can change the group a file belongs to.
- regular users must be in the target group.
- Only root can change the owner of a file, using the `chown`-command.
- chown can set group, either to users default or specified group.
- User can also use `newgrp` to switch primary group before creating file.

NOTE: use `id` to show current groups. `groups` lists group membership.

## Special permissions

SUID, SGID for executables (does not work for scripts)

SGID for directories.

Sticky bit for directories.

## Octal representation

What does `chmod 755 file.txt` do?

- `rwx` = 4 + 2 + 1 = 7
- `r-x` = 4 + 1 = 5
- `r--` = 4
- `-w-` = 2
- `--x` = 1

What about `chmod 600 file.txt`?

## Other types of items in the filesystem

- 'l' = symbolic link
- 'p' = pipe (mkfifo)
- 's' = socket (unix-domain socket)
- 'c' = character-device
- 'b' = block device

## Reference count

Reference count shows hardlinks.

Reference count for directories shows other references (e.g. `.` in CWD and
`..` in any subdirectory).

## stat and file

- The command `stat` shows details about a filesystem-entry (file, directory, etc.)
```
[spiff@spiff-thinkpad perms]$ stat file1.txt 
  File: file1.txt
  Size: 5         	Blocks: 8          IO Block: 4096   regular file
Device: 10305h/66309d	Inode: 3304745     Links: 1
Access: (0660/-rw-rw----)  Uid: ( 1000/   spiff)   Gid: ( 1000/   spiff)
Access: 2024-09-22 13:37:00.000000000 +0200
Modify: 2024-09-22 13:37:00.000000000 +0200
Change: 2024-09-17 13:54:05.126813316 +0200
 Birth: 2024-09-17 13:45:04.809428685 +0200
```

- The command `file` shows information about a file, based on magic numbers.
```
[spiff@spiff-thinkpad perms]$ file file1.txt 
file1.txt: ASCII text
```

