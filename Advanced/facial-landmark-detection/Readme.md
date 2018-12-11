##  1.  Install Dlib prequisites

The dlib library has 4 primary prerequisites
1.  **Boost**: Boost is a collection of peer-reviewed (i.e., very high quality) C++ libraries that help programmers not get caught up in reinventing the wheel. Boost provides implementations for linear algebra, multithreading, basic image processing, and unit testing, just to name a few.

2.  **Boost.Python**: As the name of this library suggests, Boost.Python provides interoperability between the C++ and Python programming language.

3.  **CMake**: CMake is an open-source, cross-platform set of tools used to build, test, and package software. You might already be familiar with CMake if you have used it to compile OpenCV on your system.

4.  **X11/XQuartx**: Short for “X Window System”, X11 provides a basic framework for GUI development, common on Unix-like operating systems. The macOS/OSX version of X11 is called XQuartz.


####  Ubuntu

>   If you didn't install pip use:
    > -   $ wget https://bootstrap.pypa.io/get-pip.py
    > -   $ sudo python get-pip.py

```
$ sudo apt-get install build-essential cmake
$ sudo apt-get install libgtk-3-dev
$ sudo apt-get install libboost-all-dev
```

##  2.  Install dlib with python bindings

Its recommended to use following with dlib for any type of Computer vision or image processing work.

-   Numpy
-   Scipy
-   scikit-image
```
$ pip install numpy
$ pip install scipy
$ pip install scikit-image
```

Now Install dlib
```
$ pip install dlib
```
This command will download the dlib package from PyPI, automatically configure it via CMake, and then compile and install it on your system.


##  3.  Test dlib is installed

open python shell( make sure you are using virtual environment )

```
$ python
Python 3.6.0 (default, Mar  4 2017, 12:32:34) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import dlib
>>> import cv2
>>> cv2.__version__
'3.4.3'
>>>
```

####    Congrats you successfully installed 'dlib' 