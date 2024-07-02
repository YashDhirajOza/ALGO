class Solution {
    public long countCompleteDayPairs(int[] hours) {
        Map<Integer, Integer> remainderCount = new HashMap<>();
        long countPairs = 0;
        for (int hour : hours) {
            int remainder = hour % 24;
            int complement = (24 - remainder) % 24;
            if (remainderCount.containsKey(complement)) {
                countPairs += remainderCount.get(complement);
            }
            if (remainderCount.containsKey(remainder)) {
                remainderCount.put(remainder, remainderCount.get(remainder) + 1);
            } else {
                remainderCount.put(remainder, 1);
            }
        }
        return countPairs;
    }
}
