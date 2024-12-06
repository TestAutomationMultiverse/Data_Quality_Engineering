from src.connectors import connect_to_database, fetch_data
from src.validators import validate_row_count, validate_column_completeness, validate_data_integrity

def test_data_migration(source_config, target_config, validation_criteria):
    source_conn = connect_to_database(source_config)
    target_conn = connect_to_database(target_config)

    source_data = fetch_data("SELECT * FROM table_name", source_conn)
    target_data = fetch_data("SELECT * FROM table_name", target_conn)

    results = {}
    if "row_count" in validation_criteria:
        results["row_count"] = validate_row_count(source_data, target_data)
    if "column_completeness" in validation_criteria:
        results["column_completeness"] = validate_column_completeness(source_data, target_data)
    if "data_integrity" in validation_criteria:
        results["data_integrity"] = validate_data_integrity(source_data, target_data)

    return results
