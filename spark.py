import operator

from pyspark import SparkContext
sc = SparkContext(appName='test')


def one2many():
    data = ['a 1,2,3', 'b 4,5,6']
    distData = sc.parallelize(data)
    def parse(line):
        e1, e2 = line.split()
        subs = e2.split(',')
        return [e1 + sub for sub in subs]
    distData = distData.flatMap(parse)
    print distData.collect()

def many2one():
    data = [('a', '1'), ('a', '2')]
    distData = sc.parallelize(data)
    distData = distData.reduceByKey(operator.add)
    print distData.collect()

    data = [('a', '1'), ('a', '2')]
    distData = sc.parallelize(data)
    distData = distData.groupByKey().mapValues(lambda x : ''.join(x))
    print distData.collect()

def ratio():
    data = [('a', 1.), ('a', 2.)]
    distData = sc.parallelize(data)
    distData = distData.groupByKey().mapValues(lambda x : (x, sum(x)))
    distData = distData.flatMapValues(lambda (x,y) : [(i, i/y, y) for i in x])
    print distData.collect()

def useDict():
    data = ['xuxing', 'goushi']
    distData = sc.parallelize(data)
    broadcastVar = sc.broadcast(set(['xuxing']))
    distData = distData.filter(lambda x : x in broadcastVar.value)
    print distData.collect()


if __name__ == '__main__':
    #one2many()
    #many2one()
    ratio()
    #useDict()
