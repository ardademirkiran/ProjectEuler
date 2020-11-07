#include <iostream>
#include <cmath>

using namespace std;
int isPrime(int num){
 if(num%2 == 0){
  return 0;
 }
 for(long long i = 3; i <= (pow(num,0.5)); i+=2){
  if(num%i == 0){
   return 0;
  }
 }
 return 1;
}



int main(){
 long sum = 0;
 for(int x=3;x<=2000000;x++){
  if(isPrime(x) == 1){
   cout<<x<< " Asal bir sayıdır.\n";
   sum += x;
  } 
 }
 cout <<sum+2 << endl;
 return 0;
}
