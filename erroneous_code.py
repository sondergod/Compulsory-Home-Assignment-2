import random as rd
from abc import ABC


def get_location():
    eu_capitals = ["Amsterdam","Athens","Berlin","Bratislava","Brussels","Bucharest","Budapest","Copenhagen","Dublin","Helsinki",
                   "Lisbon","Ljubljana","Luxembourg","Madrid","Nicosia","Paris","Prague","Riga","Rome","Sofia",
                   "Stockholm","Tallinn","Valletta","Vienna","Vilnius","Warsaw","Zagreb"]
    selection = rd.choice(range(0, 26))
    return selection

class hotel():
    rooms = [50, 75, 100, 120, 200, 300, 350]

    def __init__(self, id, rating):
        super().__init__(id, rating)
        self.hotel_id = id
        self.brand = rd.choice(['Hilton','Marriott','Hyatt','Intercontinental','Accor','Wyndham','Choice','Best Western','Radisson','Meliá'])
        self.type = rd.choice(['Resort','Business','Boutique'])
        self.stars = rd.randint(0, 5)
        self.pos, self.rooms_available = self.number_of_rooms()
        self.amenities = self.choosing_amenities()

    def number_of_rooms(self, rooms=rooms):
        pos = rooms.index(rd.choice(rooms))
        return pos

    def renovate_hotel(self, rooms=rooms):
        if self.pos < len(rooms) - 1:
            self.pos += 1
            self.rooms_available = rooms[self.pos]
            self.stars += 1

        else:
            print("This hotel already has the maximum number of rooms.")

    def choosing_amenities(self):
        if self.stars == 1:
            amenities = ['Breakfast', 'Free wifi', 'Bar', 'Gym']
        elif self.stars == 2:
            amenities.append(['Breakfast', 'Free wifi', 'Bar', 'Gym'])
        elif self.stars == 3:
            amenities.append(['Breakfast', 'Free wifi', 'Bar', 'Gym', 'Conference_room', 'Premium Bar',
                              'Concierge_service', 'Wellness_room', 'Pickup_service', 'Room service'])
        elif self.stars == 4:
            amenities.append(['Breakfast', 'Free wifi', 'Bar', 'Gym', 'Conference_room', 'Premium Bar',
                              'Concierge_service', 'Wellness_room', 'Pickup_service', 'Room service',
                              'Spa', 'Pool', 'Valet parking', 'Laundry service'])
        else:
            amenities.append(['Breakfast', 'Free wifi', 'Bar', 'Gym', 'Conference_room', 'Premium Bar',
                              'Concierge_service', 'Wellness_room', 'Pickup_service', 'Room service',
                              'Spa', 'Pool', 'Valet parking', 'Laundry service', 'Butler service',
                              'Gourmet restaurant', 'Limousine service'])
            self.stars = 5



class holiday_venue(hotel):
    def __init__(self, id, rating):
        self.id = id
        self.rating = rating
        self.location = get_location()

    @abstractmethod
    def number_of_rooms(self):


def amenities_package(self):
    if self.rating <= 2:
        self.amenities = 'Basic'
    elif self.rating == 3:
        self.amenities = 'Standard'
    elif self.rating == 4:
        self.amenities = 'Premium'
    else:
        self.amenities = 'Luxury'

    def upgrade_venue(self):
        if self.rating < 5:
            self.rating += 1
            self.amenities_package()
        else:
            print("This venue already has the highest rating.")

    def venue_downgrade(self):
            self.rating -= 1
            self.amenities_package()

class resort_hotel(hotel):
    def __init__(self, id, rating):
        self.beach_access = rd.choice(['True', 'False'])
        self.pool_size = rd.choice(['Small','Medium','Large'])
        self.spa = rd.choice([True, False])
        self.family_friendly = rd.choice([True, False])


class business_hotel(hotel):
    def __init__(self, id, rating):
        super().__init__(id, rating)
        self.conference_rooms = rd.randint(1, 5)
        self.business_center = rd.choice([True, False])
        self.high_speed_internet = rd.choice([True, False])
        self.room_service = rd.choice([True, False])


class boutique_hotel(hotel):
    def __init__(self, id):
        super().__init__(id)
        self.unique_design = np.choice([True, False])
        self.personalized_service = np.choice([True, False])
        self.intimate_size = np.choice([True, False])


class short_term_rental(holiday_venue):
    views = ['seaside', 'town', 'garden view', 'no view']

    def __init__(self, id, rating):
        global._init__(id, rating)
        self._number_of_rooms = self.input_number_of_rooms()
        self.garden = rd.choice([True, False])
        self.pool = rd.choice([True, False])
        self.view = rd.choice(self.view)

    def input_number_of_rooms(self, value=None):
        while True:
            try:
                raw = input("Enter number of rooms for short-term rental (1–5): ") if value is None else value
                number = int(raw)
                if number in range(1, 6):
                    return number
                else:
                    raise ValueError("number_of_rooms must be between 1 and 5.")
            except ValueError as e:
                if value is not None:
                    raise
                print(e)

    def number_of_rooms(self):
        return self._number_of_rooms


class hostel(hotel):
    def __init__(self, id, rating, number_of_rooms=None):
        hotel().__init__(id, rating)
        self._number_of_rooms = rd.randint(1, 25) if number_of_rooms is None else number_of_rooms
        if not (1 <= self._number_of_rooms <= 25):
            raise ValueError("Hostel number_of_rooms must be between 1 and 30.")
        self.hot_water = rd.choice([True, False])
        self.wifi = rd.choice(["free", "paid"])

    def number_of_rooms(self):
        return self._number_of_rooms


class capsule_hostel(hostel):
    def __init__(self, id, rating, number_of_rooms=None):
        super().__init__(id, rating, number_of_rooms)
        self.capsule_count = rd.randint(20, 120)
        self.pod_privacy_level = rd.choice(["low", "medium", "high"])
        self.kiosk_checkin = rd.choice([True, False])
        self.lockers = rd.choice([True, False])


class social_hostel(hostel):
    def __init__(self, id, rating, number_of_rooms=None):
        super().__init__(id, rating, number_of_rooms)
        self.bar_on_site = rd.choice([True, False])
        self.event_nights = rd.choice([["jazz night"], ["salsa"], ["karaoke"], ["board game night"], []])
        self.quiet_hours_start = rd.choice(["22:00", "23:00", "00:00"])
        self.common_area_size = rd.choice(["small", "medium", "large"])

v=[]
number_of_venues = rd.randint(10, 100)
for i in range(number_of_venues):
    id = i + 1
    rating = rd.randint(1, 5)
    x=rd.choice(['short_term_rental','capsule_hostel','social_hostel','resort_hotel','business_hotel','boutique_hotel'])
    if x == 'short_term_rental':
        v.append(short_term_rental(id, rating))
    elif x == 'capsule_hostel':
        v.append(capsule_hostel(id, rating))
    elif x == 'social_hostel':
        v.append(social_hostel(id, rating))
    elif x == 'resort_hotel':
        v.append(resort_hotel(id, rating))
    elif x == 'business_hotel':
        v.append(business_hotel(id, rating))
    else:
        v.append(boutique_hotel(id, rating))


budget_options=['low','medium','high']
client_preferences = ['short_term_rental','capsule_hostel','social_hostel','resort_hotel','business_hotel','boutique_hotel']
roadmap={'short_term_rental':'medium','capsule_hostel':'low','social_hostel':'medium','resort_hotel':'high','business_hotel':'medium','boutique_hotel':'high'}


# Your turn:
class client():