// Connor Hunter
// 2/15/24
// Return to coding in c++ warmup
// Project Euler's Problem 2
#include <iostream>
using namespace std;
/*
Problem 2:

Even Fibonnaci Numbers

Each new term in the Fibonacci sequence is generated by adding 
the previous two terms. By starting with 1 and 2, the first
10 terms will be:
1,2,3,5,8,13,21,34,55,89,...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms
*/

int main(){
    int first, sum = 0;
    int second = 1;
    while (second < 4000000){
        first = second + first; // calculate new n-1 value
        second = first + second; // calculate new n value

        if (first % 2 == 0){ // if first is even -> add to running sum
            sum += first;
        }
        else if (second % 2 == 0){ // if secon dis even -> add to running sum
            sum += second;
        }

    }
    cout << "F(n-1): " << first << endl;
    cout << "F(n): " << second << endl;

    cout << "Sum: " << sum << endl;
}  

/*
0 1
1 2
*/