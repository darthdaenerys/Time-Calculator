def add_time(start, duration, current_day=None):
    starthour,temp=start.split(':')
    startmin,ampm=temp.split(' ')
    durationhour,durationmin=duration.split(':')
    starthour,startmin=int(starthour),int(startmin)
    durationhour,durationmin=int(durationhour),int(durationmin)
    durationmin+=60*durationhour
    dayspassed=0
    startmin+=durationmin
    while(startmin>=60):
        startmin-=60
        starthour+=1
        if starthour==13:
            starthour=1
        if ampm=='AM' and starthour==12:
            ampm='PM'
        elif starthour==12:
            ampm='AM'
            dayspassed+=1
            if current_day:
                if current_day.lower()=='monday':
                    current_day='Tuesday'
                elif current_day.lower()=='tuesday':
                    current_day='Wednesday'
                elif current_day.lower()=='wednesday':
                    current_day='Thrusday'
                elif current_day.lower()=='thrusday':
                    current_day='Friday'
                elif current_day.lower()=='friday':
                    current_day='Saturday'
                elif current_day.lower()=='saturday':
                    current_day='Sunday'
                else:
                    current_day='Monday'

    if str(startmin).__len__()==1:
        new_time=f'{str(starthour)}:0{str(startmin)} {ampm}'
    else:
        new_time=f'{str(starthour)}:{str(startmin)} {ampm}'
    if current_day:
        new_time+=f', {current_day}'
    if dayspassed>0:
        if dayspassed==1:
            new_time+=f' (next day)'
        else:
            new_time+=f' ({str(dayspassed)} days later)'
    return new_time
