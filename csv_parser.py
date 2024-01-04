from City import City         #I added from path I used spyder
from Song import Song          
class CSVParser:
    @staticmethod
    def parse_cities(file_name):
        cities = []
        with open(file_name, 'r') as file:
            header_skipped = False
            for line in file:
                if not header_skipped:
                    header_skipped = True
                    continue
                data = line.strip().split(',')
                city_name = data[0].strip()
                latitude = float(data[2].strip())
                longitude = float(data[3].strip())
                city = City(city_name, latitude, longitude)
                cities.append(city)
        return cities

    @staticmethod
    def parse_songs(csv_file):
        songs = []
        with open(csv_file, "r") as file:
            next(file)
            for line in file:
                data = line.strip().split(',')
                song_name = data[0].strip()
                popularity = float(data[1])
                duration = float(data[2])
                song = Song(song_name, popularity, duration)   #added song name to display 
                songs.append(song)
        return songs
