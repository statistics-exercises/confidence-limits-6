import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_n_uniform_discrete(self) : 
        for n in range(2,4) : 
            for a in range(1,3) :
                for b in range(6,7) : 
                    mean = 0
                    for i in range(10) : 
                        var = n_uniform_discrete(n,a,b)
                        self.assertTrue( np.fabs( np.floor(var) - var)<1e-7, "your n_uniform_discrete function returns a number that is not an integer" )
                        self.assertTrue( var>=n*a and var<=n*b, "your n_uniform_discrete function returns that falls outside the required range" )
                        mean = mean + var
                    mean = mean / 10
                    var = n/12*( (b-a+1)*(b-a+1) - 1 )
                    bar = np.sqrt(var/10)*st.norm.ppf( (0.99 + 1) / 2 )
                    self.assertTrue( np.fabs( mean - n*0.5*(b+a) )<bar "your n_uniform_discrete function appears to be sampling from the wrong distribution" )
      
      def test_mean(self) : 
          for n in range(2,4) : 
             for a in range(1,3) :
                 for b in range(6,7) :
                     mean = sample_mean( 10, n, a, b )
                     var = n/12*( (b-a+1)*(b-a+1) - 1 )
                     bar = np.sqrt(var/10)*st.norm.ppf( (0.99 + 1) / 2 )
                     self.assertTrue( np.fabs( mean - n*0.5*(b+a) )<bar, "your mean function appears to be sampling from the wrong distribution" )
      
      def test_resampler(self) :
          lsamples, msamples, usamples = np.zeros(100), np.zeros(100), np.zeros(100 )
          for j in range(100) : 
              samples = np.zeros(100) 
              for i in range(100) : samples[i] = sample_mean(10,2,1,6)
              lsamples[j], msamples[j], usamples[j] = np.percentile( samples, 5), np.median(samples), np.percentile( samples, 95 )

          lll,mmm,uuu = resampling(90,100,10,2,1,6)
          self.assertTrue( np.percentile(lsamples,1)<=lll and lll<=np.percentile(lsamples, 99), "your percentiles function appears to not be working" )
          self.assertTrue( np.percentile(msamples,1)<=mmm and mmm<=np.percentile(msamples, 99), "your percentiles function appears to not be working" )
          self.assertTrue( np.percentile(usamples,1)<=uuu and uuu<=np.percentile(usamples, 99), "your percentiles function appears to not be working" )
