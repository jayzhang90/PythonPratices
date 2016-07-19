

def recktangel(word="RECK", width=2, height=2):
    word_normal = word
    word_flipped = word[::-1]
    word_len = len(word)

    rectangle_width = word_len * width - (width - 1)
    rectangle_height = word_len * height - (height - 1)
    rectangle = [[" "] * rectangle_width for i in range(rectangle_height)]

    for x in range(width):
        for y in range(height):
            if (x + y) % 2 == 0:
                word = word_normal
            else:
                word = word_flipped

            rx = y * (word_len - 1)
            ry = x * (word_len - 1)
            for i in range(word_len):
                rectangle[0 + rx][i + ry] = word[i]  # top
                rectangle[i + rx][0 + ry] = word[i]  # left
                rectangle[word_len - 1 + rx][i + ry] = word[word_len - 1 - i]  # bottom
                rectangle[i + rx][word_len - 1 + ry] = word[word_len - 1 - i]  # right

    print("\n".join([" ".join(line) for line in rectangle]) + "\n")


recktangel("RECT", 3, 1)


'''
input: word = "RECT", width = 3, height = 1
output:
    R E C T C E R E C T
    E     C     E     C
    C     E     C     E
    T C E R E C T C E R
'''