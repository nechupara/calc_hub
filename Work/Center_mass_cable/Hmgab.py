opora_A = 19.3
opora_B = 19.3
gabarit = 7

fmax = (opora_A + opora_B)/2 - gabarit
print('максимально допустимая стрела = ' + str(fmax))
height_mgab = (opora_A + opora_B)/2 - 2/3*fmax
print('приведенный центр массы для габаритного пролёта = ' + str(round(height_mgab, 2)))