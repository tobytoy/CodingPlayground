#include <iostream>
#include <string> 
#include <set>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int max = 0;
        set<char> set;
        
        for (int i=0; i < s.size() ; i++){
            if ( (i+max) > s.size() ) break;

            set.clear();
            for (int j=i; j<(i+max); j++) set.insert( s[j] );
            
            if (max == set.size()){
                for (int j=(i+max); j<s.size(); j++ ){
                    auto pos = set.find( s[j] );
                    if(pos == set.end()){
                        set.insert(s[j]);
                        max++;
                    }else{
                        break;
                    }
                }
            }
        }
        
        return max;
    }
};


int main() {
    string s = "pwwkew";
    int output;

    Solution solution;
    output = solution.lengthOfLongestSubstring(s);

    cout << "output: " << output << endl;
    
    return 0;
}



