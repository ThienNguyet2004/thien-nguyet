sodien=int(input())
if (0<=sodien<=50):
    giatien=sodien*1678
    print(giatien)
elif (51<=sodien<=100):
    giatien=50*1678+(sodien-50)*1734
    print(giatien)
elif (101<=sodien<=200):
    giatien=50*1678+50*1734+(sodien-100)*2014
    print(giatien)
elif (201<=sodien<=300):
    giatien=50*1678+50*1734+100*2014+(sodien-200)*2536
    print(giatien)
elif (301<=sodien<=400):
    giatien=50*1678+50*1734+100*2014+100*2536+(sodien-300)*2834
    print(giatien)
else :
    giatien=50*1678+50*1734+100*2014+100*2536+100*2834+(sodien-400)*2927
    print(giatien)