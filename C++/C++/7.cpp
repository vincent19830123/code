#include <iostream>	
void tt(int m, int n);
int main()
{
	using namespace std;

	cout << "Enter the number of hours: ";
	int hour;
	cin >> hour;
	cout << "Enter the number of minutes: ";
	int minute;
	cin >> minute;
	cout << "Time: ";
	tt(hour, minute);
	cout << endl;
	return 0;
}
void tt(int m, int n)
{
	using namespace std;

	cout << m << ":" << n;
}