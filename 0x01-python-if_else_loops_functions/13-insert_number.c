#include <stdio.h>
#include <stdlib.h>
#include"lists.h"


/**
 * insert_node- function that insert node in side the linked list
 * @head: pointer to the node that well insert after it  of list (by refrance)
 * @number: value in side the node
 * Return: null or the address of new node
 * number of nodes
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *it, *l_it;

	if (head == NULL)
		return (NULL);

	it = *head;
	l_it = it;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	while (it != NULL)
	{
		if (it->n > number || it == NULL)
			break;
		l_it = it;
		it = it->next;
	}

	new_node->n = number;
	new_node->next = l_it->next;
	l_it->next = new_node;
	return (new_node);
}
