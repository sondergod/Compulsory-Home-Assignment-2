import random as rd
# from abc import ABC   # ERROR: abstractmethod is used but not imported. Also ABC is never used as a base.
from abc import ABC, abstractmethod  # FIX: import abstractmethod too; will use ABC properly.


def get_location():
    eu_capitals = ["Amsterdam","Athens","Berlin","Bratislava","Brussels","Bucharest","Budapest","Copenhagen","Dublin","Helsinki",
                   "Lisbon","Ljubljana","Luxembourg","Madrid","Nicosia","Paris","Prague","Riga","Rome","Sofia",
                   "Stockholm","Tallinn","Valletta","Vienna","Vilnius","Warsaw","Zagreb"]
    # selection = rd.choice(range(0, 26))  # ERROR: returns an integer index and ignores last cities due to 0..25 range.
    selection = rd.choice(eu_capitals)      # FIX: return a random capital directly.
    return selection

# class holiday_venue(hotel):
#     def __init__(self, id, rating):
#         self.id = id
#         self.rating = rating
#         self.location = get_location()
#
#     @abstractmethod
#     def number_of_rooms(self):
# ERROR: Inheritance is inverted. A general "holiday venue" should be the abstract base; Hotel should inherit it.
class HolidayVenue(ABC):
    def __init__(self, id, rating):
        self.id = id
        self.rating = rating
        self.location = get_location()

    @abstractmethod
    def number_of_rooms(self):
        ...
    
    @abstractmethod
    def book(self, rooms):
        ...

    def amenities_package(self):
        if self.rating <= 2:
            self.amenities_tier = 'Basic'
        elif self.rating == 3:
            self.amenities_tier = 'Standard'
        elif self.rating == 4:
            self.amenities_tier = 'Premium'
        else:
            self.amenities_tier = 'Luxury'

    def upgrade_venue(self):
        if self.rating < 5:
            self.rating += 1
            self.amenities_package()
        else:
            print("This venue already has the highest rating.")

    def venue_downgrade(self):
        self.rating = max(1, self.rating - 1)
        self.amenities_package()

# def amenities_package(self):  # ERROR: this function was outdented to module scope by mistake.
#     ...

# class hotel():  # ERROR: class name should be Capitalized by convention; also will be subclass of an abstract base.
#     rooms = [50, 75, 100, 120, 200, 300, 350]
class Hotel(HolidayVenue):
    rooms = [50, 75, 100, 120, 200, 300, 350]

    # def __init__(self, id, rating):
    #     super().__init__(id, rating)   # ERROR: super() call invalid until we actually subclass an ABC with __init__.
    #     self.hotel_id = id
    #     ...
    #     self.pos, self.rooms_available = self.number_of_rooms()  # ERROR: number_of_rooms returned only a single value.
    #     self.amenities = self.choosing_amenities()
    def __init__(self, id, rating):
        super().__init__(id, rating)
        self.hotel_id = id
        self.rating = rating
        self.location = get_location()
        self.brand = rd.choice(['Hilton','Marriott','Hyatt','Intercontinental','Accor','Wyndham','Choice','Best Western','Radisson','Meliá'])
        self.type = rd.choice(['Resort','Business','Boutique'])
        self.stars = rd.randint(1, 5) # self.stars = rd.randint(0, 5)  # ERROR: hotel star ratings should be 1..5.
        self.pos, self._number_of_rooms = self.number_of_rooms()
        self.amenities = self.choosing_amenities()
        self.amenities_package()
    
    def book(self, rooms=1):
        if self._number_of_rooms >= rooms:
            self._number_of_rooms -= rooms
            return True
        return False
  

    # def number_of_rooms(self, rooms=rooms):
    #     pos = rooms.index(rd.choice(rooms))
    #     return pos                         # ERROR: returns only index, not rooms count.
    def number_of_rooms(self, rooms=rooms):
        pos = rooms.index(rd.choice(rooms))
        return pos, rooms[pos]

    def renovate_hotel(self, rooms=rooms):
        if self.pos < len(rooms) - 1:
            self.pos += 1
            self.rooms_available = rooms[self.pos]
            # self.stars += 1  # Optional: could increase up to 5; not necessarily tied to rooms.
            self.stars = min(5, self.stars + 1)
        else:
            print("This hotel already has the maximum number of rooms.")

    def choosing_amenities(self):
        # if self.stars == 1:
        #     amenities = ['Breakfast', 'Free wifi', 'Bar', 'Gym']
        # elif self.stars == 2:
        #     amenities.append([...])  # ERROR: amenities not defined; should assign, not append.
        # ...
        # else:
        #     amenities.append([...])
        #     self.stars = 5  # side-effect not needed here.
        if self.stars == 1:
            amenities = ['Breakfast', 'Free wifi']
        elif self.stars == 2:
            amenities = ['Breakfast', 'Free wifi', 'Bar', 'Gym']
        elif self.stars == 3:
            amenities = ['Breakfast', 'Free wifi', 'Bar', 'Gym', 'Conference room', 'Concierge service']
        elif self.stars == 4:
            amenities = ['Breakfast', 'Free wifi', 'Bar', 'Gym', 'Conference room', 'Concierge service',
                         'Spa', 'Pool', 'Valet parking', 'Laundry service']
        else:
            amenities = ['Breakfast', 'Free wifi', 'Bar', 'Gym', 'Conference room', 'Concierge service',
                         'Spa', 'Pool', 'Valet parking', 'Laundry service', 'Butler service',
                         'Gourmet restaurant', 'Limousine service']
            self.stars = 5
        return amenities

    
