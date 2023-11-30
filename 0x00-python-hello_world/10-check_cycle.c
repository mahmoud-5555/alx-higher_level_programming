#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if the list have loop cycle
 * @list: pointer to head of list
 * Return: number of nodes
 */
int check_cycle(listint_t *list)
{
	listint_t *two_steps;

	if (list != NULL && list->next != NULL)
	{
		two_steps = list->next;
	}
	else
	{
		return (0);
	}

	while (list != NULL && two_steps != NULL)
	{
		if (two_steps == list)
				return (1);
		list = list->next;
		if (two_steps->next != NULL)
			two_steps = (two_steps->next)->next;
		else
			break;
	}
	return (0);

}
