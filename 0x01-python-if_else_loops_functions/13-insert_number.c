#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head
 * @number: nuber
 * Return: the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_n = malloc(sizeof(listint_t));

	if (new_n == NULL)
		return (NULL);
	new_n->n = number;
	new_n->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		new_n->next = *head;
		*head = new_n;
	}
	else
	{
		listint_t *current = *head;

		while (current->next != NULL && number > current->next->n)
			current = current->next;
		new_n->next = current->next;
		current->next = new_n;
	}
	return (new_n);
}
