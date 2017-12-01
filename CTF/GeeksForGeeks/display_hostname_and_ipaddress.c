/////////////////////////////////// C Program to display hostname and IP address
// http://www.geeksforgeeks.org/c-program-display-hostname-ip-address/
// https://auth.geeksforgeeks.org/user/Smitha%20Dinesh%20Semwal/articles

/*
* There are many ways to find Hostname and IP address of a local machine.
* Here is a simple method to find hostname and IP address using C program.
* We will be using the following functions :-
* gethostname() : The gethostname function retrieves the standard host name for
* the local computer.
*ngethostbyname() : The gethostbyname function retrieves host information
* corresponding to a host name from a host database.
* inet_ntoa() : The inet_ntoa function converts an (Ipv4) Internet network
* address into an ASCII string in Internet standard dotted-decimal format.
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <netdb.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

// Returns the hostname for the local computer:
void checkHostName(int hostname)
{
    if (hostname == -1)
    {
        perror("gethostname");
        exit(1);
    }
}
// Returns the host information corresponding to the hostname:
void checkHostEntry(struct hostent * hostentry)
{
    if (hostentry == NULL)
    {
        perror("gethostbyname");
        exit(1);
    }
}

// Converts space-delimited IPv4 addresses to dotted-decimal format:
void checkIPbuffer(char *IPbuffer)
{
    if (NULL == IPbuffer)
    {
        perror("inet_ntoa");
        exit(1);
    }
}

int main()
{
    char hostbuffer[256];
    char *IPbuffer;
    struct hostent *host_entry;
    int hostname;

    // To retrieve hostname:
    hostname = gethostname(hostbuffer, sizeof(hostbuffer));
    checkHostName(hostname);

    // To retrieve host information:
    host_entry = gethostbyname(hostbuffer);
    checkHostEntry(host_entry);

    // To convert an Internet network address into an ASCII string:
    IPbuffer = inet_ntoa(*((struct in_addr*)
                            host_entry->h_addr_list[0]));

    printf("Hostname: %s\n", hostbuffer);
    printf("Host IP: %s\n", IPbuffer);

    return 0;
}

/*
* For some reason, I have to use sudo to run the executable after compilation:
* >>> sudo gcc display_hostname_and_ipaddress.c -o \
*     display_hostname_and_ipaddress && ./display_hostname_and_ipaddress
*/
