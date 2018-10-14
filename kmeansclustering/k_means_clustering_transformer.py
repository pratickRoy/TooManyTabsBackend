import json

import numpy as np
import commons.string_to_vector_transformer as string_to_vector_transformer


def transform(tab_list_json):
    """
        This transform expects json of the form

        {
            "id": 1675296550,
            "tabOpenedTimeInMillis": 6897018,
            "lastAccessedTimeInMillis": 6165700,
            "noOfAccesses": 2,
            "title": "WaniKani / Dashboard",
            "latitudeWhenOpened": 12.994895099999999,
            "longitudeWhenOpened": 77.66094389999999,
            "h1": 0,
            "table": 0.007029876977152899,
            "td": 0.028119507908611598,
            "a": 0.3602811950790861,
            "li": 0.39191564147627417,
            "audio": 0,
            "h5": 0,
            "object": 0,
            "h6": 0,
            "pre": 0,
            "code": 0,
            "iframe": 0,
            "form": 0.0017574692442882249,
            "select": 0,
            "i": 0.028119507908611598,
            "input": 0.0035149384885764497,
            "h4": 0.029876977152899824,
            "p": 0.070298769771529,
            "h2": 0,
            "ul": 0.02460456942003515,
            "h3": 0.012302284710017574,
            "b": 0.0035149384885764497,
            "video": 0,
            "tr": 0.028119507908611598,
            "img": 0.008787346221441126,
            "ol": 0.0017574692442882249,
            "text_content": "WaniKani / Dashboard WaniKani requires JavaScript to function properly Level 2 Radicals Progression 91% 034 See Apprentice Radicals Left Level 2 Kanji Progression 7%Goal: 90% 038 See Apprentice Kanji Left New Unlocks In The Last 30 Days See More Unlocks... Critical Condition Items Burned Items In The Last 30 Days Recent Community Topics Visit The Community Center... WaniKani News View the blog"
        }
    """
    return get_index_id_map_and_points_from_json(tab_list_json)


def get_index_id_map_and_points_from_json(tab_list_json):
    tab_list = json.loads(tab_list_json)
    index_id_map = {}
    points = []

    for i, tab in enumerate(tab_list):
        normalize_tab(tab)
        for index, key in enumerate(tab):
            if key == 'id':
                index_id_map[i] = tab[key]
            else:
                transformed_type, transformed_value = transform_tab_value_for_processing(key, tab[key])

                if i >= len(points):
                    points.append([])

                if transformed_type == "v":

                    for j, v in enumerate(transformed_value):
                        points[i].append(np.float64(v))
                else:
                    points[i].append(np.float64(transformed_value))

    return index_id_map, np.array(points)


def transform_tab_value_for_processing(key, value):
    transformer = {
        "title": [string_to_vector_transformer.transform, "v"],
        "pageContentHTML": [string_to_vector_transformer.transform, "v"],
        "text_content": [string_to_vector_transformer.transform, "v"]
    }
    if key in transformer:
        return transformer[key][1], transformer[key][0](value)
    return "i", value


def normalize_tab(tab):
    key_list = ["id", "tabOpenedTimeInMillis", "lastAccessedTimeInMillis", "noOfAccesses", "title",
                "latitudeWhenOpened", "longitudeWhenOpened", "h1", "table", "td", "a", "li", "audio", "h5", "object",
                "h6", "pre", "code", "iframe", "form", "select", "i", "input", "h4", "p", "h2", "ul", "h3", "b",
                "video", "tr", "img", "ol", "text_content"]

    for key in key_list:
        if key not in tab or tab[key] is None:
            tab[key] = 0
