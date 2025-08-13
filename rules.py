sepp_rules = {
    "shed": {
        "max_area": 20,
        "max_height": 3,
        "min_lot_size": 300,
        "clause_refs": ["SEPP 2008 - Clause 2.1", "Clause 2.4(1)"]
    },
    "patio": {
        "max_area": 25,
        "max_height": 3.5,
        "min_lot_size": 0,
        "clause_refs": ["SEPP 2008 - Clause 2.1", "Clause 2.5(1)"]
    }
}

def check_exempt(structure_type, width, length, height, lot_size):
    """Compare proposal against SEPP criteria and return structured results."""
    rules = sepp_rules[structure_type]
    area = width * length

    meets_area = area <= rules["max_area"]
    meets_height = height <= rules["max_height"]
    meets_lot_size = lot_size >= rules["min_lot_size"]

    if meets_area and meets_height and meets_lot_size:
        return {
            "result": " Exempt Development",
            "status": "success",
            "explanation": f"Meets SEPP criteria: area ≤ {rules['max_area']} m², "
                           f"height ≤ {rules['max_height']} m, lot size ≥ {rules['min_lot_size']} m².",
            "clauses": rules["clause_refs"]
        }
    else:
        failed_criteria = []
        if not meets_area:
            failed_criteria.append(f"area > {rules['max_area']} m²")
        if not meets_height:
            failed_criteria.append(f"height > {rules['max_height']} m")
        if not meets_lot_size:
            failed_criteria.append(f"lot size < {rules['min_lot_size']} m²")

        return {
            "result": " Requires Development Application",
            "status": "error",
            "explanation": "Fails SEPP criteria: " + ", ".join(failed_criteria),
            "clauses": rules["clause_refs"]
        }
