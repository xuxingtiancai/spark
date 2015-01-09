package case_class

object ReverseList extends App {
def reverse[T](list: List[T]): List[T] = {
  var result : List[T] = Nil
  for(t <- list) {
    result = t :: result
  }
  result
}

//main
val l = List(2, 3, 4)
println(reverse(l))
}
