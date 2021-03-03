# What is Pandashack
Pandashack is a small project which tries to extend pandas with functionality
helpful for pandas method chaining api. 

In general method chaining helps to create readable pipelines in pandas, 
but it has its weak points. One of these is the `.assign` method, which 
assumes that users are comfortable writing lambda expressions and creates 
very long lines of code. The first thing pandashack has implemented is a 
`mutate` method, similar to `mutate` in dplyr (R). This `mutate` method makes 
computing and assigning new columns very easy and is also applicable to 
grouped DataFrames. 

Furthermore, pandashack can be seen as an 
example how to extend the pandas ecosystem with custom functionality.

# Usage

First we do some setup:
```python
from seaborn import load_dataset # to get the iris dataset
import pandashack # automatically extends pandas

df_iris = load_dataset('iris')
```

Now we will try the simplest use case: 
We want to create a column called `new_col`, by computing it using the mean
of the  `sepal_length` column and adding it to each value 
of the `petal_width` column. This is how you would do this:

```python

df_iris.mutate(new_col='sepal_length.mean() + petal_width')

```

While this was a very simple example this syntax allows us to do much more.
We can use it together with any other pandas method which is compatible 
with the chaining api. For example we could compute the same `new_col`, but 
only for the subset of our data where `species` is equal to `"setosa"`. 
Then we only show the first 5 values of this new DataFrame:

```python
(df_iris
  .query('species == "setosa"') # filtering with a normal pandas method
  .mutate(new_col='sepal_length.mean() + petal_width')
  .head() # showing first 5 values with normal pandas method
)

```
Even better in contrast to the `assign` method `mutate` also works natively 
with pandas groupby objects.

Here, we groupby `species` before using the `mutate` method.
In other words we group the DataFrame by species and then compute the `mean`
of the `sepal_length` for each group separately and then add the 
`petal_length`.

```python
(df_iris
  .groupby('species') # normal groupby statement
  .mutate(new='sepal_length.mean() + petal_width')
)
```

# Installation 
Currently, you can only install pandashack using this repo.
You can follow this instruction in your terminal to do so:
* `git clone https://github.com/samihamdan/pandashack.git`
* `cd pandashack`
* `pip install -r requirements.txt`
* `pip install .`

    
