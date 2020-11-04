# Data visualtization

In this directory everything is a summary about different plotting methods and when it's best to use 
which.

### Covered Visualization libraries:
* [Matplotlib](Matplotlib.md)
* [Seaborn](Seaborn.md)
* [Plotly](Plotly.md)

## When should you use which? 
**Matplotlib** is the most commonly used plotting library with a lot of flexibility, but it lacks a visually appealing 
design and has no interactivity.

**Seaborn** is build on top of Matplotlib, enhances the style of plots  and simplifies the plot creation a bit, but 
with that it lacks some configuration capabilities Matplotlib has.

**Plotly** is a visually beautiful interactive plotting library which also can run directly in your jupiter notebook.
While it is harder to create plots with it, these plots are production ready and can instantly turned into interactive 
plots online.

**To summarize**, when you need to understand the dataset or the ML-algorithm then interactivity isn't really needed.
In this cases Matplotlib and Seaborn are perfect, because you can create plots easily and fast.
If you want to present you findings to the world then Plotly is perfect, because it gives people that aren't involved 
in the development a more indepth look into your project.
