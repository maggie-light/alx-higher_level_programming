#ifndef LIST_H
#define LIST_H

#include <stdlib.h>

/**
 * struct list_s - singly list list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly list nodes
 */
typedef struct lisint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
listint_t *insert_node(listint_t **head, int number);

#endif /*LIST_H */


