"""
this class contain all the information about departure flights
"""


class Flight_depart_information:
    def __init__(self, airline="", flight_num="", depart_to="", terminal="", schedule_time="", updated_time="",
                 counter="", status=""):
        self.counter = counter
        self.airline = airline
        self.flight_num = flight_num
        self.depart_to = depart_to
        self.terminal = terminal
        self.schedule_time = schedule_time
        self.updated_time = updated_time
        self.status = status
