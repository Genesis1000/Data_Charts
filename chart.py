# Import numpy as np
import numpy as np
import matplotlib.pyplot as plt
gdp_cap=['1000','2000','3000','5000']
life_exp=['5.9','7.5','10.45','50.9']
pop=['20000','34200','10000','19999']
# Store pop as a numpy array: np_pop
np_pop=np.array(pop)

# Double np_pop
#np_pop=np_pop*2

# Update: set s argument to np_pop
plt.plot(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.yticks([0,1, 2,3,5],['0','1k', '2k', '3k','5k'])

# Display the plot
plt.show()
