public class Solution
{

    public ListNode MergeTwoLists(ListNode list1, ListNode list2)
    {
        List<int> initialList = buildList(list1, list2);

        return buildLinkedList(initialList);
    }
    List<int> buildList(ListNode list1, ListNode list2)
    {

        List<int> result = new List<int>();

        if (list1 != null)
        {
            while (list1 != null)
            {

                result.Add(list1.val);
                list1 = list1.next;
            }
        }
        if (list2 != null)
        {
            while (list2 != null)
            {
                result.Add(list2.val);
                list2 = list2.next;
            }
        }

        return sortList(result);
    }
    List<int> sortList(List<int> list)
    {
        for (int i = 0; i < list.Count - 1; i++)
        {

            for (int j = 0; j < list.Count - i - 1; j++)
            {
                if (list[j] > list[j + 1])
                {
                    int temp = list[j];
                    list[j] = list[j + 1];
                    list[j + 1] = temp;
                }

            }
        }
        return list;
    }
    ListNode buildLinkedList(List<int> list)
    {
        ListNode result = new ListNode(0);
        ListNode operation = result;
        for (int i = 0; i < list.Count; i++)
        {
            while (operation.next != null)
            {
                operation = operation.next;
            }
            operation.next = new ListNode(list[i]);
        }

        return result.next;
    }
}