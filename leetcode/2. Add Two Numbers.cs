/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        BigInteger sum = generateNumber(l1)+generateNumber(l2);
        string values = sum.ToString();
        ListNode node = null;
        for (int i = values.Length-1; i>=0; i--){
            node = insert(node, Int32.Parse(values[i].ToString()));
        }
        return node;
    }

    BigInteger generateNumber(ListNode l){
        string sum = "";
        while(l !=null){
            sum = sum+ l.val.ToString();
            l = l.next;
        }
        sum=reverse(sum);
        return BigInteger.Parse(sum);
    }

    ListNode insert(ListNode l, int data){
        ListNode node = new (data);

        if (l==null){
            return node;
        }

        ListNode currentNode = l;
        while(currentNode.next !=null){
            
            currentNode = currentNode.next;
        }

        currentNode.next = node;

        return l;
    }

    string reverse(string s){
        string sum = "";
        for (int i = s.Length-1; i>=0; i--){
            sum = sum+s[i];
        }
        return sum;
    }
}