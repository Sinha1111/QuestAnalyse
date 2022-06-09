from scipy import stats
import pandas as pd
alpha = 0.05
first_test =pd.DataFrame([23, 20, 19, 21, 18, 20, 18, 17, 23, 16, 19])
second_test=pd.DataFrame([24, 19, 22, 18, 20, 22, 20, 20, 23, 20, 18])



t_value,p_value=stats.ttest_rel(first_test,second_test)

one_tailed_p_value=float("{:.6f}".format(p_value/2)) 


print('Test statistic is %f'%float("{:.6f}".format(t_value)))

print('p-value for one_tailed_test is %f'%one_tailed_p_value)

alpha = 0.05

if one_tailed_p_value<=alpha:

    print('Conclusion','n','Since p-value(=%f)'%one_tailed_p_value,'<','alpha(=%.2f)'%alpha,'''We reject the hypothesis that file 1 is better than file 2. 

So we conclude that file 2 is better. i.e., d = 0 at %.2f level of significance.'''%alpha)

else:

    print('Conclusion','n','Since p-value(=%f)'%one_tailed_p_value,'>','alpha(=%.2f)'%alpha,'''We do not reject the hypothesis that file 1 is better than file 2. 

So we conclude that file 1 is better. i.e., d = 0 at %.2f level of significance.'''%alpha)