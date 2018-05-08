
# Matplotlib & panda visualization

# REFERENCE: https://matplotlib.org/gallery

import matplotlib.pyplot as pyplot

# plt.show() in juypter matplotlib inline


import numpy as np 

# data sample
x = np.linspace(0,5,11)
y = x **2

# functional
plt.plot(x,y, 'r+')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

numRows = 1
numColums=3
plotNumber=1
plt.subplot(numRows, numColums,plotNumber)
plt.plot(x,y,'r*')

numRows = 2
numColums=2
plotNumber2

plt.subplot(numRows, numColums,plotNumber)
plt.plot(y,x,'b+')

plt.show()

# object oriented
#a canvas
fig = plt.figure()

# left, bottom , width, height
# THINK OF PERCENTAGE POINTS
axis = fig.add_axes([0.2,0.2,0.5,0.5])

# now plot
axis.plot(x,y)
axis.set_xlabel('x axis')
axis.set_ylabel('y axis')
axis.set_title('Title')
plt.show()

# part II

fig = plt.figure()
axis1 = fig.add_axes([0.1,0.1,0.8,0.8])
axis2 = fig.add_axes([0.2,0.5,0.4,0.3])
axis1.plot(x,y)
axis2.plot(y,x)
plt.show()


# part III

fig,axes = plt.subplots(nrows=1,ncols=2)
plt.tight_layout()
for axis in axes:
	axis.plot(x,y)

# or
# axes[0].plot(x,y)
# axes[0].set_title('')
# axes[1].plot(y,x)
# axes[1].set_title('')
# plt.tight_layout()
plt.show()


# figure size dpi ( dots per inch)
fig = plt.figure(figsize=(3,2), dpi=100)

axis = fig.add_axes([0,0,1,1])
axis.plot(x,y)
plt.tight_layout()
plt.show()

# or 

fig, axis = plt.subplots(nrows=2, ncols=1, figsize=(8,2), dpi=100)
axis[0].plot(x,y)
axis[1].plot(y,x)
plt.tight_layout()
plt.show()

# saving figures to file as a jpen, png, 
# post script PS, Encapsulated Post Script EPS, scalable vector graphics SVG
# Portable Document Format PDF

fig.savefig('myPicture.png', dpi=200)

# multi plot same canvas with legend

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
ax.plot(x,y, label='XY')
ax.plot(x,y**2, label='xy^2')
ax.legend(loc=0) # or a tuple of coordinates x,y
plt.tight_layout()
plt.show()



# setting colors

fig = plt.figure()
axis = fig.add_axes([0,0,1,1])

# color is ccs like RGB or basic color names
# linewidth or lw
# alpha is transparency
# linestyle 
axis.plot(x,y,color='purple', lw=2, alpha=0.5, linestyle='-*')

plt.tight_layout()
plt.show()

# markers for a few points in the array

axis.plot(x,y,color='purple', lw=2, alpha=0.5, linestyle='-*', marker='M', markersize=3, markerfacecolor='yellow')

plt.tight_layout()
plt.show()



# focus into a part of the line

axis.plot(x,y,color='purple', lw=2, alpha=0.5, linestyle='-*')
axis.set_xlim([0,1])
axis.set_ylim([0,2])
plt.tight_layout()
plt.show()


# data frame matplotlib capabilities

# read in a csv time series

#df['C2'].plot.hist(bins=30)
#df.plot.area(alpha=0.5)
#df.plot.bar(stacked=True)
# marker, linewidth
# df.plot.line(x=df1.index, y='C3')

# 3d x,y,color
#df1.plot.scatter(x='A', y='B', c='C')
# 3d x,y C relativity
#df1.plot.scatter(x='A', y='B', s=df1['C']*3)

#df2.plot.box()
#df.plot.hexbin(x='a',y='b', gridsize=25, cmap="coolwarm")

# kernel density estimation
#df2['a'].plot.kde()
#df2['a'].plot.density()
















