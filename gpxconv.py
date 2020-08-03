import xml.etree.ElementTree as ET
import os
import argparse

unitconv_const = 1.94384
xmlns = "http://www.topografix.com/GPX/1/1"
ns = {'gpx':xmlns}

ET.register_namespace('',xmlns)

parser = argparse.ArgumentParser()
parser.add_argument("gpxin", help="GPX input file to convert")
args = parser.parse_args()

#Check for presence of gpx file
if not os.path.isfile(args.gpxin):
    print("Cannot open " + args.gpxin)
    exit()

with open(args.gpxin, 'r') as f:
    tree = ET.parse(f)
    for point in tree.iter('{'+xmlns+'}trkpt'):
        convspeed = float(point.find('gpx:sog', ns).text) * unitconv_const
        se = ET.SubElement(point, 'speedy')
        se.text = str(convspeed)

    tree.write('output.xml')
  
