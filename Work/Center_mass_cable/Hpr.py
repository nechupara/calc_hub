height_opora_A = 19.3
ground_A = 35.73

height_opora_B = 19.3
ground_B = 25.62

distance_A_B = 314.79

f_max = 17.19

from_f_to_tower = 191.9



level_cable_A = ground_A + height_opora_A
level_cable_B = ground_B + height_opora_B

if level_cable_A < level_cable_B:
    level_cable_A, level_cable_B = level_cable_B, level_cable_A

level_join_line = level_cable_A - from_f_to_tower/distance_A_B*(level_cable_A - level_cable_B)
print(level_join_line)
delta_f = level_cable_A - level_join_line
strela = f_max - delta_f
print('фактическая стрела: ' + str(strela))


# input('enter')



