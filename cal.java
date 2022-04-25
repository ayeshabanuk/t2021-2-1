class cal
{
	public static void main(String[] args)
	{
	    int num1 = 10;
		int num2 = 30;
		int sum = add(num1,num2);
		int sub = sub(num1,num2);
		int div = div(num1,num2);
		int mul = mul(num1,num2);
		System.out.println(+div);
		System.out.println(+mul);
	}
	public static int add(int num1,int num2)
	{
		return num1 + num2;
		System.out.println(+sum);
	}
	public static int sub(int num1,int num2)
	{
		return num1 - num2;
		System.out.println(+sub);
	}
	
	public static int div(int num1,int num2)
	{
		return num1 / num2;
	}
	public static int mul(int num1,int num2)
	{
		return num1 * num2;
	}
}
