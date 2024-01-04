from csv_parser import CSVParser
from knapsack import Knapsack
from tsp import TSP

def main():
    # Parse songs and cities from CSV files in file
    songs = CSVParser.parse_songs("songs_data.csv")                                      #import and parse song data for Madonna
    cities = CSVParser.parse_cities("cities.csv")                                        #import and parse cities data

    # Apply the Knapsack algorithm
    max_duration = 200                                                                   #Maximum capacity(duration)
    selected_songs = Knapsack.knapsack(songs, max_duration)                              #apply knapsack for songs with given max_duration
    total_popularity = sum(song.popularity for song in selected_songs)                   #Calculate total popularity(value)
    total_duration = sum(song.duration for song in selected_songs)                       #Calculate total duration(weight)

    # Display selected songs and total values
    print("Selected Songs:")
    for song in selected_songs:
        print(f"{song.name} - Popularity: {song.popularity}, Duration: {song.duration}") #print selected songs
    print(f"Total Popularity: {total_popularity}")                                       #print total popularity(value)
    print(f"Total Duration: {total_duration:} seconds")                                  #print total duration(weight)

    # Apply the TSP algorithm
    city_tour, total_distance = TSP.nearest_neighbor_tsp(cities)                         #apply TSP for cities
    # Display city tour in one row
    print("\nCity Tour:")
    print(" -> ".join(city.name for city in city_tour))                                  #print tour path

    # Display total distance of the tour
    print(f"Total Distance of Tour: {total_distance:} km")                               #print total distance
 
if __name__ == "__main__":
    main()
