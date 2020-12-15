ListNode* swapPairs(ListNode* head) {
        if(head==NULL)return NULL;
        if(head->next==NULL) return head;
        ListNode* nxt = head->next;
        head->next = swapPairs(nxt->next);
        nxt->next = head;
        return nxt; 
    }
