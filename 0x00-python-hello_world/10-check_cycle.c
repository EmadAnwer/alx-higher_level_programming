#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
int check_cycle(listint_t *list)
{
	listintp_t *pinters_list = NULL, *current_p, *new_p;
	listint_t *current;
	
	while (list != NULL)
	{
		current = list;

		while (pinters_list != NULL)
		{
			current_p = pinters_list;

			if(current == current_p->p)
			{
				free_listintp(pinters_list);
				return (1);
			}
				
			pinters_list = pinters_list->next;
		}
		new_p = malloc(sizeof(listintp_t));
		if (pinters_list == NULL)
			return (-1);
		new_p->p = current;
		new_p->next = pinters_list;
		pinters_list = new_p;
		list = list->next;
	}
	free_listintp(pinters_list);
	return (0);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listintp(listintp_t *head)
{
	listintp_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
