class Solution(object):
    def countCharacters(self, words, chars):
        char_count = {}
        result = 0

        # Count characters in chars
        for char in chars:
            char_count[char] = char_count.get(char, 0) + 1

        # Check each word in words
        for word in words:
            word_count = {}
            is_good_word = True

            # Count characters in the current word
            for char in word:
                word_count[char] = word_count.get(char, 0) + 1

            # Check if the word can be formed using chars
            for char, count in word_count.items():
                if char not in char_count or count > char_count[char]:
                    is_good_word = False
                    break

            # If the word is good, add its length to the result
            if is_good_word:
                result += len(word)

        return result

solution_instance = Solution()
print(solution_instance.countCharacters(["cat","bt","hat","tree"], "atach"))  
print(solution_instance.countCharacters(["hello","world","leetcode"], "welldonehoneyr"))  # 
