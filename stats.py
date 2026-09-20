def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowercase_text = text.lower()
    ch_counts = {}
    for ch in lowercase_text:
        if ch in ch_counts:
            ch_counts[ch] += 1
        else:
            ch_counts[ch] = 1
    return ch_counts

def sort_on(sortOnTuple: tuple[str, int]) -> int:
    if sortOnTuple[1] is None:
        return 0
    return sortOnTuple[1]

def chars_dict_to_sorted_list(ch_dict):
    listOfSorted = []
    for key in ch_dict:
        count = ch_dict[key]
        listOfSorted.append((key, count))
    listOfSorted = sorted(listOfSorted, key=sort_on, reverse=True)
    return listOfSorted


