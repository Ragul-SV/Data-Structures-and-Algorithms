bool path(ListNode* head, TreeNode* root)
    {
        if(head==NULL)return true;
        if(root==NULL)return false;
        return head->val==root->val && (path(head->next,root->left) || path(head->next,root->right));
    }
    
bool isSubPath(ListNode* head, TreeNode* root) {
    if(root==NULL) return false;
    return path(head,root) || isSubPath(head,root->left) || isSubPath(head,root->right);
}
