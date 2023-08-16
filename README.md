# Generate commodity codes for Single Trade Window Guidance Service

## Implementation steps

- Create and activate a virtual environment, e.g.

  `python -m venv venv/`
  `source venv/bin/activate`

- Install necessary Python modules via `pip install -r requirements.txt`

## Usage

### To generate codes
`python get_commodities.py`

### Operation

This application:

- cycles through the Online Trade Tariff's goods_nomenclatures APIs to retrieve a list of all commodity codes
- pulls out all of the declarable commodities and their ancestry
- adds to a codes.json file for inclusion on STWGS
