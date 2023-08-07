#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>

/**
 * struct listint_s - linked list
 *@a: integer
 *@next: next node
 *
 *Description: linked list node structure
 */
typedef struct listint_s
{
	int a;
	struct listint_s*next;
} listint_t;

listint_t *add_nodeint(listint_t **head, const int a);
size_tprint_listint(const listint_t *h);
int check_cycle(listint_t *list);
void free_listint(listint_t *head);

#endif


