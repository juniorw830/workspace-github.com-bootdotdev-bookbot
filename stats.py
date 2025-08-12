def get_num_words(text: str) -> int:
    """Return the number of whitespace-delimited words in text."""
    return len(text.split())

def get_char_counts(text: str) -> dict:
    """Return a dictionary with lowercase character counts."""
    counts = {}
    for char in text.lower():  # go through every character in lowercase form
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_char_counts(char_counts: dict) -> list:
    """Convert char_counts dict to a sorted list of dicts by frequency."""
    sorted_list = []

    for char, count in char_counts.items():
        if char.isalpha():  # only letters
            sorted_list.append({"char": char, "num": count})

    def sort_on(item):
        return item["num"]

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list