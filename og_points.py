mp,w,d,l,pt=map(int,input().split())
# goal to finf the points of the team 
# we can do it by looping through all the possible values of wins and draws
og_pt=0
og_win=0
og_loss=0
og_draw=0
total=0

sum=0
arr=[mp,w,d,l,pt]
for i in range(len(arr)):
    for j in range(len(arr)):
        
        sum=arr[i]*3+arr[j]
        
        for k in range(len(arr)):
            
            if sum==arr[k]:
                og_loss=arr[j]
                og_win=arr[i]
                og_pt=arr[k]
                break
arr.remove(og_win)
arr.remove(og_loss)
arr.remove(og_pt)
mp=max(arr)
arr.remove(mp)
og_draw=arr[0]
print(mp,og_win,og_loss,og_draw,og_pt)
            
        
