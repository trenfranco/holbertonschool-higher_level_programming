#include "lists.h"

/**
 * insert_node - inserts node in a sorted linnked list
 * @head: head
 * @number: new number
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *New, *temp, *aux;

	temp = *head;
	aux = *head;
	New = malloc(sizeof(listint_t));
		if (New == NULL)
			return (NULL);
	New->n = number;

	if (head == NULL || *head == NULL)
	{
		*head = New;
		return (New);
	}
	if (number < 0)
	{
		New->next = *head;
		*head = New;
		return (New);
	}

	while (temp->next != NULL && temp->n < number)
	{
		aux = temp;
		temp = temp->next;
	}
	if (number > temp->n)
	{
		New->next = temp->next;
		aux->next = New;
		return (New);
	}
	New->next = aux->next;
	aux->next = New;
	return (New);

}
