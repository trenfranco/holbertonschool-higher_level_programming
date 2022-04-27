#include "lists.h"

/**
 * insert_node - inserts node in a sorted linnked list
 * @head: head
 * @number: new number
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *New, *temp;

	temp = *head;
	New = malloc(sizeof(listint_t));
		if (New == NULL)
			return (NULL);
	New->n = number;

	while (temp->next != NULL && temp->n < number)
	{
		temp = temp->next;
	}
	New->next = temp->next;
	temp->next = New;
	return (New);

}
