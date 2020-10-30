# Presenting results from resampling

Now that we understand how the sample mean given by the expression below can be resampled let's discuss how we might present the results from simulations where we are calculating this quantity.

![](https://render.githubusercontent.com/render/math?math=\overline{Y}=\frac{1}{m}\sum_{i=1}^{m}\sum_{j=1}^{n}X_{ij})

where each of ![](https://render.githubusercontent.com/render/math?math=X_{ij}) in this expression is a uniform discrete random that is greater than or equal to a and less than or equal to b.

In presenting our result we would run the code to generate the ![](https://render.githubusercontent.com/render/math?math=\overline{Y}) value multiple times because the output from a single simulation is a random variable.  To make our results reproducible we thus need multiple estimates of this quantity as we are not trying to calculate the value of this quantity.   We are instead trying to characterise the distribution that this (random) value is sampled from.  Just as we have seen for data sets our final statement about our results is going to read something like:

_100 values for Ybar were generated.  p% of these values were between l and u._

We are not going to write that we found that the average value was ![](https://render.githubusercontent.com/render/math?math=\overline{Y}) because any average we calculate is random.

Your task in this exercise is to use everything that you have learned thus far to write the code to generate a statement like this.  Just as we have in previous exercises we are going to perform this exercise for the random variable defined by the formula above.  You will thus need to copy your code for the three familiar functions below:  

1. `uniform_discrete` - takes two arguments `a` and `b` in input.  It should return a uniform discrete random variable that is greater than or equal to `a` and less than or equal to `b`.
2. `n_uniform_discrete` - takes three arguments `n`, `a` and `b`.  It should return the sum of `n` uniform discrete random variables that are greater than or equal to `a` and less than or equal to `b`.  Notice that you can call `uniform_discrete` in this function.
3. `sample_mean` - takes four arguments in input `m`, `n`, `a` and `b`.  It should generate `m` sums of `n` uniform discrete random variables that are greater than or equal to `a` and less than or equal to `b`.  It then should calculate a sample mean from these `m` random variables.  In other words, this function should return a random variable that is generated using the formula on this page.  Please note that you may want to include calls to `n_uniform_discrete` in this function.

You then need to write one additional function called resmpling.  This function takes 6 arguments: `conf`, `samples`, `m`, `n`, `a` and `b`.  Within this function, you will need to call `sample_mean` `nsamples` times.  This will generate `nsamples` random variables using the expression for ![](https://render.githubusercontent.com/render/math?math=\overline{Y}) above.  When you make these calls you will use the input arguments `m`, `n`, `a` and `b` when calling `sample_mean`.  The nsamples variables that you generate by calling `sample_mean` should be stored in a NumPy array as you will need to set the variable called `mmm` to the median from this set of random variables.  The variables `lll` and `uuu`, meanwhile, should be set equal to the upper and lower bounds of a `conf` % confidence limit on the data.

When your functions are complete they are used to perform a simulation of rolling two dice.  If you look at the description of this experiment in the code on the left it will help you to make sense of the task you have to complete.  
