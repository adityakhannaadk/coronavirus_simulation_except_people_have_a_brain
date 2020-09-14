
from neural import hive
import dat_str as dsr

# Train neural network hive first time (the same neural network gets used for every mover hence hive mind)
xdata = [[100,1000,100],[150,800,200],[150,800,300]]
ydata = [0,1,1.5] 
def point(xlimit,ylimit):
    import random
    x = random.uniform(0,xlimit)
    y = random.uniform(0,ylimit)
    return x,y
def Generate(GrupSize,xlimit,ylimit):
    import pandas as pd
    import math
    df = pd.DataFrame(columns='X,Y,Covid-19,Day'.split(','))
    
    for i in range(GrupSize):
        df.loc[i,'X'], df.loc[i,'Y'] = point(xlimit,ylimit)
        df.loc[i,'Covid-19'] = False
    
    samplesize = math.floor(GrupSize/100)
    MoversList = df.sample(n = samplesize).index.values.tolist()
    
    StatofDay = pd.DataFrame(columns='Healthy,Covid-19(+),Hospitalized,Cured,Dead'.split(','))
    return df , StatofDay, MoversList
    
def plt1color(df):
    cols=[]
    for l in df.index:
        if df.loc[l,'Covid-19']==True: 
            cols.append('red')
        elif df.loc[l,'Covid-19']==666: 
            cols.append('black')
        elif df.loc[l,'Covid-19']==115: 
            cols.append('yellow')
        elif df.loc[l,'Covid-19']==7: 
            cols.append('green')
        else:
            cols.append('blue') 
    return cols
def plt2color(Stat):
    cols=[]
    for i in Stat.columns:
        if i=='Covid-19(+)': 
            cols.append('red')
        elif i=='Dead': 
            cols.append('black')
        elif i=='Hospitalized': 
            cols.append('yellow')
        elif i=='Cured': 
            cols.append('green')
        else:
            cols.append('blue') 
    return cols
def Plot():
    import matplotlib.pyplot as plt
    global df, fig, Stat, Day, Moverslist
    cols=plt1color(df)
    ld = ['Healthy','Covid-19(+)','Hospitalized','Cured','Death Toll']
    axs[0].cla()
    axs[0].scatter(df['X'],df['Y'],s=1,c=cols)
    for i in MoversList:
        axs[0].scatter(df.loc[i,'X'],df.loc[i,'Y'],s=6,facecolors='none', edgecolors='black')
        axs[0].text(df.loc[i,'X']+0.02, df.loc[i,'Y']+0.02, str(i), fontsize=5)
    cols=plt2color(Stat)
    sDay = str(Day)
    title = 'Day' + sDay
    axs[0].set_title(title,loc='left')
    axs[0].set_yticklabels([])
    axs[0].set_xticklabels([])
    axs[0].tick_params(
#    axis='both',       
    which='both',      
    bottom=False,      
    top=False,         
    right=False,      
    left=False,         
    labelbottom=False) 
    axs[1].cla()
    axs[1].plot(Stat.Healthy,label=ld[0],color=cols[0])
    axs[1].plot(Stat['Covid-19(+)'],label=ld[1],color=cols[1])
    axs[1].plot(Stat.Hospitalized,label=ld[2],color=cols[2])
    axs[1].plot(Stat.Cured,label=ld[3],color=cols[3])
    axs[1].plot(Stat.Dead,label=ld[4],color=cols[4])
#    axs[1].set_prop_cycle(color=cols)
    axs[1].legend(bbox_to_anchor=(0, 1), loc='upper left', borderaxespad=0.)
    plt.xlabel('Days')
    plt.show()
    if Day<10 : sDay = '0' + sDay
    title = 'Day' + sDay + '.png'
    plt.savefig(title)

def Png_to_gif():
    from PIL import Image
    import glob
    
    # Create frames
    frames = []
    imgs = glob.glob("*.png")
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)
        
    # Save into GIF
    frames[0].save('png_to_gif.gif', format='GIF',
          append_images=frames[1:],
          save_all=True,
          duration=500, loop=0)
def infect(Person):
    import random
    global df,Day
    if random.random()>0.25 and Day>3 : return
    if df.loc[Person,'Covid-19']==False:
        df.loc[Person,'Covid-19'], df.loc[Person,'Day'] = True, Day
    
    
def Move(xlimit,ylimit):
    """ 
    Move movers using neural network (Aditya Khanna)
    """
    v = dsr.strat_rad(hive.predict([List.count(666),List.count(True),List.count(115)]))
    xx = v[0]
    yy = v[1]
    global df, MoversList
    for i in MoversList:
        if (df.loc[i,'Covid-19']==115) or (df.loc[i,'Covid-19']==666) : MoversList.remove(i)
        df.loc[i,'X'], df.loc[i,'Y'] = (df.loc[i,'X']+,yy)%xlimit, (df.loc[i,'Y']+xx)%ylimit
