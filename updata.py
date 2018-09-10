import psycopg2
import os
import pandas as pd
from sqlalchemy import create_engine
import io
dsn = create_engine('postgresql+psycopg2://postgres:991550sp@localhost/postgres')  # Use ENV vars: keep it secret, keep it safe
#conn = psycopg2.connect(dsn)
conn = dsn.raw_connection()
cur = conn.cursor()
# Do something to create your dataframe here...
df = pd.read_csv("spthrows.csv")
print (df)
output = io.StringIO()
df.to_csv(output, sep='\t', header=False, index=False)
output.seek(0)
contents = output.getvalue()
cur.copy_from(output, 'throwersd', null="") # null values become ''
conn.commit()
# Initialize a string buffer
#sio = StringIO()
#sio.write(df.to_csv(index=None, header=None))  # Write the Pandas DataFrame as a csv to the buffer
#sio.seek(0)  # Be sure to reset the position to the start of the stream

# Copy the string buffer to the database, as if it were an actual file
#with conn.cursor() as c:
#    c.copy_from(sio, "schema.table", columns=dataframe.columns, sep=',')
#    conn.commit()