class Solution {
    public boolean hasDuplicate(int[] nums) {
        Hashtable seen = new Hashtable();
        int count = 0;
        for (int i=0; i<nums.length; i++){
            if (seen.containsKey(nums[i])){
                return true;
            }
            seen.put(nums[i], 0);
        }
        return false;
    }
}
