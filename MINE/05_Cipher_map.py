"""
O(n^2) time and O(1) space algorithm ( without any workarounds and hanky-panky stuff! )
Rotate by +90:
    Transpose
    Reverse each row
Rotate by -90:
    Transpose
    Reverse each column
Rotate by +180:
    Method 1: Rotate by +90 twice
    Method 2: Reverse each row and then reverse each column
Rotate by -180:
    Method 1: Rotate by -90 twice
    Method 2: Reverse each column and then reverse each row
    Method 3: Reverse by +180 as they are same
clockwise:
    rotated = zip(*original[::-1])
And counterclockwise:
    rotated_ccw = zip(*original)[::-1]
"""
def recall_password(cipher_grille, ciphered_password):
    _90  = [x for x in zip(*cipher_grille[::-1])]
    _180 = [x[::-1] for x in map(None,*_90)]
    _270 = [x[::-1] for x in map(None,*_180)]
    d = lambda s, e=enumerate: sum([[(c,i) for i,x in e(cipher) if x =='X']
                                           for  c,cipher in e(s)],[])
    m = lambda m: [ciphered_password[cipher[0]][cipher[1]] for cipher in m]
    return "".join(m(d(cipher_grille)+d(_90)+d(_180)+d(_270)))


print recall_password(
    ('X...',
     '..X.',
     'X..X',
     '....'),
    ('itdf',
     'gdce',
     'aton',
     'qrdi')) #== 'icantforgetiddqd'

# # print recall_password(
# #     ('....',
# #      'X..X',
# #      '.X..',
# #      '...X'),
# #     ('xhwc',
# #      'rsqx',
# #      'xqzz',
# #      'fyzr')) #== 'rxqrwsfzxqxzhczy'

# def rotate90Degrees(m):
#     layers = len(m) / 2
#     length = len(m) - 1
#     for layer in range(layers):
#         for i in range(layer, length - layer):
#             temp = m[layer][i]
#             m[layer][i] = m[length - i][layer]
#             m[length - i][layer] = m[length - layer][length - i]
#             m[length - layer][length - i] = m[i][length - layer]
#             m[i][length - layer] = temp


# _90  = [x[::-1] for x in (map(None,)*cipher_grille)]
# _180 = [x[::-1] for x in map(None,*_90)]
# _270 = [x[::-1] for x in map(None,*_180)]

# def recall_password(cipher_grille, ciphered_password):
#     r = lambda d: zip(*d[::-1])
#     d = lambda s, e=enumerate: sum([[(c,i) for i,x in e(cipher) if x =='X']
#                                            for  c,cipher in e(s)],[])
#     m = lambda m: [ciphered_password[cipher[0]][cipher[1]] for cipher in m]
#     cipher = []
#     for x in [1]*4:
#         cipher += m(d(cipher_grille))
#         cipher_grille = r(cipher_grille)
#     return ''.join(cipher)

