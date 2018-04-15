import jieba.posseg as pseg
import codecs
from gensim import corpora, models, similarities
import mysql.connector
from pymongo import Connection

con   =   Connection('localhost', 21001)
db    =   con.noonde_api_development
col   =   db.no_sql_airbnb_listings
