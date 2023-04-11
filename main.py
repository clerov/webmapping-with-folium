import folium as fl
import pandas as pd

volcano_data = pd.read_csv("./data/Volcanoes_USA.txt")

volcanoes = {
    "lat": list(volcano_data["LAT"]),
    "lon": list(volcano_data["LON"]),
    "elev": list(volcano_data['ELEV']),
    "name": list(volcano_data['NAME'])
}

def color_producer(elev)-> str:
    if elev < 1000:
        return 'green'
    elif 100 <= elev < 3000:
        return 'orange'
    else:
        return 'red'


# Define a new map using folium

map = fl.Map(location=[5.65, 77.91], zoom_start=6)

# Create a new feature group
fg = fl.FeatureGroup(name="GeoPlaces")

for lat, lon, elev, name in zip(volcanoes['lat'], volcanoes['lon'], volcanoes['elev'], volcanoes['name']):
    fg.add_child(fl.Marker(location=[lat, lon],elev=elev, popup=str(name)+" ", icon=fl.Icon(color=color_producer(elev))))

fg.add_child((fl.GeoJson(data=(open('./data/world.json', 'r', encoding='utf-8-sig').read()), style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005']< 10000000 else 'orange' if 10000000 <= x['properties']['POP2005']<20000000 else 'red'} )))


map.add_child(fg)

# Define the output file
# This will generate output file named as index.html in same directory 
map.save('index.html')
print('Successfully Created The File')



