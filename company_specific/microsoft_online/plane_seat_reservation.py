# https://leetcode.com/discuss/interview-question/492652/

seats_map = 'ABCDEFGHJK'
A,B,C,D,E,F,G,H,J,K = range(10)
letter_2_idx = {l: i for i, l in enumerate(seats_map)}

seat4 = [
    [B, C, D, E],
    [D, E, F, G],
    [F, G, H, J]
]


def num_ways(n, seated):
    seats = [[True] * 10 for _ in range(n)]
    for seat in seated.split():
        idx_row = int(seat[0])-1
        idx_seat = letter_2_idx[seat[1]]
        seats[idx_row][idx_seat] = False

    counter = 0
    for row in seats:
        for s0,s1,s2,s3 in seat4:
            if row[s0] and row[s1] and row[s2] and row[s3]:
                counter += 1
                row[s0] = row[s1] = row[s2] = row[s3] = False
    return counter


if __name__ == '__main__':
    print(num_ways(2, '1A 2F 1C'))