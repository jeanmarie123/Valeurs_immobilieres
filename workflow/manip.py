
import duckdb 
import pandas

con = duckdb.connect(database = "database/real_estate.db", read_only = False)
df_data = con.execute("SELECT * FROM zone_geographique").df()


