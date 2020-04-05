#include<bits/stdc++.h>
#include<algorithm>
using namespace std;
#define double      long double

#define lb(v,n)     lower_bound(all((v)),(n))
#define ub(v,n)     upper_bound(all((v)),(n))
       
#define vi          vector<int>
       
#define fi          first
#define se          second
#define mp          make_pair
#define all(a)      (a).begin(),(a).end()
#define rall(a)     (a).rbegin(),(a).rend()
       
#define rep(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define reps(X,S,Y) for (int (X) = S;(X) < (Y);++(X))
#define rrep(X,Y) for (int (X) = (Y)-1;(X) >=0;--(X))
#define rreps(X,S,Y) for (int (X) = (Y)-1;(X) >= (S);--(X))
#define repe(X,Y) for ((X) = 0;(X) < (Y);++(X))
#define toit ios::sync_with_stdio(0);cin.tie(0);
       
int gcd(int a, int b) 
{  
    if (b == 0)  return a; 
    return gcd(b , a % b); 
}
bool mod(double a,double b) 
{
    return a/b - floor(a/b);
}
       
int occurs(vi v,int n)
{
    auto it=lb(v,n);
    auto it1=ub(v,n);
    int x=it1-it;
    return x;}
       
double max(double a,double b){
    return a<b ? b:a;
}

int main()
{toit
    int t;
    cin>>t;
    int tc=0;
    string b;
    cin>>b;
   
    while(t--)
    {
        tc++;
        char in;
        string ans="";
        rep(i,10) ans+= "0";
        reps(i,1,11)
        {
            cout << i << '\n';
            cout.flush();
            cin>>in;
            ans[i-1]=in;
        }
        cout << ans << '\n';
        cout.flush();
        char fin;
        cin >> fin;
        if(fin == 'Y') continue;
        else return 0;
    }
    return 0;
}