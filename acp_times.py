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
    #TODO: fix time zone stuff, introduce actual logic for adding hours/minutes
    #perhaps a bunch of mod ops, where days = hours %24, or somethings
    if control_dist_km > brevet_dist_km:	 #error case, if the checkpoint distance is invalid
        return arrow.now().isoformat()           #get better feedback though

    opT = [range(1,200), range(200,400), range(400, 600), range(600, 1000), range(1000,1300)]
    speedVals = [34,32,30,28,26]
    max_speed = 0    

    for item in opT:
        if control_dist_km in item:
            max_speed = speedVals[opT.index(item)]
    print("max speed is " + str(max_speed))
    print(brevet_start_time())

    open_time = control_dist_km // max_speed
    print("Thus the checkpoint opens in " + str(open_time) + " hours")
    start_time = arrow.get(brevet_start_time())
    start_time = start_time.replace(hour=+open_time)

    print("Start time is: " + str(start_time))

    #no matter what it's shifting the date 8 hours BACkwards

    return start_time.isoformat()		#todo: change this to return the passed-in values rather than now

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
    if control_dist_km > brevet_dist_km:
        return arrow.now().isoformat()

    cloT = [range(1,600), range(600, 1000), range(1000,1300)]
    speedVals = [15, 11.428, 13.333]
    min_speed = 0    

    for item in cloT:
        if control_dist_km in item:
            min_speed = speedVals[cloT.index(item)]

    close_time = control_dist_km // min_speed
    end_time = arrow.get(brevet_start_time()).replace(hour=+close_time)


    return end_time.isoformat()























