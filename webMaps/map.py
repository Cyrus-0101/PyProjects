import folium
import pandas

data = pandas.read_csv("volcanoes.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
nam = list(data["NAME"])
elev = list(data["ELEV"])

map = folium.Map(location=[-1.287060, 36.798872], zoom_start=3, tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community')

fg = folium.FeatureGroup(name="My Geo-Map")

for lt, ln, nm, el in zip(lat, lon, nam, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup="<b>Name:</b> " + nm + "\n<b>Height:</b> " + str(el) + "m.", icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("map1.html")