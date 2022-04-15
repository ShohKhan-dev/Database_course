from geopy.geocoders import Nominatim
import psycopg2

geolocator = Nominatim(user_agent="Mozilla/5.0")

location = geolocator.geocode("1557 Ktahya Boulevard")

conn = psycopg2.connect(database="vdrental", user="postgres",
                       password="8Rametago8", host="127.0.0.1", port="5432")

cur = conn.cursor()

#add_lat ='''ALTER TABLE address add column latitude float8'''
#add_long = '''ALTER TABLE address add column longitude float8'''

#cur.execute(add_lat)
#cur.execute(add_long)
#conn.commit()


cur.execute("INSERT INTO address (ID,Name,Address,review) VALUES ('"+fake.name()+"','"+fake.address()+"')")

if location:
    #print(location.address)
    lat = location.latitude
    long = location.longitude
    
else:
    lat = 0
    long = 0


print(lat, long)
