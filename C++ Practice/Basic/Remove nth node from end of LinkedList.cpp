class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* h = head;
        if(head->next==NULL) return NULL;
        n--;
        while(head!=NULL && n--)
        {
            head = head->next;
        }
        ListNode* start = h;
        if(head->next==NULL) return h->next;
        while(head->next && head->next->next !=NULL)
        {
            start = start->next;
            head = head->next;
        }
        
        if(start->next!=NULL)
        start->next = start->next->next;
        else
        start->next = NULL;
        return h;
    }
};
