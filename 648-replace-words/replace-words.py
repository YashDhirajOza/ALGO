class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)
        root_set = set(dictionary)
        words = sentence.split(" ")
        def find_root(word):
            for i in range(1, len(word) + 1):
                if word[:i] in root_set:
                    return word[:i]
            return word
        result = [find_root(word) for word in words]
        return " ".join(result)