# class resort_hotel(hotel):
#     def __init__(self, id, rating):
#         self.beach_access = rd.choice(['True', 'False'])  # ERROR: strings instead of booleans
#         ...                                               # ERROR: no super().__init__ call.
class ResortHotel(Hotel):
    def __init__(self, id, rating):
        super().__init__(id, rating)
        self.beach_access = rd.choice([True, False])
        self.pool_size = rd.choice(['Small','Medium','Large'])
        self.spa = rd.choice([True, False])
        self.family_friendly = rd.choice([True, False])


class BusinessHotel(Hotel):
    def __init__(self, id, rating):
        super().__init__(id, rating)
        self.conference_rooms = rd.randint(1, 5)
        self.business_center = rd.choice([True, False])
        self.high_speed_internet = rd.choice([True, False])
        self.room_service = rd.choice([True, False])


# class boutique_hotel(hotel):
#     def __init__(self, id):
#         super().__init__(id)               # ERROR: signature mismatch; missing rating; also super args wrong.
#         self.unique_design = np.choice([True, False])  # ERROR: uses numpy not imported; should use random.
#         ...
class BoutiqueHotel(Hotel):
    def __init__(self, id, rating):
        super().__init__(id, rating)
        self.unique_design = rd.choice([True, False])
        self.personalized_service = rd.choice([True, False])
        self.intimate_size = rd.choice([True, False])


