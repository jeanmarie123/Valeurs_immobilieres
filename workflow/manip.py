
import duckdb 
import pandas

con = duckdb.connect(database = "data/real_estate.db", read_only = False)
df_data = con.execute("SELECT * FROM zone_geographique").df()

""" 
def data():
    with duckdb.connect(database = "data/real_estate.db", read_only = False) as con:
       df_data = con.execute("SELECT * FROM zone_geographique").df()
    return df_data 
"""
