# Import the necessary packages and modules

import matplotlib.pyplot as plt
import numpy as np

# # Prepare the data
# x = np.linspace(0, 10, 100)
#
# # Plot the data
# plt.plot(x, x, label='linear')
#
# # Add a legend
# plt.legend()
#
# # Show the plot
# plt.show()

##  create subplot with markers and varied plot style
# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(2,3,1) #The three arguments designate the number of rows (1), the number of columns (1) and the plot number (1)
# ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
# ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
# ax.set_xlim(0.5, 4.5)
# plt.show()
#


#
# import matplotlib.pyplot as plt
# plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# t = np.arange(0., 5., 0.2)
#
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
#
# plt.show()

#
# import numpy as np
# import matplotlib.pyplot as plt
#
# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
#
# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
#
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
#
# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()





# import numpy as np
# import matplotlib.pyplot as plt
#
# # Fixing random state for reproducibility
# np.random.seed(19680801)
#
# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)
#
# # the histogram of the data
# n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
#
#
# plt.xlabel('Smarts')
# plt.ylabel('Probability')
# plt.title('Histogram of IQ')
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
# plt.grid(True)
# print(patches[20]) #Rectangle(90.2765,0;2.3397x0.0239775)
# plt.setp(patches[20], 'facecolor', 'r')
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
# more annotations can be found here
# https://matplotlib.org/users/annotations_guide.html
plt.ylim(-2,2)
plt.show()