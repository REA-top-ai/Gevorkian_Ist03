import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])
#csv_array = np.genfromtxt('sample.csv', delimiter=',')
# DELIMITER - разделители 
test_2 = np.genfromtxt('test_2.csv', delimiter=',')
print(test_2)

# a = np.array(l) 
# a_plus_3 = a + 3           --добавляет число 3 к каждому элементу массива a--
#                            --то же самое верно для вычитания, умножения и деления--

# a ** 2
# array([ 1, 4, 9, 16, 25, 36])   --Возведение каждого значения в квадрат--

# np.sqrt(a)
# array([ 1, 1.41421356, 1.73205081, 2, 2.23606798, 2.44948974])

test_3 = np.array([87, 85, 72, 90, 92])
test_3_fixed = test_3 + 2
print(test_3_fixed)

# Массивы также могут быть добавлены или вычтены друг из друга в NumPy, при условии,
# что массивы имеют одинаковое количество элементов.
# При добавлении или вычитании массивов в NumPy каждый элемент будет добавлен /
# вычтен к соответствующему элементу.
# 
# a = np.array([1, 2, 3, 4, 5])
# b = np.array([6, 7, 8, 9, 10])
# a + b
# array([ 7, 9, 11, 13, 15])

total_grade = test_1 + test_2 + test_3_fixed
final_grade = total_grade / 3
print(final_grade)

# одномерные массивы:
# test_1 = np.array([92, 94, 88, 91, 87])
# test_2 = np.array([79, 100, 86, 93, 91])
# test_3 = np.array([87, 85, 72, 90, 92])
# в одном двумерном массиве:
# np.array([[92, 94, 88, 91, 87],
#          [79, 100, 86, 93, 91],
#          [87, 85, 72, 90, 92]])

coin_toss = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])
coin_toss_again = np.array([1, 1, 0, 1, 0, 1, 0, 0, 1, 0])
# a = np.array([5, 2, 7, 0, 11])
# Если бы мы хотели выбрать первый элемент в этом массиве, мы бы вызывали:
# >>> a[0]
# 5
# >>> a[-1]
# 11
# >>> a[-2]
# >>> a[1:3]
# array([2, 7])
# >>> a[:3]
# array([5, 2, 7])
# >>> a[-3:]
# array([7, 0, 11])

test_11 = np.array([92, 94, 88, 91, 87])
test_22 = np.array([79, 100, 86, 93, 91])
test_33 = np.array([87, 85, 72, 90, 92])
jeremy_test_2 = test_22[3]
manual_adwoa_test_1 = test_11[1:3]
# print(jeremy_test_2)    (93)
# print(manual_adwoa_test_1)   (array([94, 88]))
# a = np.array([[32, 15, 6, 9, 14],
#               [12, 10, 5, 23, 1],
#               [2, 16, 13, 40, 37]])
# >>> a[2,1]
# 16
# # selects the first column
# >>> a[:, 0]
# array([32, 12, 2])
# # selects the second row
# >>> a[1, :]
# array([12, 10, 5, 23, 1])
# # selects the first three elements of the first row
# >>> a[0,0:3]
# array([32, 15, 6])
student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])
tanya_test_3 = student_scores[2, 0]
# print(tanya_test_3)  # (87)
cody_test_scores = student_scores[:, -1] 
# print(cody_test_scores)  # (array([87, 91, 92]))

# >>> a = np.array([10, 2, 2, 4, 5, 3, 9, 8, 9, 7])
# >>> a > 5
# array([True, False, False, False, False, False, True, True, True,
# True], dtype=bool)
# Чтобы выбрать все элементы из предыдущего массива,
# которые больше 5, мы должны написать следующее:
# >>> a[a > 5]
# array([10, 9, 8, 9, 7])
# помещаем каждый оператор в круглые скобки и используем
# логические операторы, такие как & (и) и | (или).
# В нашем примере мы можем использовать комбинированные операторы, чтобы найти
# элементы, которые больше пяти или меньше двух:
# >>> a[(a > 5) | (a < 2)]
# array([10, 9, 8, 9, 7])


porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])
cold = porridge[porridge < 60]
# print(cold)  # (array([50, 56, 51]))
hot = porridge[porridge > 80]
# print(hot)  # (array([90, 85, 98]))
just_right = porridge[(porridge >= 60) & (porridge <= 80)]
# print(just_right)  # (array([79, 65, 63, 79]))

temperature_data = np.genfromtxt('temperature_data.csv', delimiter=',')
temperature_fixed = temperature_data - 3.0
# print(temperature_fixed)
monday_temperas = temperature_fixed[0, :]
# print(monday_temperas)  # array([40.6 42.1 55.8 50. ])
thursday_friday_morning = temperature_fixed[3:5, 1]
# print(thursday_friday_morning)  # array([41.1 40.9])
temperature_extremes = temperature_fixed[(temperature_fixed < 50) | (temperature_fixed > 60)]
print(temperature_extremes)  # array([40.6 42.1 44.  41. 49.6 43.7 41.2 49.2 43.5 41.1 48.9 43.2 40.9 48.5])