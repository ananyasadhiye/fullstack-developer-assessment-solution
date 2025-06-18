from collections import Counter

def SearchingChallenge(str_input):
    str_input = str_input.strip()[1:-1]
    items = str_input.split(",")
    strArr = [item.strip().strip('"').strip("'") for item in items]

    keys = [item.split(":")[0] for item in strArr]
    key_counts = Counter(keys)
    max_freq = max(key_counts.values())
    most_common_keys = {key for key, count in key_counts.items() if count == max_freq}

    result = [item for item in strArr if item.split(":")[0] not in most_common_keys]
    return ",".join(result)

print(SearchingChallenge(input()))
