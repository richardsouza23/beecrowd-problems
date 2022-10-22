#include <iostream>
using namespace std;

int main(){
    int num_msgs = 0;
    cin >> num_msgs;
    cin.ignore(256, '\n');

    for(int i = 0 ; i < num_msgs ; i++){
        char text[51];
        cin.getline(text, 51);

        char c, c_old = ' ';

        int j = 0;
        while ((c = text[j++]) != '\0'){
            if (c != ' ' && c_old == ' '){
                cout << c;
            }

            c_old = c;
        }

        cout << endl;
    }

    return 0;
}