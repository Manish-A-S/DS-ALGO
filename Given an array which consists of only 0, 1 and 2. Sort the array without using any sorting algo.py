Inplace(Excess time)

def sort012(self,arr,n):
        i=0
        one=0
        while i<n:
            if arr[i]==2:
                arr.pop(i)
                arr.append(2)
                n-=1
                continue
                
            if arr[i]==0:
                arr.pop(i)
                arr.insert(0,0)
                i+=2
                continue
                
            if arr[i]==1:
                arr.pop(i)
                one+=1
                n-=1
                
            i+=1
        
        for i in range(n):
            if arr[i]==2:
                break
        for j in range(one):
            arr.insert(i,1)



Proper working

def sort012(self,arr,n):
        zero=[]
        one=[]
        two=[]
        for i in arr:
            if i==0:
                zero.append(i)
            elif i==1:
                one.append(i)
            else:
                two.append(i)
        res=zero+one+two
        arr[:]=res[:]
        return arr
        

For Input: 
8
2 1 0 1 2 1 2 0
Your Output: 
0 0 1 1 1 2 2 2