# class short_term_rental(holiday_venue):
#     views = ['seaside', 'town', 'garden view', 'no view']
#     def __init__(self, id, rating):
#         global._init__(id, rating)   # ERROR: nonsensical; should be super().__init__
#         self._number_of_rooms = self.input_number_of_rooms()
#         ...
#         self.view = rd.choice(self.view)   # ERROR: attribute name is "views".
class ShortTermRental(HolidayVenue):
    views = ['seaside', 'town', 'garden view', 'no view']

    def __init__(self, id, rating, preset_rooms=None):
        super().__init__(id, rating)
        self._number_of_rooms = preset_rooms if preset_rooms is not None else rd.randint(1, 5)
        self.garden = rd.choice([True, False])
        self.pool = rd.choice([True, False])
        self.view = rd.choice(self.views)

    def input_number_of_rooms(self, value=None):
        while True:
            try:
                number = int(input("Enter number of rooms for short-term rental (1–5): "))
                if 1 <= number <= 5:
                    return number
                else:
                    print("Please enter a value between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def number_of_rooms(self):
        return self._number_of_rooms

    def book(self, rooms=1):
        if self._number_of_rooms >= rooms:
            self._number_of_rooms -= rooms
            return True
        return False


# class hostel(hotel):
#     def __init__(self, id, rating, number_of_rooms=None):
#         hotel().__init__(id, rating)  # ERROR: incorrect super call
#         self._number_of_rooms = rd.randint(1, 25) if number_of_rooms is None else number_of_rooms
#         if not (1 <= self._number_of_rooms <= 25):
#             raise ValueError("Hostel number_of_rooms must be between 1 and 30.")  # ERROR: mismatch (25 vs 30)
class Hostel(HolidayVenue):
    def __init__(self, id, rating, number_of_rooms=None):
        super().__init__(id, rating)
        self._number_of_rooms = rd.randint(1, 30) if number_of_rooms is None else number_of_rooms
        if not (1 <= self._number_of_rooms <= 30):
            raise ValueError("Hostel number_of_rooms must be between 1 and 30.")
        self.hot_water = rd.choice([True, False])
        self.wifi = rd.choice(["free", "none"])

    def number_of_rooms(self):
        return self._number_of_rooms

    def book(self, rooms=1):
        if self._number_of_rooms >= rooms:
            self._number_of_rooms -= rooms
            return True
        return False


class CapsuleHostel(Hostel):
    def __init__(self, id, rating, number_of_rooms=None):
        super().__init__(id, rating, number_of_rooms)
        self.capsule_count = rd.randint(20, 120)
        self.pod_privacy_level = rd.choice(["low", "medium", "high"])
        self.kiosk_checkin = rd.choice([True, False])
        self.lockers = rd.choice([True, False])


class SocialHostel(Hostel):
    def __init__(self, id, rating, number_of_rooms=None):
        super().__init__(id, rating, number_of_rooms)
        self.bar_on_site = rd.choice([True, False])
        self.event_nights = rd.choice([["jazz night"], ["salsa"], ["karaoke"], ["board game night"], []])
        self.quiet_hours_start = rd.choice(["22:00", "23:00", "00:00"])
        self.common_area_size = rd.choice(["small", "medium", "large"])

budget_options=['low','medium','high']
client_preferences = ['short_term_rental','capsule_hostel','social_hostel','resort_hotel','business_hotel','boutique_hotel']
roadmap={'short_term_rental':'medium','capsule_hostel':'low','social_hostel':'medium','resort_hotel':'high','business_hotel':'medium','boutique_hotel':'high'}

class Client:
    def __init__(self, name, budget, preferred_type=None, rooms_needed=None):
        self.name = name
        self.budget = budget                    # 'low', 'medium', or 'high'
        self.preferred_type = preferred_type    # e.g. 'ShortTermRental', 'BusinessHotel'
        self.rooms_needed = rooms_needed if rooms_needed is not None else rd.randint(1, 3)
        self.booked_venue = None                # stores the venue this client successfully booked

    def choose_venue(self, venues, roadmap):
        """Choose a random venue that matches the client's budget and/or preferred type."""
        matching = [
            venue for venue in venues
            if roadmap.get(venue.__class__.__name__, None) == self.budget
        ]

        if self.preferred_type:
            matching = [v for v in matching if v.__class__.__name__ == self.preferred_type]

        if not matching:
            print(f"{self.name} found no venues matching budget '{self.budget}'.")
            return None

        return rd.choice(matching)
    

    def book_venue(self, venues, roadmap):
        venue = self.choose_venue(venues, roadmap)
        if not venue:
            return

        success = venue.book(self.rooms_needed)

        if success:
            self.booked_venue = venue
            print(f"{self.name} booked {self.rooms_needed} room(s) at "
                f"{venue.__class__.__name__} ({venue.location}) – {venue._number_of_rooms} left")

            # Detailed venue info depending on type
            if isinstance(venue, ShortTermRental):
                print(f"  → View: {venue.view}, Pool: {venue.pool}, Garden: {venue.garden}")
            elif isinstance(venue, Hostel):
                print(f"  → Hot water: {venue.hot_water}, Wi-Fi: {venue.wifi}")
            elif isinstance(venue, Hotel):
                print(f"  → Brand: {venue.brand}, Stars: {venue.stars}, Amenities: {venue.amenities_tier}")

            # Fallback message if fully booked after this reservation
            if venue._number_of_rooms == 0:
                print(f"  → No more rooms available at {venue.__class__.__name__} in {venue.location}.")

        else:
            print(f"{self.name} could not book {self.rooms_needed} room(s) at "
                f"{venue.__class__.__name__} ({venue.location}) – no availability")


#####################--------------------------------------CREATING CLIENTS, VENUES AND INTERACTIONS--------------------------------------#####################

# --- Venue creation phase ---
v = []
venue_counts = {}

number_of_venues = rd.randint(10, 100)
print(f"\n[Setup] Creating {number_of_venues} venues...")

for i in range(number_of_venues):
    id = i + 1
    rating = rd.randint(1, 5)
    x_type = rd.choice([
        'ShortTermRental',
        'CapsuleHostel',
        'SocialHostel',
        'ResortHotel',
        'BusinessHotel',
        'BoutiqueHotel'
    ])

    # Instantiate the correct venue type
    venue_class = globals()[x_type]
    v.append(venue_class(id, rating))
    venue_counts[x_type] = venue_counts.get(x_type, 0) + 1

# Summary of venues created
print("\n[Summary] Venue creation complete:")
for venue_type, count in venue_counts.items():
    print(f"  {venue_type}: {count}")

# Optional customization
choice = input("\n[Input] Customize number of rooms for ShortTermRentals? (yes/no): ").strip().lower()
if choice == "yes":
    for venue in v:
        if isinstance(venue, ShortTermRental):
            venue.input_number_of_rooms()
print("\n[Info] Customization complete. All venues finalized.")

# --- Client creation phase ---
clients = []
client_counts = {}

number_of_clients = rd.randint(100, 200)
print(f"\n[Setup] Creating {number_of_clients} clients...")

budgets = ['low', 'medium', 'high']
roadmap = {
    'ShortTermRental': 'medium',
    'CapsuleHostel': 'low',
    'SocialHostel': 'medium',
    'ResortHotel': 'high',
    'BusinessHotel': 'medium',
    'BoutiqueHotel': 'high'
}

for i in range(number_of_clients):
    name = f"Client_{i+1}"
    budget = rd.choice(budgets)
    valid_types = [t for t, b in roadmap.items() if b == budget]
    preferred_type = rd.choice(valid_types)
    rooms_needed = rd.randint(1, 3)
    new_client = Client(name, budget, preferred_type, rooms_needed)
    clients.append(new_client)
    client_counts[budget] = client_counts.get(budget, 0) + 1

# Summary of clients created
print("\n[Summary] Client creation complete:")
for budget, count in client_counts.items():
    print(f"  {budget.capitalize()}-budget clients: {count}")

print(f"\n[Info] All {len(clients)} clients have been created successfully.")

# --- Booking phase ---
print("\n[Process] Booking phase started...\n")

for client in clients:
    client.book_venue(v, roadmap)

# --- Booking summary ---
print("\n[Summary] Booking results:")

for i, client in enumerate(clients[:10]):
    if client.booked_venue:
        booked = client.booked_venue
        print(f"  {client.name} booked {booked.__class__.__name__} in {booked.location}.")
    else:
        print(f"  {client.name} did not manage to book any venue.")

if len(clients) > 10:
    print(f"  ... (skipping {len(clients) - 10} more clients)")

booked_total = sum(1 for c in clients if c.booked_venue)
print(f"\n[Stats] Successful bookings: {booked_total}/{len(clients)} clients.")

# --- Remaining availability ---
print("\n[Summary] Remaining availability (first 10 venues):")
for venue in v[:10]:
    print(f"  {venue.__class__.__name__} in {venue.location}: {venue._number_of_rooms} rooms left")

print("\n[End] Simulation complete.\n")
