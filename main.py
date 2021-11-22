import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from libs.etl.Transform import Transform


def main():
    schema = 'buildings_history'
    db = 'dwhe'
    con = Transform('snowflake', db, schema)

    results = con.manual_sql('select * from dwadmin.buildings limit 10;')

    print(results)
    

if __name__ == '__main__':
    main()