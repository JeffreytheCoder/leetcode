# Create a google calender that finds avaliable timeslots for
# two people to meet based on each's existing meeting timeslots

# Input: 
# 1. two lists consisting lists of time range in strings ['start_time', 'end_time']
# 2. a list of time range in strings ['start_time', 'end_time']
# Output: a list consisting lists of time range in strings ['start_time', 'end_time']

schedule_A = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
schedule_B = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
schedule_C = [['12:30', '14:30'], ['14:30', '16:00'], ['18:00', '18:30']]

schedule_AB = [['9:00', '11:30'], ['12:00', '14:30'], ['14:30', '15:00'], ['16:00', '18:00']]
schedule_AC = [['9:00', '10:30'], ['12:00', '14:30'], ['14:30', '18:00'], ['18:00', '18:30']]

final_schedule_AB = [['11:30', '12:00'], ['15:00', '16:00']]

# Plan
# 1. merge existing meeting timeslots of two people
# 2. exclude to avaliable timeslots
# 3. compare to working hours range

# return a merged list of timeslots lists
def mergeSchedules(s1, s2):
    merged_s = []
    p1 = 0
    p2 = 0
    while (p1 != len(s1) and p2 != len(s2)):
        t1 = s1[p1]
        t2 = s2[p2]
        # if the start or end time is between the interval of the other timeslot, it can be merged
        if (compareTime(t1[0], t2[0]) >= 0 and compareTime(t1[0], t2[1]) <= 0
            or compareTime(t1[1], t2[0]) >= 0 and compareTime(t1[1], t2[1]) <= 0):
            merged_t = [t1[0] if compareTime(t1[0], t2[0]) <= 0 else t2[0], t1[1] if compareTime(t1[1], t2[1]) >= 0 else t2[1]]
            merged_s.append(merged_t) 
            p1 += 1
            p2 += 1 
        else:   # if corresponding timeslot can't be merged, add directly
            earlier_t = t1 if compareTime(t1[1], t2[0]) < 0 else t2
            merged_s.append(earlier_t)
            if earlier_t == t1:
                p1 += 1
            else:
                p2 += 1
            
    return merged_s

# return avaliable time except the merged time
def excludeTime(s):
    excluded_s = []
    for i in range(len(s)):
        if i != len(s) - 1 and s[i][1] != s[i+1][0]:
            excluded_s.append([s[i][1], s[i+1][0]])
    return excluded_s
        
# return 1 if time1 is later than time2, 0 if same, -1 if earlier
def compareTime(time1, time2):
    # calculate hours into minutes
    h1, m1 = time1.split(":")
    h2, m2 = time2.split(":")
    
    t1 = int(h1) * 60 + int(m1)
    t2 = int(h2) * 60 + int(m2)
    
    if (t1 > t2):
        return 1
    elif (t1 < t2):
        return -1
    else:
        return 0
    
def oldCompareTime(time1, time2):
    #24 hours: 00:00-23:59
    h1 = int(time1[0:2]) if int(time1[0]) == 1 else int(time1[0])
    m1 = int(time1[2:]) if h1 < 10 else int(time1[3:])
    h2 = int(time2[0:2]) if int(time2[0]) == 1 else int(time2[0])
    m2 = int(time2[2:]) if h2 < 10 else int(time2[3:])
    
    if (h1 == h2):
        if (m1 == m2):
            return 0
        elif (m1 > m2):
            return 1
        else:
            return -1
    elif (h1 > h2):
        return 1
    else:
        return -1
    
print(mergeSchedules(schedule_A, schedule_B))
print(schedule_AB)
print(excludeTime(mergeSchedules(schedule_A, schedule_B)))
print(final_schedule_AB)