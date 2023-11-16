from flask import jsonify
from tinydb import Query

from validator import FIELDS, is_valid, validate


def get_form_name(db, data):
    fields = list(data.keys())
    if fields:
        search_query = Query()[fields[0]].exists()

        # Dynamically extend the query
        for key in fields[1:]:
            search_query &= Query()[key].exists()

        filtered = db.search(search_query)

        form_name = set([row["name"] for row in filtered])
        return list(form_name)


def process_form(db, data):
    """Validate POST data and retrieve form"""
    status, processed_data = validate(data)
    if is_valid(status):
        forms = get_form_name(db, processed_data)
        if forms:
            return jsonify(forms), 200
        else:
            return jsonify(_type_field(processed_data)), 200
    return jsonify(processed_data), 400


def _type_field(data: dict) -> dict:
    data_to_validate = {
        key: f"{field}_type" for key in data for field in FIELDS if field in key
    }
    return data_to_validate
