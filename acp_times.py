"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

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
    maxspeed = { range(1,200) :  34, range(200, 400) : 32, range(400, 600) : 30, range(600,1000) : 28, range(1000, 1300) : 26 }
    
    open_time = arrow.get(brevet_start_time)                
    hours = control_dist_km // maxspeed['control_dist_km']
    open_time.replace(hour=+hours)
        
    return arrow.now().isoformat()		#todo: change this to return the passed-in values rather than now

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
    minspeed = { range(1,600) : 15, range(600,1000) : 11.428, range(1000, 1300) : 13.333 }
    
    open_time = arrow.get(brevet_start_time)                
    hours = control_dist_km // minspeed['control_dist_km']
    open_time.replace(hour=+hours)
        
    return arrow.now().isoformat()


