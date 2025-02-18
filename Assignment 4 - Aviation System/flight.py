from Airport import Airport


class Flight:
    def __init__(self, flightNo, origAirport, destAirport):
        # Check that both origAirport and destAirport are Airport objects
        if not isinstance(origAirport, Airport) or not isinstance(destAirport, Airport):
            raise TypeError("The origin and destination must be Airport objects")
        # Check that flightNo is the correct format
        if not isinstance(flightNo, str):
            raise TypeError("The flight number format is incorrect")
        if len(flightNo) != 6 or not flightNo[:3].isalpha() or not flightNo[3:].isdigit():
            raise TypeError("The flight number format is incorrect")
        self._flightNo = flightNo
        self._origin = origAirport
        self._destination = destAirport

    def __repr__(self):
        # Get the cities
        orig_code = self._origin.getCode()
        dest_code = self._destination.getCode()
        # Check whether it's domestic or international
        if self.isDomesticFlight():
            flight_type = " [domestic]"
        else:
            flight_type = " [international]"
        return f"Flight({self._flightNo}): {orig_code} -> {dest_code} {flight_type}"

    def __eq__(self, other):
        # Returns True is self and other flights are considered the same flight
        if not isinstance(other, Flight):
            return False
        return self._origin == other._origin and self._destination == other._destination

    def getFlightNumber(self):
        # Getter that returns the Flight number string code
        return self._flightNo

    def getOrigin(self):
        # Getter that returns the object of the Flight origin
        return self._origin

    def getDestination(self):
        # Getter that returns the object of the Flight destination
        return self._destination

    def isDomesticFlight(self):
        # Returns True if the flight is domestic
        return self._origin.getCountry() == self._destination.getCountry()

    def setOrigin(self, origin):
        # Setter that updates the Flight origin
        if isinstance(origin, Airport):
            self._origin = origin

    def setDestination(self, destination):
        # Setter that updates the Flight destination
        if isinstance(destination, Airport):
            self._destination = destination
