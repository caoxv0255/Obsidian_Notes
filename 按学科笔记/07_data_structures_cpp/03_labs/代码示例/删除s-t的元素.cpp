#include<iostream>

using namespace std;

const int MaxSize=100;

template<typename DataType>

class SeqList{
	
	public:
		SeqList();
		SeqList(DataType a[],int n);
		void PrintList();
		void Delete();
	private:
		DataType data[MaxSize];
		int length;
	
};
template<typename DataType>
SeqList<DataType>::SeqList(){
	
	length=0;
	
}

template<typename DataType>
SeqList<DataType>::SeqList(DataType a[],int n){
	
	if(n>MaxSize)throw"illgal";
	for(int i=0;i<n;i++){
		
		data[i]=a[i];
		
	}
	
	length=n;
	
}

template<typename DataType>
void SeqList<DataType>::PrintList(){
	
	for(int i=0;i<length;i++){
		
		cout<<data[i]<<"\t";
		
	}
	
	cout<<endl;
	
}

template<typename DataType>
void SeqList<DataType>::Delete(){
	
	if(length==0) throw"顺序表为空";
	int count=0,temp=0,arr[length];
    for(int i=0;i<length;i++){

     	for(int j=i+1;j<length;j++){
		
		if(data[i]==data[j]){
			
			arr[count]=i;
			count++;
			cout<<arr[count-1];
		}
		
     }
	
	}
	for(int i=0;i<count;i++){
        arr[i]=arr[i]-temp;
		for(int j=arr[i];j<length;j++){
			
			data[j]=data[j+1];
			
		}
		length--;
    	temp++;
	}

}

int main(){
	
	int arr[10]={2,4,6,6,6,10,8,14,18,20};
	SeqList<int> m(arr,10);
	m.PrintList();
	m.Delete();	
	m.PrintList();
}