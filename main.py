import matplotlib.pyplot as plt

def collatz_conjecture(num):
   num = int(input('Enter a number: '))
   sequence = [num]
   count = 1
   while(num != 1):
       if((num%2)==0):
           num = num // 2 
       else:
           num = (num*3) + 1
       sequence.append(num)
       count=count+1



   print(count)
   plt.plot(sequence)
   plt.ylabel('Collatz Sequence')
   plt.yscale('log')
   plt.show()

   return sequence

print(collatz_conjecture(1))