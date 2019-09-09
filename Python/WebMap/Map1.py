import folium
import pandas
import Functions
from folium.plugins import FloatImage



data_MarkerVolc = pandas.read_csv("Volcanoes.txt")
data_MarkerCapit = pandas.read_json("StatesCapitals.txt")
data_MarkerCapitT = data_MarkerCapit.transpose()
data_MarkerWorldCapit = pandas.read_json("WorldCapitals.json")

map = folium.Map(location=[38.30, -99.94], tiles="Stamen Terrain", zoom_start=5)

fg = Functions.add_markers(data_MarkerVolc, "red", "volcanoes")
map.add_child(fg)
fg = Functions.add_markers(data_MarkerCapitT, "black", "cities")
map.add_child(fg)

fg = Functions.add_polygon()
map.add_child(fg)

image_file = 'POPULATIONLEGEND.png'
FloatImage(image_file, bottom=0, left=0).add_to(fg)

fg = Functions.add_markers(data_MarkerWorldCapit, "gray", "capitals")
map.add_child(fg)
map.add_child(folium.LayerControl())

map.save("Map1.html")
