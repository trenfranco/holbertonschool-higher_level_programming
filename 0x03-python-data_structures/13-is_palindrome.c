#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
size_t sizeList(const listint_t *data);

/**
 * is_palindrome -  checks if a singly linked list is a palindrome.
 * @head: head node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int cont = 0, i, j, *arr1 = NULL;

	if (!*head || !head)
		return (1);
	temp = *head;
	cont = sizeList(*head);
	arr1 = malloc(sizeof(int) * cont);

	i = 0;
	while (i < cont)
	{
		arr1[i] = temp->n;
		temp = temp->next;
		i++;
	}
	j = cont - 1;
	i = 0;
	while (i < (cont - 1) / 2)
	{
		if (arr1[i] != arr1[j])
		{
			free(arr1);
			return (0);
		}
		i++;
		j--;
	}
	free(arr1);
	return (1);
}
/**
 * sizeList - number of elements in a linked list
 * @data: list
 * Return: Cty of nodes
 */
size_t sizeList(const listint_t *data)
{
	int cont = 0;

	while (data != NULL)
	{
		data = data->next;
		cont++;
	}
	return (cont);
}
