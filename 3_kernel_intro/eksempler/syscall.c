#include <sys/syscall.h>
#include <unistd.h>

int main(void) {
  char *str = "Hello world\n";
  syscall(SYS_write, 1, str, 12);

  return 0;
}