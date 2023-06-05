#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle -  checks if a singly linked list has a cycle
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *my_pointer;

	current = list;
	my_pointer = list;
	while (current != NULL && my_pointer && my_pointer->next)
	{
		current = current->next;
		my_pointer = my_pointer->next->next;
		if (my_pointer == current)
			return (1);
	}

	return (0);
}
