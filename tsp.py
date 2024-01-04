class TSP:
    @staticmethod
    def nearest_neighbor_tsp(cities):                                                    #NN algorithm 
        if not cities:
            return [], 0

        start_city = cities[0]
        tour = [start_city]
        unvisited = set(cities[1:])
        total_distance = 0                                                               #initialize parameters

        current_city = start_city
        while unvisited:
            next_city = min(unvisited, key=lambda city: city.distance_to(current_city))  #sort unvisited cities.distance
            total_distance += current_city.distance_to(next_city)                        #update total_distance
            unvisited.remove(next_city)                                                  #remove visited
            tour.append(next_city)                                                       #add to tour as next visited
            current_city = next_city                                                     #update current city to new visited location

        total_distance += current_city.distance_to(start_city)                           #add returning back distance to start_city
        return tour, total_distance

    @staticmethod
    def one_opt(tour):                                                                   #improvement with 1-opt
        improved = True                                                                  #initialize bool flag to execute while loop
        while improved:                                                                  #iterate while solution improved
            improved = False                                                             #not updated yet
            for i in range(len(tour) - 1):                                               #iterate all next locations
                for j in range(i + 2, len(tour)):                                        #iterate over possibly changing locations
                    new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]                     #change places
                    if TSP.tour_distance(new_tour) < TSP.tour_distance(tour):            #if updated tour is smaller then existing
                        tour = new_tour                                                  #update
                        improved = True                                                  #break flag
                        break
                if improved:
                    break
        return tour

    @staticmethod
    def tour_distance(tour):
        distance = 0
        for i in range(len(tour)):
            distance += tour[i].distance_to(tour[(i + 1) % len(tour)])                   #update total tour distance 
        return distance
