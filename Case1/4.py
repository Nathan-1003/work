from dash import Dash, dash_table
import pandas as pd

db_connection_str = 'mysql+pymysql://root:oh_my_ody!@34.142.180.39:13306/data_center'

#db_connection = create_engine(db_connection_str)
df = pd.read_sql('SELECT channel_id FROM data_center.channel GROUP BY channel_id ORDER BY channel_id', con=db_connection_str)
#df = pd.read_sql('SELECT channel_id,count(*) AS count FROM data_center.channel GROUP BY channel_id ORDER BY channel_id', con=db_connection_str)

print(type(df))
#print(df)

app = Dash(__name__)

app.layout = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])

if __name__ == '__main__':
    app.run_server(debug=True)