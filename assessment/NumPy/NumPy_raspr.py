import numpy as np
# import codecademylib
from matplotlib import pyplot as plt

sum = 5 + 2 
width = 5
ans = 2

# # This plots a histogram
# plt.hist(data)
# # This displays the histogram
# plt.show()

# plt.hist(data, bins = 5)
# plt.show()

# # We pass 51 so that our range includes 50
# plt.hist(data, range=(20, 51))

# d = np.array([1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5])
# plt.hist(d, bins=5, range=(1, 6))
# plt.show()

# commutes = np.array([20, 30, 50, 40, 24, 26, 27,27, 30, 50, 20, 34, 15,
# 18,17, 35,37,38, 43,45,47])
# plt.hist(commutes, bins=6, range=(20, 50))
# plt.show()

# graph_a = 'multimodal'
# graph_b = 'unimodal'
# graph_c = 'bimodal'

# graph_a = 'right-skewed'
# graph_b = 'left-skewed'
# graph_c = 'symmetric'

a = np.random.normal(0, 1, size = 100000)

b_data = np.random.normal(6.7, 0.7, size = 1000)
f_data = np.random.normal(7.7, 0.3, size = 1000)
plt.hist(b_data,
bins=30, range=(5, 8.5), histtype='step',
label='Brachiosaurus')
plt.hist(f_data,
bins=30, range=(5, 8.5), histtype='step',
label='Fictionosaurus')
plt.xlabel('Femur Length (ft)')
plt.legend(loc=2)
plt.show()

mystery_dyno = 'brachiosaurus'
answer = 'false'

