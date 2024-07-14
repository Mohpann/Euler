// Connor Hunter

#include <iostream> 
using namespace std; 

/*
Multiples of 3 or 5

Problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5
we get 3, 5 ,6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

natural numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

3: 3 6 9 12
3 % 3 -> 0
12 % 3 -> 0

5: 5 10 15 20
5 % 5 -> 0
20 % 5 -> 0

*/
int main() 
{ 
    int sum = 0;
    for (int num = 1; num < 1000; num++){ // loop through all natural numbers below 1000, starting at 1
        if (num % 3 == 0|| num % 5 == 0){
            sum += num;
        }
    }
    cout << sum;
    return 0; 
}