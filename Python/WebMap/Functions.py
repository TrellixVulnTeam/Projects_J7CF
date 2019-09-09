import folium

def add_markers(data_marker, clr, thing):

    if thing == "volcanoes":
        fg = folium.FeatureGroup(name="Volcanoes in America")
        for i in range(len(data_marker)):
            html = """
            <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
            Height: %s m
            """
            iframe = folium.IFrame(html=html % (str(data_marker['name'][i]) + " volcano",
                                                str(data_marker['name'][i]), str(data_marker['ELEV'][i])),
                                   width=150, height=100)

            fg.add_child(folium.Marker(location=[data_marker['lat'][i], data_marker['long'][i]],
                                       popup=folium.Popup(iframe),
                                       icon=folium.Icon(color=clr)))


    elif thing == "cities":
        fg = folium.FeatureGroup(name="States Capitals")
        for i in range(len(data_marker)):
            html = """
            <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
            """
            iframe = folium.IFrame(html=html % (str(data_marker['name'][i]) + " city", str(data_marker['name'][i])),
                                   width=100, height=50)
            fg.add_child(folium.Marker(location=[data_marker['lat'][i], data_marker['long'][i]],
                                       popup=folium.Popup(iframe),
                                       icon=folium.Icon(color=clr)))
    elif thing == "capitals":
        fg = folium.FeatureGroup(name="Capitals")
        for i in range(len(data_marker)):
            html = """
            <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
            """
            iframe = folium.IFrame(html=html % (str(data_marker['CapitalName'][i]) + " city", str(data_marker['CapitalName'][i])),
                                   width=100, height=50)
            fg.add_child(folium.Marker(location=[data_marker['CapitalLatitude'][i], data_marker['CapitalLongitude'][i]],
                                       popup=folium.Popup(iframe),
                                       icon=folium.Icon(color=clr)))

    return fg


def add_polygon():
    fg = folium.FeatureGroup(name="Population")
    fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig')).read(),
                                style_function=lambda x: {'fillColor': 'green'
                                if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 30000000
                                else 'red'}))

    return fg

