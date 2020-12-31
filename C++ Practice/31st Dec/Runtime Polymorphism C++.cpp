#include <iostream>
using namespace std;

class A
{
	public:
	A(int x,int y)
	{
		a = x;
		b = y;
	}
	
	virtual void fun() = 0;
	
	protected:
	int a,b;	
};

class B : public A
{
	public:
	B(int x=0, int y=0) : A(x,y)
	{
		
	}
	
	void fun()
	{
		cout<<"Class B "<<a + b<<endl;
	}
};

class C : public A
{
	public:
	C(int x=0, int y=0) : A(x,y)
	{
		
	}
	
	void fun()
	{
		cout<<"Class C "<<a - b<<endl;
	}
};

int main() {
	A* obja;
	B objb(10,5);
	C objc(10,5);
	obja = &objb;
	obja->fun();
	obja = &objc;
	obja->fun();
	return 0;
}
