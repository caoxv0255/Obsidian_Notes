#include <iostream>
using namespace std;

int main() {
	int A[1000]={};
    int n, m, i=1, j=0, max, temp, a_i;
    cin >> n >> m;
    
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    
    for (int i = 0; i < n; i++) {
		
		temp=0;
        
        for (int j = i; j < i + m; j++) {
            temp += A[j];
    	}
    	
        if (max < temp) max=temp;
        
    }
    
    cout<<"max="<< max;
    
    return 0;
}
