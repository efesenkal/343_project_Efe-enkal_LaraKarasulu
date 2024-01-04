class Knapsack:
    @staticmethod
    def knapsack(songs, max_duration):
        songs.sort(key=lambda x: x.popularity / x.duration, reverse=True)      #prioritized based on popularity/duration
        total_duration = 0
        selected_songs = []                                                    #initialize parameters

        for song in songs:
            if total_duration + song.duration <= max_duration:                 #if not exceeded duration 
                selected_songs.append(song)                                    #append song to selected song list
                total_duration += song.duration                                #update total_duration with song.duration attr

        return selected_songs
