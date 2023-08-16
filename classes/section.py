from classes.commodity import Commodity


class Section(object):
    def __init__(self, section_json, hidden_commodities):
        self.json = section_json
        self.hidden_commodities = hidden_commodities
        self.parse_section()
        self.get_ancestry()
        self.extract_data()

    def parse_section(self):
        self.commodities = {}
        for entity in self.json["data"]:
            commodity = Commodity(entity)
            self.commodities[commodity.goods_nomenclature_sid] = commodity

    def get_ancestry(self):
        for commodity in self.commodities:
            commodity_object = self.commodities[commodity]
            parent_sid = commodity_object.parent_sid
            is_chapter = commodity_object.is_chapter
            while parent_sid is not None and is_chapter is False:
                id = parent_sid
                parent_sid = self.commodities[id].parent_sid
                is_chapter = self.commodities[id].is_chapter
                description = self.commodities[id].description
                if parent_sid is not None and is_chapter is False:
                    self.commodities[commodity].ancestral_descriptions.insert(
                        0, description)

    def extract_data(self):
        self.declarable_commodities = []
        for commodity in self.commodities:
            commodity_object = self.commodities[commodity]
            if commodity_object.declarable:
                if commodity_object.goods_nomenclature_item_id not in ["sdhfois"]:  # self.hidden_commodities:
                    self.declarable_commodities.append(
                        self.commodities[commodity].as_dict())
