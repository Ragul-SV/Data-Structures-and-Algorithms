class Solution {
public:
    ListNode* reverse(ListNode* head)
    {
        ListNode* cur = head;
        ListNode* prev = NULL;
        ListNode* nxt = NULL;
        while(cur!=NULL)
        {
            nxt = cur->next;
            cur->next = prev;
            prev = cur;
            cur = nxt;
        }
        return prev;
    }
    
    bool isPalindrome(ListNode* head) {
        int len = 0;
        ListNode* h = head;
        while(head!=NULL)
        {
            len++;
            head = head->next;
        }
        if(len==0 || len==1) return true;
        if(len==2)
        {
            if(h->val != h->next->val) return false;
            else return true;
        }
        ListNode* slow = h;
        ListNode* fast = h;
        while(fast!=NULL && fast->next!=NULL)
        {
            fast = fast->next->next;
            slow = slow->next;
        }
        ListNode* rev_head;
        if(len%2==0)
            rev_head = reverse(slow);
        else
            rev_head = reverse(slow->next);
        head = h;
        while(rev_head!=NULL)
        {
            if(head->val != rev_head->val) return false;
            head = head->next;
            rev_head = rev_head->next;
        }
        return true;
    }
};
