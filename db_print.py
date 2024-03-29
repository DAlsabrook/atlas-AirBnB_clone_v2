# #!/usr/bin/python3
# from models.engine.db_storage import DBStorage
# from models.place import place_amenity
# from sqlalchemy import select
# from models.state import State
# from models.city import City
# from models.place import Place
# from models.user import User
# from models.amenity import Amenity

# def print_tables():
#     session = DBStorage()
#     session.reload()
#     engine = session.get_engine()

#     with engine.connect() as connection:
#         place_amen = connection.execute(select(place_amenity)).fetchall()
#         states = connection.execute(select(State)).fetchall()
#         cities = connection.execute(select(City)).fetchall()
#         places = connection.execute(select(Place)).fetchall()
#         users = connection.execute(select(User)).fetchall()
#         amenities = connection.execute(select(Amenity)).fetchall()

#     print("\nStates table:")
#     for state in states:
#         print(f"{state.name}", end="  | ")

#     print("\n\nCities table:")
#     for city in cities:
#         print(f"{city.name}", end="  | ")

#     print("\n\nPlaces table:")
#     for place in places:
#         print(f"{place.name}", end="  | ")

#     print("\n\nAmenities table:")
#     for amenity in amenities:
#         print(f"{amenity.name}", end="  | ")

#     print("\n\nUsers table:")
#     for user in users:
#         print(f"{user.email}", end="  | ")

#     i = -1
#     print("\n\nplace_amenity table:")
#     print("| ", end="")
#     for row in place_amen:
#         for obj in row:
#             if i < 2:
#                 print(f"{obj}", end=" | ")
#                 i += 1
#             else:
#                 print(f"\n| {obj}", end=" | ")
#                 i = 0

#     print()


# if __name__ == "__main__":
#     print_tables()

from models.engine.db_storage import DBStorage
from models.place import Place
from models.state import State
from models.city import City

def print_tables():
    session = DBStorage()
    session.reload()

    # Assuming DBStorage session provides access to the ORM session
    orm_session = session.get_session()

    # fetching all State instances
    states = orm_session.query(State).all()
    print("States:\n\t", end="")
    for state in states:
        print(f"{state.name}", end=" | ")

    # Fetching all City instances
    cities = orm_session.query(City).all()
    print()
    print("Cities:\n\t", end="")
    for city in cities:
        print(f"{city.name}", end=" | ")

    # Fetching all Place instances
    places = orm_session.query(Place).all()

    print("\n\nPlaces and their amenities:")
    for place in places:
        print(f"\t-{place.name} in {place.cities.name}, {place.cities.state.name}\n\t\tamenities:", end=" | ")
        for amenity in place.amenities:
            print(amenity.name, end=" | ")
        print("\n")

    # Other table prints...

if __name__ == "__main__":
    print_tables()
