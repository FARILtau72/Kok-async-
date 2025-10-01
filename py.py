import phonenumbers
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode
import folium

key = 'Masukkan_API_kode_anda' #api key phonenumbers
#input nomor telepon dan kode negara 
phonenumber = input("Input nomor telepon dan kode negara: ")
phonenumber = "+" + phonenumber
#mentransfer data phone number to geocoder
number_obj = phonenumbers.parse(phonenumber)
location = geocoder.description_for_number(number_obj, 'en')
#data di proses oleh geocode dengan API key 
geocoder_api = OpenCageGeocode(key)                                                                                                                                                                                                                   
results = geocoder_api.geocode(location)
#Hasil dari proses oleh Geocoder
if results:
    #Menampilkan hasil lokasi berdasarkan Letak Geometri
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(f"📍 Latitude: {lat}, Longitude: {lng}")

    #Membuat map 
    my_map = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(my_map)

    #menyimpan data di locations.html
    my_map.save("locations.html")
    print("🗺️ Map Tersimpan di 'locations.html'")
else:
    print("data tidak ditemukan/tidak valid! ")
   
    