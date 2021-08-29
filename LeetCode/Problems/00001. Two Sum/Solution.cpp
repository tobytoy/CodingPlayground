#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        
        for(int i=0;i<nums.size()-1;i++)
        {
            for(int j=i+1;j<nums.size();j++)
            {
                if(nums[i]+nums[j]==target)
                {
                    ans = {i, j};
                    
                    break;
                }
            }
        }
        
        return ans;
    }
};


int main() {

    vector<int> input_nums = {2,7,11,15};
    int input_target = 9;
    vector<int> output;

    Solution solution;
    output = solution.twoSum(input_nums, input_target);


    cout << "output: ";
    for (const auto &item : output) {
        cout << item << ", ";
    }
    cout << endl;
    
    return 0;
}



