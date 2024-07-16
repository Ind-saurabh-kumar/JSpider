

public class Obj {
    

    // It is a class it self


    
    public static void main(String []args){
        // It is main method of the class

        Obj total = new Obj();

        System.out.println("The sum of two number is: "+total.sum(10,20));

        
    }

    int sum(int a , int b){
        int num1=a;
        int num2=b;
        int tot=num1+num2;
        return tot;
    }

}
