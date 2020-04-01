import java.io.*;
import java.util.*;

class QueueOp{
    static void insert(Queue<Integer> q, int k){
        q.offer(k);
    }

    static int findFrequency(Queue<Integer> q, int k){
        int count = 0;
        for(Integer i:q)
        {
            if(i==k) count++;
        }
        return count;
    }
    
}

class GFG {

	public static void main (String[] args) {

		Scanner sc = new Scanner(System.in);
		int testcase = sc.nextInt();
		
		while(testcase-- > 0){
		    Queue<Integer> q = new LinkedList<>();
		    int n = sc.nextInt();
		    QueueOp obj = new QueueOp();
		    for(int i = 0;i<n;i++){
		        int k = sc.nextInt();
		        obj.insert(q, k);
		    }
		   
		    int x = sc.nextInt();
		    for(int i = 0;i<x;i++){
		        int k = sc.nextInt();
		        int f = obj.findFrequency(q, k);
		        if(f != 0){
		            System.out.println(f);
		        }
		        else{
		            System.out.println("-1");
		        }
		    }
		}
	}
} 
