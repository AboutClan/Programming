t = int(input())

for i in range(t):
    ps = input()     
    count = 0     

    for ch in ps:    
        if ch == '(':         
            count = count + 1
        else:               
            count = count - 1

        if count < 0:        
            break           
          
    if count == 0:
        print("YES")
    else:
        print("NO")
