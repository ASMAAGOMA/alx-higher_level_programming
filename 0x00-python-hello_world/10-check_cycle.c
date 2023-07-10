#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: the point to check with
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
