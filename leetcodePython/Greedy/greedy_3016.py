from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        char_freq = Counter(word)
        key_maps, key_index = [0]*8, 0
        press_count = 0
        for ch, freq in char_freq.most_common():
            if key_index < len(key_maps):
                key_maps[key_index] += 1
                press_count += freq
                key_index += 1
                continue
            index = key_index % len(key_maps)
            key_maps[index] += 1
            new_press = freq * key_maps[index]
            press_count += new_press
            key_index += 1
        return press_count
