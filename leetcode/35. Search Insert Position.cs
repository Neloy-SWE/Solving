public class Solution {
    public int SearchInsert(int[] nums, int target) {
        int nutral = (int)nums.Count()/2;
        int returnValue = 0;
        if (nums.Count()==1){
            if (target > nums[0]){
                return 1;
            }
            else{
                return 0;
            }
        }
        else if (nums[nutral]>=target){
            for (int i = 0; i<=nutral; i++){
                if (target<=nums[i]){
                    returnValue= i;
                    break;
                }
            }
        }
        else{
            for (int i = nutral; i<= nums.Count()-1; i++){
                if (target<=nums[i]){
                    returnValue= i;
                    break;
                }
                else if (i==nums.Count()-1){
                    returnValue= i+1;
                    break;
                }
            }
        }
        return returnValue;
    }
}