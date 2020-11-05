import matplotlib.pyplot as plt
import numpy
from scipy import stats

xl = [14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5]
yl = [220, 330, 190, 340, 410, 445, 415]
plt.scatter(xl, yl)
slope, intercept, r, p, std_err = stats.linregress(xl, yl)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, xl))

plt.scatter(xl, yl)
plt.plot(xl, mymodel)
plt.ylabel("Price (R)")
plt.xlabel("Temperatue (C)")
plt.title("Soup sales in relation to temperature")
plt.show()
