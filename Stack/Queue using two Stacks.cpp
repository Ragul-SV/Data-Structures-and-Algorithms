/* The method push to push element into the queue */
void StackQueue :: push(int x)
 {
        s1.push(x);
 }

/*The method pop which return the element poped out of the queue*/
int StackQueue :: pop()
{
    int ele;
        if(s2.empty())
        {
            if(s1.empty()) return -1;
            while(!s1.empty())
            {
                int ele = s1.top();
                s1.pop();
                s2.push(ele);
            }
            ele = s2.top();
            s2.pop();
            return ele;
        }
        else
        {
            ele = s2.top();
            s2.pop();
            return ele;
        }
}
