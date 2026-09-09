import numpy as np
from matplotlib import pyplot as plt

mean_sat = 1000
std_sat = 100
one_above = mean_sat + std_sat
one_below = mean_sat - std_sat
one_std = 2000 * 0.68
print(one_above, one_below, one_std)

# Let's generate 10,000 "experiments"
# N = 10 shots
# P = 0.30 (30% he'll get a free throw)
# a = np.random.binomial(10, 0.30, size=10000)

# plt.hist(
#     a,
#     bins=np.arange(-0.5, 11.5, 1),
#     density=True
# )
# plt.xlabel('Number of "Free Throws"')
# plt.xticks(range(11))
# plt.ylabel('Frequency')
# plt.show()


# посчитаем вероятность того, что он попадет 4 раза в корзину:
# a = np.random.binomial(10, 0.30, size=10000)
# np.mean(a == 4)
# Когда мы запустим этот код, мы получим:
# >> 0.1973

# email = np.random.binomial(500, 0.05, size=10000)
# # plt.hist(email)
# # plt.show()
# no_emails = np.mean(email == 0)
# print(no_emails * 100, '%')
# eight_percent = 500 * 0.08
# print(eight_percent)
# b_test_emails = np.mean(email >= eight_percent)
# print(b_test_emails * 100, '%' , b_test_emails)


with open('sunflower.csv', 'r') as file:
    sunflowers = np.array(
        [float(x) for x in file.read().split()]
    )
sunflowers_mean = np.mean(sunflowers)
sunflowers_std = np.std(sunflowers)

# plt.hist(sunflowers,
# range=(11, 15), histtype='step', linewidth=2,
# label='observed', normed=True)
# plt.legend()
# plt.show()
sunflowers_normal = np.random.normal(sunflowers_mean, sunflowers_std, size=5000)
plt.hist(sunflowers_normal,
range=(11, 15), histtype='step', linewidth=2,
label='normal', density=True)
plt.legend()
plt.show()

experiments = np.random.binomial(200, 0.1, size = 50000)
prob = np.mean(experiments < 20)
print(prob * 100, '%')
