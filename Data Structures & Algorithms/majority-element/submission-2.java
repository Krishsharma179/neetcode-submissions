class Solution {
    public int majorityElement(int[] nums) {

        
        HashMap<Integer, Integer> hash = new HashMap<>();

        int maxcount = 0, res = 0;

        for (int num : nums) {
            if (hash.containsKey(num)) {
                hash.put(num, hash.get(num) + 1);
            } else {
                hash.put(num, 1);
            }
        }

        for (Map.Entry<Integer, Integer> entry : hash.entrySet()) {
            int num = entry.getKey();
            int count = entry.getValue();

            if (count > maxcount) {
                maxcount = count;
                res = num;
            }
        }

        return res;
    }
}
