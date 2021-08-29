#include <iostream>
#include <cmath>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        if ( x >= pow(2,31) || x < -pow(2,31) ){
            return 0;
        }else{
            int sign = (x < 0)?-1:1;
            int ans =0;
            while( x ){
                ans = ans * 10 + (x % 10);
                x /= 10;
            }
            ans *= sign;
            return ans;
        }
        
    }
};

int main() {
    int input_x = 123;
    int output;

    Solution solution;
    output = solution.reverse(input_x);


    cout << "output: " << output << endl;
    
    return 0;
}



