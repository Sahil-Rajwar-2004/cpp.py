# ***cpp.py***

## compile and run C++ files in python environment :) 

## Installation

```bash
git clone "https://github.com/Sahil-Rajwar-2004/cpp.py.git"
cd cpp.py
python setup.py sdist bdist_wheel
cd dist
pip install <wheel-file>
```

### Example

```python3
from cpp import CPP

src_code = """
#include <iostream>
using namespace std;

int main(){
    cout<<"Hello World"<<endl;
    return 0;
}
"""

src = CPP(src_code)
src.compile("hello_world.exe")
src.run("hello_world.exe")
```

### Output 

```bash
g++ (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

compilation successful.

Hello World
```

## License

### MIT

