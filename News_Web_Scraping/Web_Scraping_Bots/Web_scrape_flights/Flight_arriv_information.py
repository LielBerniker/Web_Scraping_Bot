"""
this class contain all the information about arrival flights
"""


class Flight_arriv_information:
    def __init__(self, airline="", flight_num="", land_from="", terminal="", schedule_time="", updated_time="",
                 status=""):
        self.airline = airline
        self.flight_num = flight_num
        self.land_from = land_from
        self.terminal = terminal
        self.schedule_time = schedule_time
        self.updated_time = updated_time
        self.status = status
