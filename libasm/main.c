/*
◦ ft_strlen (man 3 strlen)
◦ ft_strcpy (man 3 strcpy)
◦ ft_strcmp (man 3 strcmp)
◦ ft_write (man 2 write)
◦ ft_read (man 2 read)
◦ ft_strdup (man 3 strdup, you can call to malloc)
*/
#include <string.h>
#include <stdio.h>

#define T_STRING "start libasm!!"

// int	main(int argc, char **argv){
int	main(void){
	printf("%lu\n", strlen(T_STRING));
	return (0);
}