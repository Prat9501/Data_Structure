# def convert(s, n):
#     st = ""
#     for i in range(n, 0, -1):
#         for ji in range(0, len(s), i+1):
#             st += s[ji]
#     print(st)



def convert(s, numRows):
    if numRows == 1:
        return s
    rows = [''] * numRows
    cur_row, dow = 0, 0

    for char in s:
        # import pdb; pdb.set_trace()
        rows[cur_row] += char
        if cur_row == 0 or cur_row == numRows-1:
            dow ^= 1
        cur_row += 1 if dow else -1

    res = ''.join([row for row in rows])
    print(res)


convert("PAYPALISHIRING", 4)
