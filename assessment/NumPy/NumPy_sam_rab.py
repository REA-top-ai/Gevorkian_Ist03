import numpy as np

calorie_stats = np.genfromtxt('cereal.csv', delimiter=' ', dtype=float, invalid_raise=False)
calorie_stats = calorie_stats[~np.isnan(calorie_stats)]
# print(calorie_stats)

crunchie_munchies = 60
average_calories = np.mean(calorie_stats) - crunchie_munchies
#print(average_calories) #44.4(4)
calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)
median_calories = np.median(calorie_stats_sorted)
# print(median_calories) # 110.0
nth_percentile = np.percentile(calorie_stats_sorted, 7)
print(nth_percentile) # 63
more_calories = 100 - 7
# print(more_calories) # 95
calorie_std = np.std(calorie_stats_sorted)
# print(calorie_std) # 19.87615979999813

print("=== ВЫВОДЫ ===")
print("""
Анализ данных конкурентов показывает, что CrunchieMunchies с 60 калориями 
на порцию значительно полезнее большинства злаков на рынке:

1. Средняя калорийность конкурентов на {:.2f} калорий выше, чем у CrunchieMunchies.
2. Медиана составляет {:.1f} калорий, что почти в 2 раза больше наших хлопьев.
3. {:.1f}% всех конкурентов имеют более 60 калорий на порцию.
4. Даже самый низкий процентиль, превышающий 60 калорий, составляет {:.1f} калорий.

Эти данные можно использовать в маркетинге для демонстрации, что CrunchieMunchies 
являются одним из самых низкокалорийных вариантов на рынке, что делает их 
отличным выбором для потребителей, следящих за своим здоровьем и весом.
""".format(average_calories, median_calories, more_calories, nth_percentile))




