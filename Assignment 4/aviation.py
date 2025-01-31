from Flight import *
from Airport import *

class Aviation:
    def __init__(self):
        # Stores instance variables
        self._allAirports = {}
        self._allFlights = {}
        self._allCountries = {}

    def getAllAirports(self, airports):
        self._allAirports = airports

    def getAllFlights(self, flights):
        self._allFlights = flights

    def getAllCountries(self, countries):
        self._allCountries = countries

    def setAllAirports(self):
        return self._allAirports

    def setAllFlights(self):
        return self._allFlights

    def setAllCountries(self):
        return self._allCountries

    def loadData(self, airportFile, flightFile, countriesFile):
        try:
            with open(countriesFile, "r", encoding='utf8') as file:
                for line in file:
                    # Read all the data in the countries file
                    line = line.strip()
                    country, continent = map(str.strip, line.split(','))
                    self._allCountries[country] = continent

            with open(airportFile, "r", encoding='utf8') as file:
                for line in file:
                    # Read all the data in the airports file
                    code, name, city, country = map(str.strip, line.split(','))
                    country = self._allCountries.get(country)
                    airport = Airport(code, name, city, country)
                    self._allAirports.append(airport)

            with open(flightFile, "r", encoding='utf8') as file:
                for line in file:
                    # Read all the data from the flights file
                    flightNo, origCode, destCode = map(str.strip, line.split(','))
                    origAirport = self.getAirportByCode(origCode)
                    destAirport = self.getAirportByCode(destCode)
                    flight = Flight(flightNo, origAirport, destAirport)
                    if origCode in self._allFlights:
                        self._allFlights[origCode].append(flight)
                    else:
                        self._allFlights[origCode] = [flight]

            # Return True if the function ran successfully
            return True
        except:
            # Return False if there was an error while running the function
            return False

    def getAirportByCode(self, code):
        # Return the Airport object that has the given code
        for airport in self._allAirports:
            if airport.getCode() == code:
                return airport
        else:
            return -1

    def findAllCityFlights(self, city):
        # Returns a list that contains all Flight objects that involve the given city either as origin or the destination
        cityFlights = []
        for flights in self._allFlights.values():
            for flight in flights:
                if flight.getOrig().getCity() == city or flight.getDest().getCity() == city:
                    cityFlights.append(flight)
        return cityFlights

    def findFlightByNo(self, flightNo):
        # Returns a flight object of which the flight number equals to flightNo
        for flights in self._allFlights.values():
            for flight in flights:
                if flight.getFlightNumber() == flightNo:
                    return flight
        else:
            return -1

    def findAllCountryFlights(self, country):
        # Returns a list that contains all Flight objects that involve the given country either as the origin or the destination (or both)

        # Find all airports in the given country
        airportsCountry = [airport.getCode() for airport in self._allAirports if airport.getCountry() == country]

        # Make a list of all Flight objects that involve airportsCountry
        flightsCountry = []
        for airport in airportsCountry:
            for flight in self._allFlights.get(airport, []):
                if flight.getDest().getCountry() == country or flight.getOrig().getCountry() == country:
                    flightsCountry.append(flight)
        return flightsCountry

    def findFlightBetween(self, origAirport, destAirport):
        # Check if there's a direct flight from origAirport object to destAirport object
        for flight in self._allFlights.values():
            if flight.getOrigin() == origAirport and flight.getDestination() == destAirport:
                return f"Direct Flight({flight.getFlightNumber()}): {origAirport.getCode()} to {destAirport.getCode()}"

        # Check if there's a single-hop connecting flight from origAirport to destAirport
        connectAirports = set()
        for flight1 in self._allFlights.values():
            if flight1.getOrigin() == origAirport:
                for flight2 in self._allFlights.values():
                    if flight2.getDestination() == destAirport and flight2.getOrigin() == flight1.getDestination():
                        connectAirports.add(flight1.getDestination())
        if len(connectAirports) > 0:
            return connectAirports
        else:
            return -1

    def findReturnFlight(self, firstFlight):
        # Finds the Flight object that departs from origin B and arrives in destination A
        origAirport = firstFlight.getOrigin()
        destAirport = firstFlight.getDestination()
        for flight in self._allFlights.values():
            if flight.getOrigin() == destAirport and flight.getDestination() == origAirport:
                return flight
        return -1

    def findFlightsAcross(self, ocean):
        # Returns a set of all the flight codes that cross the specified ocean
        green = {'North America', 'South America'}
        red = {'Asia', 'Australia'}
        blue = {'Africa', 'Europe'}
        if ocean == 'Pacific':
            origZone = red
            destZone = green
        elif ocean == 'Atlantic':
            origZone = green
            destZone = blue
        else:
            return -1
        codes = set()
        for flight in self._allFlights.values():
            origContinent = flight.getOrigin().getContinent()
            destContinent = flight.getDestination().getContinent()
            if (origContinent in origZone and destContinent in destZone) or (origContinent in destZone and destContinent in origZone):
                codes.add(flight.getFlightNumber())
        if len(codes) > 0:
            return codes
        else:
            return -1
