#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: Linked list structure
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	/** Check if list is empty or has one node **/
	if (list == NULL || list->next == NULL)
	{
		return (0);
	}


	/** Move slow pointer one step and fast pointer by two steps **/
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
