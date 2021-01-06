/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
public:
    Node* flatten(Node* head) {
        Node* h = head;
        while(h!=NULL)
        {
            if(h->child!=NULL)
            {
                Node* nxt = h->next;
                h->next = h->child;
                h->next->prev = h;
                h->child = NULL;
                Node* temp = h->next;
                while(temp->next!=NULL)
                    temp = temp->next;
                temp->next = nxt;
                if(nxt!=NULL)
                    nxt->prev = temp;
            }
            h = h->next;
        }
        return head;
    }
};
