import java.util.Scanner;
class Voting{
	public static void main(String args[]){
		int age,y;
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter your age: ");
		age=sc.nextInt();
		if(age>17)
			System.out.println("You're eligible to vote");
		else
		{
			y=18-age;
			System.out.println("You can vote after "+ y +" years");
		}
	}
}