#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>
#include <stdio.h>

/**
 * struct listint_s - linked list
 * @a: integer
 * @next: points to node
 * Description: node structure for python project
 */
typedef struct listint_s
{
	int a;
	struct listint_s *next;
} listint_t;

#endif
