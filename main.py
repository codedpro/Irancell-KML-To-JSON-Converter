import json
from pykml import parser
from lxml import etree
from tqdm import tqdm

def kml_to_json(kml_file, json_file):
    """
    Converts a KML file to a GeoJSON file.

    Args:
        kml_file: The path to the KML file. 
        json_file: The path to the GeoJSON file.
    """

    with open(kml_file, 'r') as f:
        root = parser.parse(f).getroot()

    geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    def extract_coordinates(coord_str):
        coordinates = []
        coord_pairs = coord_str.strip().split()
        for pair in coord_pairs:
            lon, lat, *alt = map(float, pair.split(','))
            coordinates.append((lon, lat))
        return coordinates

    placemarks = root.Document.Folder.Placemark
    total_placemarks = len(placemarks)

    for placemark in tqdm(placemarks, total=total_placemarks, desc="Converting KML to JSON"):
        feature = {
            "type": "Feature",
            "properties": {
                "name": str(placemark.name)
            },
            "geometry": {
                "type": "",
                "coordinates": []
            }
        }

        if hasattr(placemark, 'Point'):
            feature["geometry"]["type"] = "Point"
            coords = extract_coordinates(placemark.Point.coordinates.text)[0]
            feature["geometry"]["coordinates"] = coords
        elif hasattr(placemark, 'LineString'):
            feature["geometry"]["type"] = "LineString"
            coords = extract_coordinates(placemark.LineString.coordinates.text)
            feature["geometry"]["coordinates"] = coords
        elif hasattr(placemark, 'Polygon'):
            feature["geometry"]["type"] = "Polygon"
            outer_boundary = extract_coordinates(placemark.Polygon.outerBoundaryIs.LinearRing.coordinates.text)
            feature["geometry"]["coordinates"].append(outer_boundary)
            if hasattr(placemark.Polygon, 'innerBoundaryIs'):
                inner_boundary = extract_coordinates(placemark.Polygon.innerBoundaryIs.LinearRing.coordinates.text)
                feature["geometry"]["coordinates"].append(inner_boundary)

        geojson["features"].append(feature)

    with open(json_file, 'w') as f:
        json.dump(geojson, f, indent=2)

    print(f"Converted {kml_file} to {json_file} successfully.")

if __name__ == "__main__":
    kml_file_path = 'input.kml'
    json_file_path = 'output.json'
    try:
        kml_to_json(kml_file_path, json_file_path)
    except Exception as e:
        print(f"An error occurred: {e}")