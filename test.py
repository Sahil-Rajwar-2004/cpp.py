from cpp import CPP

src_code = """#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int x;
    cin >> x;
    cout<<pow(x,2)<<endl;
    return 0;
}
"""

src = CPP(src_code)
src.compile("power.exe",True)
src.run("power.exe")

