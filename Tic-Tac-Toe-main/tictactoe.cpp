#include "game.h"
using namespace std;

int main()
{
    int n, m, i, j, k, count;
    string p1, p2, retry;
    char a[9];
    int b, turns=0;
    bool p;

    for (i = 0; i < 9; i++)
        a[i] = i + '1';

    cout <<"\n...\t\tTIC TAC TOE\t\t...\n\t\t\t\tBy: Darshan K S\n\n\t\tPress Enter\n";

    getchar();
    
    cout << "Enter Player 1 name: ";
    cin >> p1;
    cout << "Enter Player 2 name: ";
    cin >> p2;
    cout << endl;
    //
    p = toss(p1, p2);
    
    //
    gui_templ();

    //game logic
    while (!win(a))
    {
        //Checking for draw game
        if(turns==9)
        {
            cout<<"\aGame ends with a draw!\n";
            break;
        }
        //
        //Chance display
        if(p==0)
        {
            cout << "\n "<<p1<< "'s chance. Select the box number: ";
        }
        else
        {
            cout << "\n "<<p2<< "'s chance. Select the box number: ";
        }
        //
        //Array modification on user entry
        cin >> b;
        if (b <= 9 && b > 0)
        {
        if((a[b-1]=='X')||(a[b-1]=='O'))   
        {
            cout<<"\aCannot overwrite. Choose another box: ";
            cin>>b;
        }
        
        while((a[b-1]!='X')&&(a[b-1]!='O'))
        {
            if (p == 0)
            {
                a[b-1] = 'O';
            }
            else
            {
                a[b-1] = 'X';
            }
        }
        }
        else
        {
            cout << "\aPlease enter a valid box.\n";
            turns--;
        }
        //
        gui_run(a, b, p);
        p = !p;
        b=0;
        ++turns;
        //
        //Game end
        if(win(a)==1)
        {
            cout<<"\a\n\t"<<p1<<" won the round!";
        }
        else if (win(a)==2)
        {
            cout<<"\a\n\t"<<p2<<" won the round!";
        }
        //
    }
    //
    //Play again
    {
    cout<<"\nWould you like to play another round?(yes / no): ";
    cin>>retry;
    if(!(retry.compare("yes")))
        main();
    else
        cout<<"\n\tC Ya!\n";
    }
    //

    return 0;
}