def check(i,j):
    import math
    global df, YesterdayPatients, Distlimit
    Dist = math.sqrt((df.loc[i,'X']-df.loc[j,'X'])**2+(df.loc[i,'Y']-df.loc[j,'Y'])**2)
    flag = ((YesterdayPatients[i]==True) ^ (YesterdayPatients[j]==True)) and Dist<Distlimit
    return flag
    
def interact():
    global Day, df
    for i in range(len(df)):
        for j in range(i):
            if check(i,j):
                if (df.loc[i,'Covid-19']==False) :
                    infect(i)
                else:
                    infect(j)
def kill():
    import math
    global df
    
    samplesize = math.floor(len(df[df['Covid-19']==True])*.005+len(df[df['Covid-19']==115])*.005)
    if samplesize>len(df[df['Covid-19']==True]): return
    df.loc[df[df['Covid-19']==True].sample(n = samplesize).index.values.tolist(),'Covid-19']=666
    return
def hospitilize():
    import math
    global df
    samplesize = math.floor(len(df[df['Covid-19']==True])*0.03)
    if samplesize>len(df[df['Covid-19']==True]): return
    df.loc[df[df['Covid-19']==True].sample(n = samplesize).index.values.tolist(),'Covid-19']=115
    return
def cure():
    global df, Day
    df.loc[(df['Day']<Day-10) & (df['Covid-19']==True) ,'Covid-19'] = 7
    df.loc[(df['Day']<Day-21) & (df['Covid-19']==115) ,'Covid-19'] = 7
    return
    
    
def Tomorrow(): # To Be checked and Resolved!!!
    global df, Day
    Day +=1
    kill()
    hospitilize()
    cure()
    Move(xlimit,ylimit)
    interact()
def Count(Day):
    global df, Stat
    
    List = list(df['Covid-19'])
    
    Stat.loc[Day,'Healthy'] = List.count(False)
    Stat.loc[Day,'Covid-19(+)'] = List.count(True)    
    Stat.loc[Day,'Hospitalized'] = List.count(115)    
    Stat.loc[Day,'Cured'] = List.count(7)
    Stat.loc[Day,'Dead'] = List.count(666)
     
    return
    
def write_log(*args):
    global log_file
    line = ' '.join([str(a) for a in args])
    log_file.write(line+'\n')
    print(line)
    
# Main -------------------------------------------------------------------
import matplotlib.pyplot as plt
import random
log_file = open("Log.txt","w+")
# -------------------------------------------
#   I N P U T   V A R I A B L E S   H E R E  |
# -------------------------------------------
#                                            |
n = 1000    #                                |
xlimit,ylimit=30,30   #                      |
Distlimit = 1.5 #                            |
#                                            |
# -------------------------------------------
write_log(31*'-')
write_log("Here's the Input Data:")
write_log(8*'- - ') 
write_log('Numper of Sample:',n)
write_log('X & Y limites: ',xlimit,', ',ylimit)
write_log('Distance required for Contamination:', Distlimit)
# Day = 0,  Generating Model...
Day = 0
df, Stat, MoversList = Generate(n,xlimit,ylimit)
infect(random.randrange(n))
fig, axs = plt.subplots(2)
fig.suptitle('Covid-19 Epidemic Sample Model', fontsize=16)
Plot()
Count(Day)
write_log(31*'-')
write_log('Day:',Day)
write_log(8*'- - ')    
write_log(Stat.loc[Day])
# Day=1
YesterdayPatients = list(df['Covid-19'])
Tomorrow()
Plot()
Count(Day)
write_log(31*'-')
write_log('Day:',Day)
write_log(8*'- - ')    
write_log(Stat.loc[Day])
    
#Main Loop  .  .  .
countsames = 0
while Stat.loc[Day, 'Healthy']>0 and Day<100:
    log_file = open("Log.txt","a+")
    if (list(Stat.loc[Day])==list(Stat.loc[Day-1])): 
        countsames +=1
        if countsames>2 : break
    else :
        countsames = 0
    
    YesterdayPatients = list(df['Covid-19'])
    Tomorrow()
    Plot()
    Count(Day)
    write_log(31*'-')
    write_log('Day:',Day)
    write_log(8*'- - ')    
    write_log(Stat.loc[Day])
    log_file.close()
Png_to_gif()
Stat.to_excel('Stat.xlsx')
Stat.plot(title='Statistical Data Vs. Days Passed')
plt.savefig('Stat')
