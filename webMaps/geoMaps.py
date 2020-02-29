import folium
import pandas

data = pandas.read_csv("volcanoes.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
nam = list(data["NAME"])
elev = list(data["ELEV"])

def colorGrader(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    elif 3000 <= elevation < 5000:
        return 'purple'
    else:
        return 'red'

map = folium.Map(
    location=[-1.287060, 36.798872], 
    zoom_start=4,
    tiles='Open Street Map'
    )

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, nm, el in zip(lat, lon, nam, elev):
    fgv.add_child(folium.CircleMarker(
        location=[lt, ln], 
        popup="<b>Name:</b> " + nm + "\n<b>Height:</b> " + str(el) + "m.", 
        radius=8,
        fill_color=colorGrader(el),
        color='grey',
        fill_opacity=0.7
    ))
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(
    data=open('worldPop.json', 'r', encoding='utf-8-sig')
    .read(),
    style_function=
        lambda x: {
            'fillColor': 'yellow' 
                if x ['properties']['POP2005'] < 15000000 
                else 'orange' if 15000000 <= x['properties']['POP2005'] < 35000000
                else 'green' if 35000000 <= x['properties']['POP2005'] < 45000000
                else 'red'
        }
))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("geoMap.html")