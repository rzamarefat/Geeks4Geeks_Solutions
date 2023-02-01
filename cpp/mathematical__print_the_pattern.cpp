// You a given a number N. You need to print the pattern for the given value of N.

// For N = 2 the pattern will be 
// 2 2 1 1
// 2 1

// For N = 3 the pattern will be 
// 3 3 3 2 2 2 1 1 1
// 3 3 2 2 1 1
// 3 2 1
// ==================================================================

#include <iostream>
using namespace std;

int main(){
    cout << "Please enter N: " << endl;

    short N;
    cin >> N;

    for (int i=0; i<N; i++){
        for (int j=0; j<N; j++){
            for (int x=0; x<N-i; x++){
                cout << N - j;
            }
        }

        cout << endl;
    }
    
    return 0;
}
    







