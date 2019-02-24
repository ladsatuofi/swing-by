import urllib.request

import os.path
import json
import datefinder
import location_extractor as loc
from bs4 import BeautifulSoup


def filter_by_year(date):
    if (date.year != 2019):
        return False
    else:
        return True


# parse dates
def date_extraction(copy_of_text):
    matches = datefinder.find_dates(copy_of_text)
    matches = list(filter(filter_by_year, matches))
    start_date = matches[0]
    end_date = matches[0]
    for date in matches:
        if date < start_date:
            start_date = date
        if date > end_date:
            end_date = date
    return (start_date, end_date)


def location_extraction(text):
    matches = loc.extract_locations_from_text(text)
    for match in matches:
        if match_location_to_building(match) is not None:
            return match_location_to_building(match)


def retrieve_buildings():
    response = urllib.request.urlopen('http://fs.illinois.edu/about-us/building-list-by-building-number')
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    buildings = dict()
    for link in soup.find_all('tr'):
        for key in link.attrs:
            if key == 'height':
                count = 0
                building_name = ''
                for element in link.find_all('td'):
                    count += 1
                    if count == 2 and element.string is not None and element.string.strip() != '' and type(
                            element.find('p')) == type(element.find('hfjhefb')):
                        building_name = element.string.strip()
                    elif count == 3 and element.string is not None and element.string.strip() != '' and type(
                            element.find('p')) == type(element.find('hfjhefb')):
                        buildings[building_name] = element.string.strip()
    # because there's random <p> tags for these buildings ? ? ?
    del buildings['']
    buildings['CERL – Plant/Soil Response Facility'] = '2902 Newmark Drive'
    buildings['Golf Turf Care Center'] = '2010 South Wright Street'
    buildings['Grounds Shed'] = 'Adjacent to 501 E. Daniels St.'
    buildings['Siebel Center for Design'] = '1208 S. Fourth'
    return buildings


def match_location_to_building(location):
    for building_name in retrieve_buildings().keys():
        if building_name.lower().__contains__(location.lower()):
            return (building_name, retrieve_buildings()[building_name])


if __name__ == '__main__':
    if os.path.exists("data.json"):
        with open("data.json") as f:
            categories = json.load(f)
        # otherwise, create the file by scraping the UIUC building list
    else:
        buildings = retrieve_buildings()
        with open("data.json", "w") as f:
            json.dump(buildings, f)