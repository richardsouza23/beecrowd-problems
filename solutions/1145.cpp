#include <iostream>
 
using namespace std;
 
int main() {
    int X,Y;
    cin >> X >> Y;
    
    for(int i=1 ; i<=Y ; i++){
        if(i%X==0) cout << i << endl;
        else printf("%i ",i);
    }
    
    return 0;
}