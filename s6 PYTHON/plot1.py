
import matplotlib


# matplotlib

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
fig=plt.figure(figsize=(10,10))
x=[10,20,30,40,50]
y=[20,30,40,50,60]
plt.plot(x,y,"y--",label="s-cline") 
plt.legend(loc="upper right")
plt.title("student course plot")
plt.ylabel("course selection")
plt.xlabel("no of students")
plt.show()