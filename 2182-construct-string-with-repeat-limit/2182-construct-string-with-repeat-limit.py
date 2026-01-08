from collections import Counter

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        letters = sorted(freq.keys(), reverse=True)
        result = []

        while letters:
            ch = letters[0]
            use = min(freq[ch], repeatLimit)
            result.append(ch * use)
            freq[ch] -= use

            if freq[ch] == 0:
                letters.pop(0)
            else:
                # Need a smaller character to break the sequence
                if len(letters) == 1:
                    break  # no smaller character available

                next_ch = letters[1]
                result.append(next_ch)
                freq[next_ch] -= 1

                if freq[next_ch] == 0:
                    letters.pop(1)

        return "".join(result)
