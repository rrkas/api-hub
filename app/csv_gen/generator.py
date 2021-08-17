import csv
import os
import uuid

from faker import Faker

from app.config import conf

out_path = os.path.join(conf.OUTPUT_DIR, "csv")


def generate(schema: dict, count: int) -> str:
    f = Faker()
    file_name = "abcd"  # uuid.uuid4().hex
    file_path = os.path.join(out_path, file_name + ".csv")
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for k, v in schema.items():
            if v not in dir(f):
                del schema[k]
        writer.writerow(list(schema.keys()))
        for i in range(count):
            t = []
            for v in schema.values():
                x = eval(f"f.{v}()")
                t.append(x)
            writer.writerow(t)
        file.close()
    return file_name
