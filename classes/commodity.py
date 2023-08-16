class Commodity(object):
    def __init__(self, entity):
        self.entity = entity
        self.ancestral_descriptions = []
        self.parse_commodity()

    def parse_commodity(self):
        self.goods_nomenclature_sid = self.entity["id"]
        self.goods_nomenclature_item_id = self.entity["attributes"]["goods_nomenclature_item_id"]
        self.is_chapter = True if self.entity["attributes"]["goods_nomenclature_item_id"][-8:] == "00000000" else False
        self.description = self.entity["attributes"]["formatted_description"]
        self.declarable = self.entity["attributes"]["declarable"]
        self.parent = self.entity["relationships"]["parent"]["data"]
        if self.parent is not None:
            self.parent_sid = self.parent["id"]
        else:
            self.parent_sid = None

    def as_dict(self):
        self.json = {
            "id": self.goods_nomenclature_item_id,
            "description": self.description,
            "sub": self.ancestral_descriptions
        }
        return self.json
