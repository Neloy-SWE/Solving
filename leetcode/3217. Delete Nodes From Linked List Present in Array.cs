public class Solution
{
    public ListNode ModifiedList(int[] nums, ListNode head)
    {

        if (head == null)
        {
            return head;
        }

        HashSet<int> removableValues = new(nums);
        ListNode temporaryNode = new(0);
        temporaryNode.next = head;
        ListNode currentNode = temporaryNode;


        while (currentNode.next != null)
        {
            if (removableValues.Contains(currentNode.next.val))
            {
                currentNode.next = currentNode.next.next;
            }
            else
            {
                currentNode = currentNode.next;
            }
        }
        head = temporaryNode.next;

        return head;
    }


}