import csv
import logging
import sqlite3

import dataset_definitions
from utils import abs_path_from_rel_path


def build_database(conn: sqlite3.Connection, schema_definitions_rel_path: str) -> None:
    """Build the database using the schemas defined in `schemas.sql`"""
    with open(schema_definitions_rel_path, "r") as sql_file:
        sql_script = sql_file.read()

    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()


def empty_str_as_none(row: list[str]) -> list[str]:
    return [None if v == "" else v for v in row]


def insert_data(
    conn: sqlite3.Connection, dataset: dataset_definitions.BaseDataset
) -> None:
    """Use the file_location and INSERT statement from
    the dataset dataclasses to INSERT data from .csv files.
    """
    with open(dataset.file_location) as f:
        reader = csv.reader(f)
        # skip the header row
        next(reader)
        cur = conn.cursor()
        for row in reader:
            row = empty_str_as_none(row)
            try:
                cur.execute(dataset.insert_statement, row)
            except sqlite3.IntegrityError as e:
                logging.error(f"IntegrityError: {dataset.table_name} - {e} {row}")
    conn.commit()


def main():
    db_name = "experiments.db"
    conn = sqlite3.connect(db_name)
    # fk constraints are not enabled by default in sqlite, so enable here
    conn.execute("PRAGMA foreign_keys = 1")

    schema_definitions_rel_path = abs_path_from_rel_path("schemas.sql")
    build_database(conn, schema_definitions_rel_path)

    # `tubes` needs to be inserted before `readings` to catch the fk constraint errors
    datasets = [
        dataset_definitions.tubes,
        dataset_definitions.readings,
        dataset_definitions.strains,
    ]
    for dataset in datasets:
        insert_data(conn, dataset)


if __name__ == "__main__":
    main()
