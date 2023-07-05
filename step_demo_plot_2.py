# import numpy as np
# import matplotlib.pyplot as plt
#
# # Δημιουργία των δεδομένων θερμοκρασίας
# x = np.arange(14)
# y = np.array([20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 28, 27, 26, 25])
#
# # Απεικόνιση των δεδομένων με το στυλ 'steps-post'
# plt.step(x, y, where='post', label='Temperature')
# plt.plot(x, y, 'o--', color='grey', alpha=0.3)
#
# # Ρύθμιση του γραφήματος
# plt.grid(axis='x', color='0.95')
# plt.legend(title='Parameter where:')
# plt.title('Temperature Variation')
# plt.xlabel('Day')
# plt.ylabel('Temperature (°C)')
#
# plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Υποθέτουμε μια λίστα με ημερομηνίες (x) και θερμοκρασίες (y)
x = [1, 2, 3, 4, 5, 6, 7]
y = [20, 21, 21, 22, 23, 23, 22]

plt.step(x, y, 'b', where='pre', label='pre (default)')
plt.plot(x, y, 'o--', color='grey', alpha=0.3)

plt.step(x, y, 'orange', where='mid', label='mid')
plt.plot(x, y, 'o--', color='grey', alpha=0.3)

plt.step(x, y, 'g', where='post', label='post')
plt.plot(x, y, 'o--', color='grey', alpha=0.3)

plt.grid(axis='x', color='0.95')
plt.legend(title='Parameter where:')
plt.title('Temperature Variation')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')

plt.show()
