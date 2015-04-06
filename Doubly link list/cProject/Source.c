#include<stdio.h>
#include<stdlib.h>

 typedef struct 
 {
	int* next;
	int* prev;
	int data;
}Node;

Node* head;
Node* CreateNode(int num)
{
	Node* node = malloc(sizeof(Node));
	node->next = NULL;
	node->prev = NULL;
	node->data = num;
	return node;

}
void insertAtHead(int num)
{
	Node* NewNode = CreateNode(num);
	if (head == NULL)
	{
		head = NewNode;
	}
	else
	{
		NewNode->next = head;
		head->prev = NewNode;
		head = NewNode;
	}


}


void insertAtTail(int num)
{
	Node* NewNode = CreateNode(num);
	if (head == NULL)
	{
		head = NewNode;
	}
	else
	{
		Node *temp=head;
		while (temp->next != NULL)
			temp = temp->next;
		temp->next = NewNode;
		NewNode->prev = temp;
	}
}

void DisplayHeadToTail()
{
	if (head == NULL)
	{
		printf("\nList is Empty\n");
		return;
	}
	Node *temp = head;
	printf("\nHead to Tail Data:");

	while (temp!=NULL)
	{
		printf(" %d",temp->data);
		temp = temp->next;
	}
	printf("\n");

}

void DisplayTailToHead()
{
	if (head == NULL)
	{
		printf("\nList is Empty\n");
		return;
	}
	Node *temp = head;
	printf("\nTail to Head Data:");
	while (temp->next != NULL)
		temp = temp->next;
	while (temp != NULL)
	{
		printf(" %d", temp->data);
		temp = temp->prev;
	}
	printf("\n");

}
int main()
{
	head = NULL;
	
	insertAtHead(1);
	insertAtHead(2);
	insertAtHead(3);
	insertAtHead(4);
	insertAtTail(5);
	insertAtTail(6);
	insertAtTail(7);
	insertAtTail(8);
	
	DisplayHeadToTail();
	DisplayTailToHead();
}