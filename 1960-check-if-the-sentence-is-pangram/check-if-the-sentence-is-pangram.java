class Solution {
    public boolean checkIfPangram(String sentence) {
        Set<Character> alphabetSet = new HashSet<>();
        for (char c = 'a'; c <= 'z'; c++) {
            alphabetSet.add(c);
        }
        Set<Character> inputSet = new HashSet<>();
        for (char c : sentence.toCharArray()) {
            inputSet.add(Character.toLowerCase(c));
        }
        return inputSet.containsAll(alphabetSet);
    }
}
