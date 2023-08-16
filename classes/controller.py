import requests
import json
import os
from classes.section import Section


class Controller(object):
    def __init__(self):
        self.url_template = "https://www.trade-tariff.service.gov.uk/api/v2/goods_nomenclatures/section/{section_id}"
        self.make_folders()
        self.get_hidden_commodities()

    def make_folders(self):
        self.resources_folder = os.path.join(os.getcwd(), "resources")
        self.codes_folder = os.path.join(self.resources_folder, "codes")
        self.hidden_commodities_folder = os.path.join(
            self.resources_folder, "hidden_commodities")
        os.makedirs(self.codes_folder, exist_ok=True)

    def get_hidden_commodities(self):
        filename = os.path.join(self.hidden_commodities_folder, "hidden_commodities.json")
        f = open(filename)
        self.hidden_commodities = json.load(f)
        f.close()

    def scrape_sections(self):
        self.commodities = []
        for section_id in range(1, 22):
            message = "Collecting data from section {section_id}".format(
                section_id=section_id
            )
            print(message)
            url = self.url_template.format(
                section_id=section_id
            )
            response = requests.get(url)
            section = Section(response.json(), self.hidden_commodities)
            self.commodities += section.declarable_commodities

    def write_stw_codes_file(self):
        print("Writing data to codes.json")
        filename = os.path.join(self.codes_folder, "codes.json")
        file = open(filename, "w")
        json.dump(self.commodities, file, indent=4)
        file.close()
        print("Done")
