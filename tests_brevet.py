###
#Various nose tests. Pretty basic checks, should be thorough enough
###
import acp_times as brevet
import arrow
import dateutil


def test_right_times():      #checks if opening and closing times are correct
    date = arrow.get('2017-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert brevet.open_time(930, 1000, date) == (date.replace(days=+1, hours=+6, minutes=+35)).isoformat()
    assert brevet.close_time(930, 1000, date) == (date.replace(days=+2, hours=+20, minutes=+52)).isoformat()
    
    assert brevet.open_time(700, 1000, date) == (date.replace(hours=+22, minutes=+22)).isoformat()
    assert brevet.close_time(700, 1000, date) == (date.replace(days=+2, minutes=+45)).isoformat()
    
    assert brevet.open_time(120, 200, date) == (date.replace(hours=+3, minutes=+31)).isoformat()
    assert brevet.close_time(120, 200, date) == (date.replace(hours=+8)).isoformat()    

def test_date_extend():      #checks if the +20% rule works for various dates
    date = arrow.get('2017-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss').isoformat()
    assert brevet.open_time(1000, 1000, date) == brevet.open_time(1200, 1000, date)
    assert brevet.open_time(650, 600, date) == brevet.open_time(700, 600, date)
    assert brevet.open_time(240, 200, date) == brevet.open_time(210, 200, date)

def test_bad_dist():          #checks if distance is beyond the 20% rule or otherwise invalid
    date = arrow.get('2017-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss')
    assert brevet.open_time(500, 200, date) == None
    assert brevet.open_time(1201, 1000, date) == None
    assert brevet.open_time(-40, 200, date) == None
    assert brevet.open_time(-220, 200, date) == None
    
    
    
    