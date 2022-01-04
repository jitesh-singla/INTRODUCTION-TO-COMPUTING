#include <iostream>
#include <cmath>
#include <conio.h>

using namespace std;
class bankaccount
{
    int principal;
    float rate,year;
    
    float calc();

public:
    bankaccount()
    {
        int a;
        float b;
        cout << "enter the amount you want to invest" << endl;
        cin >> a;
        cout << "the no. of year you want to invest " << endl;
        cin >> b;
        principal = a;
        year = b;
    }

    void condition()
    {
        char c;
        rate = 4;
        cout << "the interest rate for this time period is  " << rate << "%" << endl;
        cout << "did you wish to continue (y/n)"<<endl;
        cin >> c;
        if (c == 'y')
        {
            cout << "the intrest on the amount will be " << calc() << endl;
        }
        else
            cout << "session terminated";
    }

    void interest()
    {
        char c;
        if (year == 1)
        {
            condition();
        }
        else if (year > 1)
        {
            rate = 6;
            cout << "the interest rate for this time period is   " << rate << "%" << endl;
            cout << "did you wish to continue (y/n)"<<endl;
            cin >> c;
            if (c == 'y')
            {
                cout << "the intrest on the amount will be " << calc() << endl;
            }
            else
                cout << "session terminated";
        }
        else
            cout << "error 99999";
    }
};
float bankaccount ::calc()
{
    double c;
    c = (principal * year * rate) / 100;

    return c;
}
int main()
{
    bankaccount A;
    A.interest();
    getch();
}