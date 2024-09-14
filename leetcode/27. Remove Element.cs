public class Solution
{
    public int RemoveElement(int[] nums, int val)
    {
        if (nums.Length == 0) return 0;
        int n = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] != val)
            {
                nums[n] = nums[i];
                n++;
            }
        }
        return n;
    }
}