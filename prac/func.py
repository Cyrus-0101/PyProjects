def minsToHrs(secs, mins = 60):
    hrs = mins / 60 + secs / 3600
    return hrs
    
print(minsToHrs(1500))

def secsToHrs(secs):
    hrs = secs / 3600
    return hrs
    
print(secsToHrs(12000))
