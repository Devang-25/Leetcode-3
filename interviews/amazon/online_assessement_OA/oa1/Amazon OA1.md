# Amazon OA1

## reverse array

```java			
class SortArray{
  public static int[] reverseArray( int arr[] ) {
    int i, temp, originalLen = arr.length;
    int len = originalLen;
    for( i = 0 ; i < originalLen / 2 ; i++){
      temp = arr[ len - 1 ];
      arr[ len - 1 ] = arr[i];
      arr[i] = temp;
      len -= 1;
    }
    return arr;
  }
}

class Main {
  public static void main(String[] args) {
    // String[] arr_str = {"hello", "world"};
    int[] arr = {1, 2, 3, 4, 5, 6};
    int[] outArr = SortArray.reverseArray(arr);
    System.out.println(Arrays.toString(outArr));
    System.out.println("Hello world!");
  }
}
```

![image-20190218121537109](/Users/sonya/Library/Application Support/typora-user-images/image-20190218121537109.png)

## ![image-20190218121613755](/Users/sonya/Library/Application Support/typora-user-images/image-20190218121613755.png)









## print EvenOddPattern

```java
class Main {
  public static void main(String[] args) {
    int num = 3;
    EvenOddPattern.printPattern(num);
    // System.out.println(Arrays.toString(result));
    System.out.println("Hello world!");
  }
}


class EvenOddPattern{
  static void printPattern( int num ){
    int i, print = 0 ;
    if ( num % 2 == 0 ){
      print = 0;
      for ( i = 0 ; i < num ; i ++ ){
        System.out.print(print + " ");
        print += 2;
      }
    }
    else{
      print = 1;
      for ( i = 0 ; i < num ; i ++){
        System.out.print( print + " " );
        print += 2;
      }
    }
  }
}
```



## printpattern2 : print  a ab abc abcd

```java
public class PrintPattern2{
  public static void print2(int row){
    for (int i = 0 ; i < row ; i++){
      char ch = 'a';
      char print = ch;
      for (int j = 0; j <= i ; j++){
        System.out.println(print++);
      }
    System.out.println(" ");
    }
  }
  public static void main(String[] args){
    print2(4);
  }
}
```





## printpattern3 : print 11 , 1111, 111111 ...

```java
public class PrintPattern3{
    public static void print3(int row){
        int x = 1;
        for (int i = 1 ; i <= row ; i++ ){
            for (int j = i ; j > 0 ; j--){
                System.out.print(x + "" + x);
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args){
        print3(4);
    }
}
```



- 少个一个括号



## Insertionsort

```java
public class InsertionSort{
    public static int[] insertionsort(int[] arr){
        int n = arr.length;
        for (int i = 1 ; i < n ; i++){
            int temp = arr[i];
            int j = i;
            while (j > 0 && arr[j - 1] > temp){
                arr[j] = arr[j - 1];
                j--;
            arr[j] = temp;
            }
        }
    return arr;
    }
    
    
    public static void main(String[] args){
        int[] arr = {3, 2, 4, 1};
        arr = insertionsort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
```



