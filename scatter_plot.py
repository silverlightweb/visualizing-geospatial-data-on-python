#You'll using plt.scatter() to plot the father and son height in data
import matplotlib.pyplot as plt
#scatter plot 1
#color darked
#marker = 's'
plt.scatter(father_son.fheight,father_son.sheight,c='darked',marker='s')
plt.show()

#scatter plot 2
#edgecolor = 'darkblue'
#c = yellow
plt.scatter(father_son.fheight,father_son.sheight,c='yellow',edgecolor='darkblue')
plt.show()
#Add gridlines and axes label to my scatterplot
#Enter the plot title equal 'Son Height as a Function of Father Height'
#scatter plot 3
plt.scatter(father_son.fheight,father_son.sheight,c='yellow',edgecolor='darkblue')
plt.grid()
plt.xlabel('father height (inches)' )
plt.ylabel( 'son height (inches)')
plt.title('Son Height as a Function of Father Height')

# Show your plot
plt.show()