import json, datetime
import unittest

def validate_record(record):
    try:
        timestamp = record.get("timestamp")


        truck_id = record.get("truck_id")
        if not truck_id or not isinstance(truck_id,str):
            return False, "Invalid or missing truck_id",timestamp

        latitude = record.get("latitude")
        if not isinstance(latitude,float):
            return False, "Invalid latitude",timestamp


        longitude = record.get("longitude")
        if not isinstance(longitude,float):
            return False, "Invalid longitude"

        return True, "Valid",timestamp



    except Exeception as e:
        return False, f"Exeception: {str(e)}", timestamp


def procces_log_file(filepath):
    records = []
    with open(filepath,"r") as file:
        records  = json.load(file)
        print(records)
    
    with open("success.log", "w") as success_log, open("error.log", "w") as error_log:
        for record in records:
            valid, message, timestamp = validate_record(record)
            print(valid, message,timestamp)
            
            truck_id = record.get("truck_id","UNKNOWN")
            timestamp = record.get("timestamp","NO_TIME")
            line = f"{truck_id}| {timestamp}"

            if valid:
                success_log.write(line + "| SUCCESS \n")
            else:
                error_log.write(line + f"| ERROR: {message} \n")


class TestGpsValidation(unittest.TestCase):
    def test_valid_record(self):
        record =  {
        "truck_id": "TRUK123",
        "latitude": 59.437,
        "longitude": 24.7536,
        "timestamp": "2025-04-16T10:05:00Z"
    }

        valid, message, timestamp = validate_record(record)
        self.assertTrue(valid) 
        self.assertEqual(message, "Valid")

    def test_missing_truck_id(self):
        record =  {
            "latitude": 59.437,
            "longitude": 24.7536,
            "timestamp": "2025-04-16T10:05:00Z"
        }
        valid, message, timestamp = validate_record(record)
        self.assertFalse(valid) 
        self.assertEqual(message, "Invalid or missing truck_id")


procces_log_file("log_input.json")
unittest.main()
