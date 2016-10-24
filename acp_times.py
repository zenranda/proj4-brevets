"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import dateutil

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments. 
#


def open_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    if control_dist_km > (brevet_dist_km * 1.2):	                #error case, if the checkpoint distance is too far
        print("Error: controle distance > brevet distance + 20%.")  #this clause comes from the official time calculator
        return None

    if brevet_dist_km < control_dist_km < (brevet_dist_km *1.2):    #controles a little past the overall distance are counted as being on that distance
        control_dist_km = brevet_dist_km

    if control_dist_km < 0:
        print("Error: negative controle distance.")
        return None
        
    s = control_dist_km    
    threshhold = 0
    hours = 0
    vals = [[34, 200],[32, 200], [30, 200], [28, 400], [26, 300]]#indices are [max speed, distance max speed is applicable]

    while s > 0:                                                 #method for calculating open time
        if s > vals[threshhold][1]:                              #in short, it takes the first 200 km and divides them by the max speed
            s -= vals[threshhold][1]                             #then it takes those hours and adds them to an overall hour count
            hours += vals[threshhold][1]/(vals[threshhold][0])   #then it moves to the next max speed/distance threshold and repeats
            threshhold += 1                                      #this is because each chunk of the distance has its own max speed
        else:                                                    #and we need to concatenate the distance we travel per chunk/that chunk's max speed
            hours += s/(vals[threshhold][0])
            s = 0

    mins = hours * 60                                            #gets minutes from the final hour count
    hrs = 0                                                      #then converts them back into hours + remainder minutes
    while mins >= 60:
        hrs += 1
        mins = mins - 60
    mins = mins // 1
    
    start_time = arrow.get(brevet_start_time())
    start_time = start_time.replace(hours=+hrs)
    start_time = start_time.replace(minutes=+mins)

    return start_time.isoformat()


def close_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    if control_dist_km > (brevet_dist_km * 1.2):	                #error case, if the checkpoint distance is too far
        return None

    if brevet_dist_km < control_dist_km < (brevet_dist_km *1.2):
        control_dist_km = brevet_dist_km

    if control_dist_km < 0:
        return None
 
    s = control_dist_km
    hours = 0    
    threshhold = 0
    vals = [[15, 600],[11.428, 400], [13.333, 300]]

    while s > 0:                                                    #method for getting open time
        if s > vals[threshhold][1]:                                 #logic the same as open_time()
            s -= vals[threshhold][1]                                #only real difference is closing times have fewer, larger chunks
            hours += vals[threshhold][1]/(vals[threshhold][0])
            threshhold += 1
        else:
            hours += s/(vals[threshhold][0])
            s = 0

    mins = hours * 60
    hrs = 0
    while mins >= 60:
        hrs += 1
        mins = mins - 60
    mins = mins // 1

    end_time = arrow.get(brevet_start_time())
    end_time = end_time.replace(hours=+hrs)
    end_time = end_time.replace(minutes=+mins)

    return end_time.isoformat()





