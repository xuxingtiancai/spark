import org.apache.spark._ 
import SparkContext._ 

object WordCount extends App{
val conf = new SparkConf().setAppName("Simple Application").setMaster("local")
val sc = new SparkContext(conf)
val distData = sc.parallelize(Array(1, 2, 3, 4))
val sum = distData.reduce(_ + _)
val map_sum = distData.map(_ * 2).reduce(_ + _)
println(sum, map_sum)
}
