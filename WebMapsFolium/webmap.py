
import pandas
import folium

# VOLCANX020,NUMBER,NAME,LOCATION,STATUS,ELEV,TYPE,TIMEFRAME,LAT,LON

dataFrame = pandas.read_csv('./Volcanoes_USA.txt')

lat = list(dataFrame["LAT"])
lon = list(dataFrame["LON"])
elev = list(dataFrame["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return 'brown'
    elif 1000 <= elevation < 3000:
        return 'black'
    else:
        return 'white'


# find the highest strato Volcano to open on
df = dataFrame[dataFrame.TYPE == 'Stratovolcano']

df = df[df.ELEV > 3000 ]

initLat = 35.35
initLon = -105.125

if ( df.empty == False):
    row = df.max()
    initLat = row.LAT
    initLon = row.LON
else:
    df = dataFrame[dataFrame.TYPE == 'Stratovolcano']
    df = df[df.ELEV < 3000 ]
    if ( df.empty == False):
        row = df.max()
        initLat = row.LAT
        initLon = row.LON

map = folium.Map(location=[initLat, initLon], zoom_start=3, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for lat, lon, elev in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lat, lon], radius = 6, popup=str(elev)+" m",
    fill_color=color_producer(elev), fill=True,  color = 'grey', fill_opacity=1.0))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('./world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("index.html")

