height_opora_A = 26.5
ground_A = 67.86

height_opora_B = 26.5
ground_B = 69.27

distance_A_B = 350

from_f_to_tower = 179

f_max = 15.72


level_cable_A = ground_A + height_opora_A
level_cable_B = ground_B + height_opora_B

if level_cable_A < level_cable_B:
    level_cable_A, level_cable_B = level_cable_B, level_cable_A

level_join_line = level_cable_A - from_f_to_tower/distance_A_B*(level_cable_A - level_cable_B)
print(level_join_line)
delta_f = level_cable_A - level_join_line
strela = f_max - delta_f
print('фактическая стрела: ' + str(strela))
Hpr = (height_opora_A + height_opora_B)/2 - 2/3*strela
print('Приведенная высота центра массы = '+ str(round(Hpr, 2)))

# input('enter')



