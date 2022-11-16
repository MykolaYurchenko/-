import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np
x= [0.2, 0.6, 1.1, 1.8, 2.6]
y=[3.34, 4.53, 2.75, 3.91, 3.57]
spl = UnivariateSpline(x, y)
xs = np.linspace(0.2, 3.57, 1000)
plt.plot(x, y,'ro',xs, spl(xs), 'g')
plt.show()