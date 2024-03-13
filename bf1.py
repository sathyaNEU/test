str = "aabbaabb"
super_done=-1
for i in range(0,len(str)):
    done = -1
    prefix = str[:i+1]
    tmp = prefix
    while(prefix!=str):
        prefix = prefix+tmp
        if(prefix==str):
            done=1
        if(len(prefix)>len(str)):
            break
    if(done==1):
        super_done=1
        print("prefix "+tmp + " does works") 
if(super_done==-1):
    print("no solution")

