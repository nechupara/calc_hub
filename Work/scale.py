#scale1 : scale2
scale1 = 1
scale2 = 2000

mm_to_m = scale2/(scale1*1000)
m_to_mm = scale1*1000/scale2

mm_to_km = mm_to_m/1000
km_to_mm = m_to_mm*1000

print('масштаб %s:%s' % (scale1, scale2))
print('в 1 мм %s м        (/%s)' % (mm_to_m, m_to_mm))
print('в 1 м %s мм        (/%s)' % (m_to_mm, mm_to_m))
print()

print('в 1 мм %s км        (/%s)' % (mm_to_km, km_to_mm))
print('в 1 км %s мм        (/%s)' % (km_to_mm, mm_to_km))
