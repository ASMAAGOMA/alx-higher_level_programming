#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to pointer of head of the list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compare_lists - Compares two linked lists for equality
 * @list1: First linked list
 * @list2: Second linked list
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return 0;

		list1 = list1->next;
		list2 = list2->next;
	}

	/* If one list is shorter than the other, they are not equal */
	if (list1 != NULL || list2 != NULL)
		return (0);

	return (1);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to pointer of head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *prev_slow_ptr = *head;
	listint_t *second_half;
	int palindrome = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast_ptr != NULL && fast_ptr->next != NULL)
		{
			fast_ptr = fast_ptr->next->next;
			prev_slow_ptr = slow_ptr;
			slow_ptr = slow_ptr->next;
		}

		if (fast_ptr != NULL)
			slow_ptr = slow_ptr->next;

		second_half = slow_ptr;
		prev_slow_ptr->next = NULL;

		reverse_list(&second_half);

		palindrome = compare_lists(*head, second_half);

		reverse_list(&second_half);

		if (fast_ptr != NULL)
		{
			prev_slow_ptr->next = slow_ptr;
			slow_ptr->next = second_half;
		}
		else
		{
			prev_slow_ptr->next = second_half;
		}
	}

	return (palindrome);
}
