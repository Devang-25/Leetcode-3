class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        i = 0
        while i < len(words):
            j = i
            cur = len(words[j])
            while j < len(words):
                if (j + 1) < len(words):
                    if (cur + len(words[j+1]) + 1) <= maxWidth:
                        j += 1
                elif j > i and j < (len(words) -1):
                    num_split = j - 1
                    space = (maxWidth - cur) / num_split + 1
                    results.append((" " * space).join(w) for w in words[i : j+1])
                    i = j+1
                    break
                elif (j == i) or j == (len(words) - 1):
                    space = maxWidth - cur
                    row = " ".join(w) for w in words[i : j+1]
                    results.append(row + (" " * space))
                    i = j+1
        return results
