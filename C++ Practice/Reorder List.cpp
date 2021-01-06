Node* reverse(Node* head)
{
    Node *prev = NULL,*cur=head,*nxt;
    while(cur!=NULL)
    {
        nxt = cur->next;
        cur->next = prev;
        prev = cur;
        cur = nxt;
    }
    return prev;
}

void reorderList(Node* head) {
    // Your code here
    Node* slow=head;
    Node* fast = head;
    while(fast!=NULL && fast->next!=NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
    }
    Node* head1 = head;
    Node* head2 = reverse(slow->next);
    slow->next = NULL;
    Node* temp = new Node(0);
    Node* cur = temp;
    while(head1!=NULL || head2!=NULL)
    {
        if(head1!=NULL)
        {
            cur->next = head1;
            cur = cur->next;
            head1 = head1->next;
        }
        if(head2!=NULL)
        {
            cur->next = head2;
            cur = cur->next;
            head2 = head2->next;
        }
    }
}
