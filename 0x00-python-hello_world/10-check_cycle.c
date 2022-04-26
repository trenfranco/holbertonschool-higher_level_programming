#include "lists.h"

/**
 * check_cycle - check if it has a cycle
 *@list: list
 * Return: 0 if no cycle 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;
	slow = list;
	fast = list;

	while(slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return(1);
	}
	return(0);
}
