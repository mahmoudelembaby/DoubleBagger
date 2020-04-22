import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://mahmoud@localhost:5432/doublebagger')

posts = pd.read_sql('select * from post_post', engine)

companies = pd.read_sql('select * from post_company', engine)

posts_companies = pd.merge(
    companies, posts, left_on='id', right_on='company_id')

posts_companies
