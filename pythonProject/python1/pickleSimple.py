import pickle #pickle 腌制，泡

d1 = {
    'a':[99,56],
    'b':(1,2,2,3),
    'c':{1,2,3}
}
l1 = [1,2,3]
l1.append(l1)

with open('fileOperate/pickleFile.txt','wb+') as pf:
    pickle.dump(d1,pf)
    pickle.dump(l1,pf,-1)
    pf.close()
f2 = open('fileOperate/pickleFile.txt','rb')
print(f2.readlines())
