
import java.io.*;
import java.util.*;
public class tree1<Type>{
 Type data;
tree1 left;
tree1 right;
public tree1(Type data){
this.left=null;
this.right=null;
this.data=data;
System.out.println("Node added :"+data);

};

public void setLeft(tree1 left){

    this.left=left;

    System.out.println("Setting "+data+" on Left Of "+left.data);
}
public void setRight(tree1 right){
    this.right=right;
    System.out.println("Setting "+data+" on right Of "+right.data);
}
public tree1<Type> getLeft(){
    System.out.println("Setting "+data+" on Left Of "+left.data);

    return this.left;
}
public tree1<Type> getRight(){
    System.out.println("Getting "+data+" on right Of "+right.data);
   
    return this.right;
}
public static void printInOrder(tree1 root){
    if(root==null)
    return ;
    printInOrder(root.left);
    System.out.println(root.data);
    printInOrder(root.right);
}
public static void printPreOrder(tree1 root){
    if(root==null)
    return ;
    System.out.println(root.data);
   
    printInOrder(root.left);
    printInOrder(root.right);
}
public static void printPostOrder(tree1 root){
    if(root==null)
    return ;
   
    printInOrder(root.left);
    printInOrder(root.right);
    System.out.println(root.data);
  
}
    public static  void Dfs(tree1 root){
      Stack<tree1>      stack = new Stack<>();
       
        
        stack.push(root);
       while(stack.size()>0){
        tree1 current=stack.pop();
        System.out.println(" Data in stack "+current.data);
        
        System.out.println();
            if(current.right!=null)
{ 
//     System.out.println(" Data in right "+current.right.data);
       
            stack.push(current.right);
// root=root.right;
        }
            if(current.left!=null){
                // System.out.println(" Data in left  "+current.left.data);
       
          stack.push(current.left);
        // root=root.left;     
        }
       }


        
    };
    

public static void main(String ...args){
    tree1 a =new tree1<String>("1");
tree1 b =new tree1<String>("2");
tree1 c =new tree1<String>("3");
tree1 d =new tree1<String>("4");
tree1 e =new tree1<String>("5");
tree1 f =new tree1<String>("6");
tree1 g =new tree1<String>("7");
System.out.println("Try1");

a.setLeft (b);
a.setRight(c);
b.setLeft (d);
b.setRight(e);
c.setRight(g);
g.setLeft(f);
 Dfs(a);
 System.out.println("InOrder");

 printInOrder(a);
 System.out.println("PreOrder");

 printPreOrder(a);
 System.out.println("PostOrder");

 printPostOrder(a);

}
}
