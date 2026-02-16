from utils.logger import logger


class DataValidator:
    def __init__(self):
        """Mock Data Validator for AWS DMS Testing"""
        self.source_schema = {
            "id": "int",
            "name": "string",
            "created_at": "timestamp"
        }
        self.target_schema = {
            "id": "int",
            "name": "string",
            "created_at": "timestamp"
        }
        self.target_data = [
            {"id": 1, "name": "Alice", "created_at": "2024-01-29T10:00:00Z"},
            {"id": 2, "name": "Bob", "created_at": "2024-01-29T10:05:00Z"}
        ]

    def check_data_loaded(self):
        """Mock function to check if data is loaded into the target"""
        is_loaded = len(self.target_data) > 0
        logger.info(f"Data loaded into target: {is_loaded}")
        return is_loaded

    def get_duplicate_records(self):
        """Mock function to check for duplicate records in target"""
        seen = set()
        duplicates = 0
        for record in self.target_data:
            record_id = record["id"]
            if record_id in seen:
                duplicates += 1
            seen.add(record_id)

        logger.info(f"Duplicate records found: {duplicates}")
        return duplicates

    def get_schema(self, table_name):
        """Mock function to return schema of a table"""
        schema = self.source_schema if table_name == "source_table" else self.target_schema
        logger.info(f"Schema for {table_name}: {schema}")
        return schema

    def compare_schemas(self):
        """Compare source and target schemas"""
        match = self.source_schema == self.target_schema
        logger.info(f"Schema comparison result: {match}")
        return match

    def validate_cdc_ordering(self, timestamps):
        """Ensure CDC timestamps are in sequential order"""
        is_ordered = timestamps == sorted(timestamps)
        logger.info(f"CDC timestamps in order: {is_ordered}")
        return is_ordered