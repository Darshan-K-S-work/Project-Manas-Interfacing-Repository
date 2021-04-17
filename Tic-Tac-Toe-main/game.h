#include <iostream>
#include <string>
#include <ctime>
#include <stdlib.h>
using namespace std;


//Toss
int toss(string p1, string p2)
{
    srand((unsigned)time(0));
    if ((rand()) % 2)
    {
        cout << p1 << " starts with \"O\"" << endl;
        return 0;
    }
    else
    {
        cout << p2 << " starts with \"X\"" << endl;
       return 1;
    }
}

//Win checker
int win(char a[])
{
    int i, j;
    //rows check
    for(i=0; i<=6; i+=3)
    {
        if((a[i]==a[i+1])&&(a[i+1]==a[i+2])&&(a[i]=='O'))
            return 1;
        else if((a[i]==a[i+1])&&(a[i+1]==a[i+2])&&(a[i]=='X'))
            return 2;
    }//
    //column check
    for(i=0; i<3; i++)
    {
        if((a[i]==a[i+3])&&(a[i+3]==a[i+6])&&(a[i]=='O'))
            return 1;
        if((a[i]==a[i+3])&&(a[i+3]==a[i+6])&&(a[i]=='X'))
            return 2;
    }//
    //Diagonal check
    if((a[0]==a[4])&&(a[4]==a[8])&&(a[0]=='O'))
        return 1;
    else if((a[2]==a[4])&&(a[4]==a[6])&&(a[2]=='O'))
        return 1;
    else if((a[0]==a[4])&&(a[4]==a[8])&&(a[0]=='X'))
        return 2;
    else if((a[2]==a[4])&&(a[4]==a[6])&&(a[2]=='X'))
        return 2;
    
    return 0;
}

//Runtime grid
void gui_run(char a[], int b, bool p)
{
    int n, m, i, j, k, c = 0;

    for (m = 0; m < 16; m++)
        cout << "_ ";
    cout << endl;
    for (k = 0; k < 3; k++)
    {
        for (j = 1; j <= 3; j++)
        {
            for (i = 0; i < 13; i++)
            {
                if ((j == 2) && ((i == 2) || (i == 6) || (i == 10)))
                {
                    if((a[c]=='X')||(a[c]=='O'))
                    {
                        cout<< " "<<a[c]<<" ";
                    }
                    else
                    {
                        cout<<"   ";
                    }
                    ++c;
                    continue;
                }
                if ((i == 4) || (i == 8) || (i == 0) || (i == 12))
                {
                    cout << "|";
                    continue;
                }
                cout << "   ";
            }
            cout << endl;
        }
        for (m = 0; m < 16; m++)
            cout << "_ ";
        cout << endl;
    }
}

//Initial grid
void gui_templ()
{
    int n, m, i, j, k, c = 1;

    for (m = 0; m < 16; m++)
        cout << "_ ";
    cout << endl;
    for (k = 0; k < 3; k++)
    {
        for (j = 1; j <= 3; j++)
        {
            for (i = 0; i < 13; i++)
            {
                if ((j == 2) && ((i == 2) || (i == 6) || (i == 10)))
                {
                    cout << " " << c << " ";
                    ++c;
                    continue;
                }
                if ((i == 4) || (i == 8) || (i == 0) || (i == 12))
                {
                    cout << "|";
                    continue;
                }
                cout << "   ";
            }
            cout << endl;
        }
        for (m = 0; m < 16; m++)
            cout << "_ ";
        cout << endl;
    }
}


