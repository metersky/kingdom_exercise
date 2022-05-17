import sqlite3

import pandas as pd


def main():
    conn = sqlite3.connect("experiments.db")
    query = """
        SELECT
            readings.tube_id, 
            strains.food_type,
            AVG(lactate_concentration) AS avg_lactate_concentration
        FROM tubes
            INNER JOIN strains ON strains.strain_id = tubes.strain_id
            INNER JOIN readings ON readings.tube_id = tubes.tube_id
        GROUP BY 1, 2;
    """
    df = pd.read_sql_query(query, conn)
    plt = df.plot(x="food_type", y="avg_lactate_concentration", kind="scatter")
    fig = plt.get_figure()
    fig.savefig("output.png")


if __name__ == "__main__":
    main()
