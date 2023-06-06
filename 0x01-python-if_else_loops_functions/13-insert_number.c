#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: node pinter
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	else
	{
		if (current->n > number)
		{
			new->next = current;
			*head = new;
			return (new);
		}
		while (current->next != NULL)
		{
			if (current->next->n > number)
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
			current = current->next;
		}
	}
	current->next = new;
	return (new);
}
