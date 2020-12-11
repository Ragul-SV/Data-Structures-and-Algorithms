#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int data;
	Node *next;
};

void push(Node **head,int val)
{
	
	Node *node = *head;
	Node *temp = new Node();
	temp->data = val;
	temp->next = NULL;
	if(*head==NULL)
	{
		*head = temp;
		return;
	}
	while(node->next!=NULL)
	{
		node = node->next;
	}
	node->next = temp;
}

void printList(Node *head)
{
	while(head)
	{
		cout<<head->data<<" ";
		head = head->next;
	}
	cout<<endl;
}

Node* reverse(Node *head)
{
	Node *cur = NULL;
	Node *prev = NULL;
	while(head!=NULL)
	{
		cur = head->next;
		head->next = prev;
		prev = head;
		head = cur;
	}
	return prev;
}

Node* reverseK(Node *head, int k)
{
	Node *cur = head;
	Node *nxt = NULL;
	Node *prev = NULL;
	int count = 0;
	while(cur!=NULL && count<k)
	{
		nxt = cur->next;
		cur->next = prev;
		prev = cur;
		cur = nxt;
		count++;
	}
	if(nxt!=NULL)
	head->next = reverseK(nxt,k);
	return prev;
}

int nthfromstart(Node *head,int n)
{
	n--;
	while(n--)
	{
		head = head->next;
	}
	return head->data;
}

int nthfromend(Node *head,int n)
{
	Node *res = head;
	n--;
	while(n--)
	{
		head = head->next;
	}
	while(head->next!=NULL)
	{
		res = res->next;
		head = head->next;
	}
	return res->data;
}

bool detectLoop(Node *head)
{
	unordered_set<Node*> s;
	while(head!=NULL)
	{
		if(s.find(head) != s.end()) return true;
		s.insert(head);
		head = head->next;
	}
	return false;
}

int middle(Node* head)
{
	Node *fast=head,*slow=head;
	while(fast!=NULL && fast->next!=NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	return slow->data;
}

int main()  
{  
    Node *head = NULL;
    for(int i=1;i<=7;i++)
    {
    	push(&head,i);
    }
    printList(head);
    head = reverse(head);
    printList(head);
    cout<<middle(head)<<endl;
    cout<<nthfromstart(head,5)<<endl;
    cout<<nthfromend(head,5)<<endl;
    head = reverseK(head,2);
    printList(head);
    head->next->next->next = head->next;
    cout<<detectLoop(head)<<endl;
    
}
