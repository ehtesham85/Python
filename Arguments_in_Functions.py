#       Default Arguments
def average(a=9, b=1):
   print("The Average is : ",(a+b)/2)
# average(4,6)
# average(b=9)


#       Keyword Arguments
def name(fname,mname="Ali",lname="jutt"):
    print("Hello ",fname,mname,lname)
# name("Ehtesham","Wahla","Jutt")


#       Average of Tuple-Numbers
def average(*numbers):
   sum=0;
   for i in numbers:
     sum=sum+i
   print("Average : ",sum/len(numbers))
# average(5,6)


#       Return value from Function
def Average(*numbers):
   sum=0
   for i in numbers:
       sum=sum+i
   return sum/len(numbers)
c=average(5,6,7,1)
print(c)


