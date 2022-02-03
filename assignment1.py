import numpy as np
import matplotlib.pyplot as plt 
import re

np.set_printoptions(suppress=True)

arr_uniformly = np.random.uniform(0,1,100)
arr_gaussian = np.random.normal(50,50,200)

# print(arr_uniformly)
# print(arr_gaussian)

fig1, ax = plt.subplots(figsize=(10,7))

array_u = [arr_uniformly, []]
array_g = [[], arr_gaussian]
 
# Creating plot
ax.boxplot(array_u, labels=['uniformly', ''])
ax2 = ax.twinx()
ax2.boxplot(array_g, labels=['', 'gaussian'])
 
# show plot
plt.show()
plt.savefig("fig1.png")
plt.close(fig1)

#################

fig2, ax = plt.subplots(figsize=(10,7))
n, bins, patches = ax.hist(arr_gaussian, bins=20, color='green')
ax2 = ax.twinx()
n, bins, patches = ax2.hist(arr_uniformly, bins=20, color='red')

plt.show()

plt.savefig("fig2.png")
plt.close(fig2)


#####################


file = open('tmp.bin', 'w')
file.write(str(arr_uniformly))
file.write('\n')
file.write(str(arr_gaussian))
file.close()

file = open('tmp.bin', 'r')
array_r = file.read()


arr_uniformly_r = array_r.split(']')[0][1::]
arr_gaussian_r = array_r.split(']')[1][2::]


arr_uniformly_ra = []
for i in re.findall(r'[\w.-]+', arr_uniformly_r):
	arr_uniformly_ra.append(float(i))

arr_gaussian_ra = []
for i in re.findall(r'[\w.-]+', arr_gaussian_r):
	arr_gaussian_ra.append(float(i))



# print("Here is the reading result!")
# print(arr_uniformly_ra)
# print(np.shape(arr_gaussian_ra))

fig1, ax = plt.subplots(figsize=(10,7))
 

x_uniformly = np.sort(arr_uniformly_ra)
  
# get the cdf values of y
y = np.arange(100) / 100.0
  
# plotting
plt.xlabel('x-axis')
plt.ylabel('y-axis')
  
plt.title('CDF using sorting the data')
  
ax.plot(x_uniformly, y, marker='o')
# print()
# quit()

ax2 = ax.twinx()

x_uniformly_2 = np.sort(arr_gaussian_ra)
y_2 = np.arange(np.min(arr_gaussian_ra), np.max(arr_gaussian_ra)) / 200.0

# ax2.xlabel('x-axis')
# ax2.ylabel('y-axis')
  
ax2.plot(x_uniformly, y, marker='o')

plt.show()
plt.savefig("fig3.png")