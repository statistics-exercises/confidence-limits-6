import numpy as np

def uniform_discrete(a,b) :
  # Your code to generate the uniform discrete random variable goes here
  
  
def n_uniform_discrete( n, a, b ) : 
  # You code to generate the sum of n uniform discrete random variables goes here
  
  
def sample_mean( m, n, a, b ) : 
  # Your code to calculate the mean of m sums of n uniform discrete random variables
  # goes here


def resampling( conf, nsamples, m, n, a, b ) : 
  # Your code to generate the resamples and to compute the median and percentiles goes here 
  lll, mmm, uuu = 0, 0, 0 
  return lll, mmm, uuu
  

# The code from here should not need to be modified
# this will output the results
lower, median, upper = resampling( 90, 200, 50, 2, 1, 6 )
print("An experiment was performed in which two dice were rolled 50 times and the average score was computed")
print("This experiment was repeated 200 times and 90% of the means obtained were between", lower, "and", upper )
print("The median score was", median )
