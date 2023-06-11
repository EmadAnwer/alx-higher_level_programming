#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * Return: address of the new element or NULL if it fails
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int len, *array_int, i;

	current = *head;
	if (!head || !*head || !current->next)
		return (1);
	while (current != NULL)
	{
		len++;
		current = current->next;
	}
	array_int = (int *)malloc(len * sizeof(int));
	for (i = 0; i < len; i++)
	{
		array_int[i] = current->n;
		current = current->next;
	}
	for (i = 0; i < len / 2; i++)
	{
		if (array_int[i] != array_int[len - 1 - i])
			return (0);
	}

	return (1);
}
