from collections import Counter


list_strings = ["eat", "tea", "ate", "bat", "tab", "rat", "car"]


def anagrams_output(list_strings):
    anagrams_list = []
    length = len(list_strings)
    i = 0
    while (i < length):
        current_string = list_strings[i]
        j = i + 1
        while (j < length):
            comparing_string = list_strings[j]
            if (Counter(current_string) == Counter(comparing_string)):
                if (current_string not in anagrams_list):
                    anagrams_list.append(current_string)
                if (comparing_string not in anagrams_list):
                    anagrams_list.append(comparing_string)
            j += 1
        i += 1
    return anagrams_list


result = anagrams_output(list_strings)
print(result)
