import Image
import math
import operator



h1 = Image.open("img1.png").histogram()
h2 = Image.open("img3.png").histogram()
#def  
rms = math.sqrt(reduce(operator.add,
	map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
print(rms)