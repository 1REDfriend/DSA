import json

def findStations(stations, all_cities):
    uncovered_cities = set(all_cities)
    selected_stations = []
    
    while uncovered_cities:
        best_station = None
        max_covered = 0
        
        for station in stations:
            covered = len(set(station["Cities"]) & uncovered_cities)
            if covered > max_covered:
                max_covered = covered
                best_station = station
        
        if best_station:
            selected_stations.append(best_station["Name"])
            uncovered_cities -= set(best_station["Cities"])
        else:
            break
    
    selected_stations.sort()
    return selected_stations

all_cities = json.loads(input())
n = int(input())
stations = []
for _ in range(n):
    station_data = json.loads(input())
    stations.append(station_data)

result = findStations(stations, all_cities)
print(result)