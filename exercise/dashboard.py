import logging
import sqlite3
from enum import Enum
from typing import Dict


class Questions(Enum):
    question_one = """
        SELECT
            strains.food_type, 
            COUNT(DISTINCT tubes.strain_id)
        FROM tubes
        INNER JOIN strains ON strains.strain_id = tubes.strain_id
        GROUP BY 1;
    """

    question_two = """
        SELECT
            tubes.freezer, 
            COUNT(DISTINCT tubes.strain_id)
        FROM tubes
        GROUP BY 1;
    """

    question_three = """
        SELECT
            AVG(lactate_concentration)
        FROM tubes
            INNER JOIN strains ON strains.strain_id = tubes.strain_id
            INNER JOIN readings ON readings.tube_id = tubes.tube_id
        WHERE strains.food_type = 'beverage';
    """

    question_four = """
        SELECT
            tubes.strain_id    
        FROM tubes
            INNER JOIN strains ON strains.strain_id = tubes.strain_id
            INNER JOIN readings ON readings.tube_id = tubes.tube_id
        GROUP BY 1
        HAVING acetate_concentration > 0.5;
    """

    question_five = """
        SELECT
            food_retail_source, 
            AVG(acetate_concentration)
        FROM tubes
            INNER JOIN strains ON strains.strain_id = tubes.strain_id
            INNER JOIN readings ON readings.tube_id = tubes.tube_id
        GROUP BY 1;
    """


def run_query(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()


def get_dashboard_data(sqlite_filepath: str) -> Dict:
    """Given the path to a sqlite file, query the database to answer the five
    questions above and return those answers in a dictionary."""
    conn = sqlite3.connect(sqlite_filepath)
    answers = {}
    for question in Questions:
        answers[question.name] = run_query(conn, question.value)

    return answers


def main():
    answers = get_dashboard_data("experiments.db")
    logging.info(answers)


if __name__ == "__main__":
    main()
