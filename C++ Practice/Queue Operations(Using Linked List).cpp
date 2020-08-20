#include <iostream>
using namespace std;

struct Node
{
	int data;
	Node *next;
	Node(int val){
		data = val;
		next = NULL;
	}
};

struct Queue
{
	Node *front,*rear;
	Queue(){
		front=rear=NULL;
	}
	void enqueue(int val)
	{
		Node *temp = new Node(val);
		if(rear==NULL)
		{
			front=rear=temp;
			return;
		}
		rear->next = temp;
		rear = temp;
	}
	int dequeue()
	{
		if(front==NULL)
		{
			return -1;
		}
		Node *temp = front;
		int val = temp->data;
		front = front->next;
		if(front==NULL)rear=NULL;
		delete (temp);
		return val;
	}
};

int main() {
	Queue q;
	q.enqueue(10);
	q.enqueue(20);
	q.enqueue(30);
	q.enqueue(40);
	q.enqueue(50);
	cout<<q.dequeue()<<endl;
	cout<<q.dequeue()<<endl;
	cout<<q.dequeue()<<endl;
	return 0;
}
