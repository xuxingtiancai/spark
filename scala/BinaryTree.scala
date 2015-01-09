
package case_class

object BinaryTree extends App {
abstract class BinaryTree[+T]
case object Empty extends BinaryTree[Nothing]
case class RootNode[T](value : T, left : BinaryTree[T], right : BinaryTree[T]) extends BinaryTree[T]

def preTravel[T](bt: BinaryTree[T]): List[T] = bt match {
  case Empty => List()
  case RootNode(value, l, r) => List(value):::preTravel(l):::preTravel(r)
}

//main
val left = RootNode(2, Empty, Empty)
val right = RootNode(3, Empty, Empty)
val bt = RootNode(4, left, right)
println(preTravel(bt))
}
