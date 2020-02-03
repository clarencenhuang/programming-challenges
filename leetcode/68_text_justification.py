class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        word_lens = list(map(len, words))
        lines = []
        ptr = 0
        while ptr < len(words):
            line = []
            line_len = 0
            while True:
                if ptr >= len(words):
                    break
                next_len = line_len + word_lens[ptr]
                if len(line) > 0:
                    next_len += 1
                if next_len > maxWidth:
                    break

                line.append(words[ptr])
                line_len = next_len
                ptr += 1
            if len(line) == 1 or ptr >= len(words):
                # last line or only 1, left justify
                buffer = " ".join(line)
                padding_right = maxWidth - len(buffer)
                buffer += padding_right * " "
                lines.append(buffer)
            else:
                leftover = maxWidth - line_len
                num_spaces = len(line) - 1
                even_spacing = leftover // num_spaces
                to_distribute = leftover - (even_spacing * num_spaces)
                buffer = ""
                for i, word in enumerate(line):
                    if i > 0:
                        buffer += " " * (even_spacing + 1)
                        if to_distribute > 0:
                            to_distribute -= 1
                            buffer += " "
                    buffer += word
                lines.append(buffer)
        return lines




