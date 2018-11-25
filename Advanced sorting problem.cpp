#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);
/////////////
long getSum(vector<int> &BITree, long index) 
{ 
    long sum = 0; 
    while (index > 0) 
    { 
        sum += BITree[index];  
        index -= index & (-index); 
    } 
    return sum; 
} 
  
void updateBIT(vector<int> &BITree, int n, long index, int val) 
{ 
    while (index <= n) 
    { 
       BITree[index] +=val; 
       index += index & (-index); 
    } 
} 
  
// Returns inversion count arr[0..n-1] 
long insertionSort(vector<long> arr)
{ 
    long invcount = 0; // Initialize result 
    int n = arr.size();
 
    long maxElement = *max_element(arr.begin(), arr.end()); 
    vector<int> BIT(maxElement+1,0);
    
    for (int i=n-1; i>=0; i--) 
    { 
        invcount += getSum(BIT, arr[i]-1); 
        updateBIT(BIT, maxElement, arr[i], 1); 
    } 
   cout << invcount <<endl;
   return invcount; 
} 
  

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    
    int n;
    string arr_temp_temp;
    vector<string> arr_temp;
    for (int t_itr = 0; t_itr < t; t_itr++) {
        
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        getline(cin, arr_temp_temp);
        
        arr_temp = split_string(arr_temp_temp);
        vector<long> arr(n);
        for (int i = 0; i < n; i++) {
            arr[i] = stoi(arr_temp[i]);
        }

        //long result = insertionSort(arr);
        fout << insertionSort(arr) << "\n";
    }

    fout.close();

    return 0;
}
