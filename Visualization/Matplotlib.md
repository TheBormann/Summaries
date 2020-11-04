# Matplotlib
In matplotlib every plot is in a container or grid, these are called **figures**. Plots in figures are stored in **axis**,
these can be customized, changed in size and in location in the figure. **Ticks** are the steps on the x-axis/ y-axis, the
x-axis/y-axis is called **spine**, to differentiate better.

## How to work with Matplotlib
Generally the workflow follows this pattern:
1. We need to define a figure, which is the container of any of your plots
    ```
    fig = plt.figure(figsize=(3,3))
    ```
2. Then we can add Axes/ subplots, which hold the actual plots 
    ```
    plt.subplot(2, 1, 1)
    plt.plot(X,Y)
    ```
3. Additionally we can add some configurations to the plot and axis
    ```
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    ```
4. Show / save the plot
    ```
    fig.savefig("../img/img.svg")
    plt.show()
    ```
5. Clear plot (necessary when reusing the )
    ```
    # clear axis
    fig.cla()
    # clear figure
    fig.clf()
    ```

Now Matplotlib offers shortcuts to speed up the process:

**Define figure and axis at once:**
```
fig, ax = plt.subplots(figsize=(3,3))
ax.plot(X, Y, lw=2)
plt.show()
```

**Shortest method:**
```
df.plot(kind="scatter", x=x_values, y=y_values)
plt.show()
```

## How to create multi-plot layouts
#### Horizontal
```
# create figure
plt.figure(figsize=(6, 3))
# add subplot
plt.subplot(1, 2, 1)
plt.text(0.5, 0.5, 'subplot(1,2,1)', ha='center', va='center')

plt.subplot(1, 2, 2))
plt.text(0.5, 0.5, 'subplot(1,2,2)', ha='center', va='center')
```
![Horizontal layout](./img/horizontal-layout.svg "Horizontal layout")
#### Vertical
```
# create figure
plt.figure(figsize=(3, 6))
# add subplot
plt.subplot(2, 1, 1)
plt.text(0.5, 0.5, 'subplot(2,1,1)', ha='center', va='center')

plt.subplot(2, 1, 2)
plt.text(0.5, 0.5, 'subplot(2,1,2)', ha='center', va='center')
```
![Vertical Layout](./img/vertical-layout.svg "Vertical layout") 
#### Advanced
The subplot function works like this, subplot(nrows, ncols, index). every plot needs at least 2 rows to be displayed
```
fig = plt.figure()
#  subplot(nrows, ncols, index), define rows, columns of grid and where it is
plt.subplot(4, 1, 1)

plt.subplot(4, 1, 2)

plt.subplot(2, 3, 4)

plt.subplot(2, 3, 5)

plt.subplot(2, 3, 6)

```
![Custom layout](./img/advanced-layout.svg "Custom layout")
 
## Different plots and elements in matplotlib
| Img  |  Kind (and Parameters) | Description  |
|---|---|---|
| ![Line Plot](./img/line-plot.svg "Line Plot") | plot() <br><br> \[X], **Y**,, label, fmt, color, marker, linestyle | Used for change over time |
| ![Scatter Plot](./img/scatter-plot.svg "Scatter Plot") | scatter() <br><br> **X**, **Y**, s(izes), c(olors), markers, cmap| Best to compare two features |
| ![Bar Plot](./img/bar-plot.svg "Bar Plot") | bar\[h]() <br><br> **x**, **height**, width, bottom, align, color | barh rotates the plot |
| ![Histogram Plot](./img/hist-plot.svg "Histogram Plot") | hist <br><br>  **X**, bins, range, density, weights | Used to see value distribution |
| ![Box Plot](./img/box-plot.svg "Box Plot") | boxplot() <br><br> **X**, notch, sym, bootstrap, widths  | Boxplot shows outliers better |
| ![Violin Plot](./img/violin-plot.svg "Violin Plot") | violinplot() <br><br> **X**, **Y**, fmt, color, marker, where | An alternative to Boxplot |
| ![Contour Plot](./img/contour-plot.svg "Contour Plot") | contour\[f]() <br><br> \[X], \[Y], **Z**, levels, colors, extent, origin | Visualizes values in an 2d array |
| ![Hex Plot](./img/hex-plot.svg "Hex Plot") | hexbin() <br><br> **X**, **Y**, C, gridsize, bins  | Like a scatter plot, but hexagonals are buckets for values |
| ![Step Plot](./img/step-plot.svg "Step Plot") | step() <br><br> **X**, **Y**, \[fmt], color, marker, where | Different format of plot() with no transition |
| ![Error Plot](./img/error-plot.svg "Error Plot") | errorbar() <br><br> **X**, **Y**, xerr, yerr, fmt  | Adds error bars to plot(), <br>to show how accurate values are |
| ![Barbs Plot](./img/barbs-plot.svg "Barbs Plot") | barbs() <br><br> \[X], \[Y], **U**, **V**, C, length, pivot, sizes | It's used to plot any two dimensional vector quantity |
| ![Event Plot](./img/event-plot.svg "Event Plot") | eventplot() <br><br> **positions**, orientation, lineoffsets | t's useful where you need to show <br> timing or position of multiple sets of discrete events. |
| ![XCorr Plot](./img/xcorr-plot.svg "XCorr Plot") | xcorr() <br><br> **X**, **Y**, normed, detrend | Plots the cross correlation between x and y |
| ![Imshow Plot](./img/imshow.svg "Imshow Plot") | imshow() <br><br> **Z**, \[cmap], interpolation, extent, origin | Displays images, or values of an 2d array |
| ![3D Plot](./img/3D-plot.svg "3D Plot") | plot_surface() <br><br> **X, Y, Z** (2d arrays) <br><br> color, cmap, shade| Best to compare two features |
| ![Pie Plot](./img/pie-plot.svg "pie Plot") | pie() <br><br>  **Z**, \[explode], labels, colors, radius  | Creates a piechart |
| ![Text Plot](./img/text-plot.svg "Text Plot") | text() <br><br> **x**, **y**, **text**, va, ha, size, weight | Adds text to plot at specific coordinates |
| ![Quiever Plot](./img/quiver-plot.svg "Quiever Plot") | quiver() <br><br> \[X], \[Y], **U**, **V**, C, units, angles | Adds arrows |
| ![Fill Plot](./img/fill-plot.svg "Fill Plot") | fill\[_between]\[x]() <br><br> **X**, Y1, Y2, color, where | fills area between values |

##### Implementations are found [here](./code/matplotlib.ipynb) 

## Most important customizations
First let's have a deeper look into the anatomy of a figure:
![Anatomy of figure](./img/4xjiuc5k.bmp "Anatomy of figure")
As you can see, there are a lot of different parts at play to build a graph. We will only focus the most important ones:
```
# Set Title
plt.title("My Title")

# Change label of axis
plt.ylabel("My Y Label") ; plt.xlabel("My X Label")

# Change the axis values (ticks)
plt.yticks(range(1,10)) ; plt.xticks([0,2,4,6,8],
                            ['0', '2B', '4B', '6B', '8B'])

# Change range of an Axis (first 2 values are min and max for x-axis, last 2 for y-axis)
plt.axis([-5, 105, 0, 5])

# add/ customize legend
plt.legend(loc=9)
```


#### Next up [Seaborn](./Seaborn.md)

## References
* https://matplotlib.org/
* http://scipy-lectures.org/intro/matplotlib/auto_examples/
* https://github.com/matplotlib/cheatsheets