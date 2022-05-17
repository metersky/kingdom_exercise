from dataclasses import dataclass

from utils import abs_path_from_rel_path


@dataclass
class BaseDataset:
    file_location: str
    table_name: str
    insert_statement: str


tubes = BaseDataset(
    file_location=abs_path_from_rel_path("../data/tubes.csv"),
    table_name="tubes",
    insert_statement="""
        INSERT INTO tubes (
                tube_id,
                strain_id,
                tube_type,
                tube_size,
                freezer        
                ) VALUES (?, ?, ?, ?, ?);
    """,
)

readings = BaseDataset(
    file_location=abs_path_from_rel_path("../data/readings.csv"),
    table_name="readings",
    insert_statement="""
        INSERT INTO readings (
                reading_id,
                tube_id,
                lactate_concentration,
                acetate_concentration
                ) VALUES (?, ?, ?, ?);
    """,
)


strains = BaseDataset(
    file_location=abs_path_from_rel_path("../data/strains.csv"),
    table_name="strains",
    insert_statement="""
        INSERT INTO strains (
            strain_id,
            food_type,
            food_name,
            food_production_source,
            food_retail_source
                ) VALUES (?, ?, ?, ?, ?);
    """,
)
