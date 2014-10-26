from pyspark import SparkContext
sc = SparkContext(appName='SparkSql')

from pyspark.sql import *
sqlContext = SQLContext(sc)

def registerTable(contentObj, schmeaList, tableName):
    lines = sc.parallelize(contentObj)
    parts = lines.map(lambda l: tuple(l.split(',')))
    
    fields = [StructField(field_name, StringType(), True) for field_name in schmeaList]
    schema = StructType(fields)

    schemaTable = sqlContext.applySchema(parts, schema)
    schemaTable.registerTempTable(tableName)


def initialTable():
    registerTable(['a,10', 'b,20', 'c,5', 'c,10'], 'name age'.split(), 'peopleAge')
    registerTable(['a,SE', 'b,QE'], 'name career'.split(), 'peopleCareer')
 

def with_filter():
    results = sqlContext.sql('SELECT * FROM peopleAge where age>10')
    for i in results.collect():
        print i


def with_aggr():
    results = sqlContext.sql('SELECT name,sum(age) FROM peopleAge group by name')
    for i in results.collect():
        print i


def with_join():
    results = sqlContext.sql('SELECT a.name,age,career FROM peopleAge a join peopleCareer b on a.name=b.name')
    for i in results.collect():
        print i

if __name__ == '__main__':
    initialTable()
    #with_filter()
    #with_aggr()
    with_join()
