
package case_class

import scala.util.parsing.combinator._

class Arith extends JavaTokenParsers {
def compose(t: Double, list: List[String~Double]): Double = list match {
  case Nil => t
  case ("+"~e) :: next => compose(t+e, next)
  case ("-"~e) :: next => compose(t-e, next)
  case ("*"~e) :: next => compose(t*e, next)
  case ("/"~e) :: next => compose(t/e, next)
  case List(_) => throw new RuntimeException("input error") 
}
def expr: Parser[Double] = term~rep("+"~term | ""~term) ^^ {
  case t~list => compose(t, list)
}
def term: Parser[Double] = factor~rep("*"~factor | "/"~factor) ^^ {
  case t~list => compose(t, list)
}
def factor: Parser[Double] = (
      floatingPointNumber ^^ (_.toDouble)
    | "("~>expr<~")"
)
}

object ParseExpr extends Arith {
def main(args: Array[String]) {
println(parseAll(expr, "2 * (3 + 7) + 3"))
}
}
