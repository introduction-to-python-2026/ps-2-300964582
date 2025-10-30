def find_max_number(num1, num2, num3):
    
 if num1 > num2 :
    if num1 > num3 :
       return num1
    else:
      return num3
 else: 
   if num2 > num3:
     return num2
   else:
    return num3 

def find_mean(num1, num2, num3):
    mean = ( num1+ num2 + num3)/3
    return mean 

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    sigma=  (((num1- mean) + (num2- mean) +(num3-mean))/ 3 ) ** 0.5
    return mean, sigma
