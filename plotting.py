# Python Tutorial for Beginners: Episode 13 Plotting Graphs in Python with matplot

# importing relevant modules
import matplotlib.pyplot as plt

# # very basic plot
# x = [1, 3, 5, 10]
# plt.plot(x) # what we are plotting
# plt.show() # shows what we are plotting
#
# # plotting x and y against each other
# y = [7, 12, 21, 22] # must be same shape
# plt.plot(x, y)
# plt.show()

# plot a better looking plot
# line 1-- points
x = [3, 9, 14]
y = [2, 7, 30]
# plotting x and y
plt.plot(x, y, c = "red", linewidth = 2, label = "Line 1")

# line 2 -- points
x2 = [1, 15, 18]
y2 = [0, 3, 12]
# plotting x2 and y2
plt.plot(x2, y2,
         c = "green",
         linewidth = 2,
         label = "Line 2",
         linestyle = "dashed",
         marker = "o",
         markerfacecolor = "orange",
         markersize = 10)

# label the axes
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title ("Two Lines")

# setting axis limits
plt.ylim(1, 10)
plt.xlim(0, 30)

# show legend on plot
plt.legend()

# show plot
plt.show()