#include <stdio.h>
//#include <sys/types.h>
#include <unistd.h>
#include <sys/ptrace.h>
#include <sys/wait.h>


void do_fuzz(char* argv[]) {
    int status;
    pid_t pid;
    if (!(pid = fork())) {
        ptrace(PT_TRACE_ME, 0, NULL, NULL);
//        execv(argv[0], argv);
        // here goes execution
    } else {
        waitpid(pid, &status, 0);
        if (WIFEXITED(status)) {
            printf("Process %d exited with code %d\n", pid, WEXITSTATUS(status));
            return;
        } else if ( WIFSIGNALED (status) )
        { /* завершение программы по сигналу */
            printf ("Process %d terminated by unhandled signal %d\n",
                    pid, WTERMSIG (status));
            return;
        }
    }
}


int main(int argc, char* argv[]) {
//    printf("Hello, World!\n");
    do_fuzz(argv);
    return 0;

}
