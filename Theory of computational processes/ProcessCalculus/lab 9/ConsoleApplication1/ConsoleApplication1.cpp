#include <iostream>
#include <thread>
#include <cmath>
#include <mutex>
#include <chrono>

using namespace std;

using chrono::system_clock;
using Time = decltype (chrono::system_clock::now());

void print_dt(Time t0) {
    auto t1 = system_clock::now();
    cout << "dt = " << chrono::duration_cast<chrono::milliseconds>(t1 - t0).count() << "ms" << endl;
}

void calculatePI(double& pi, int k, const int n) {
    pi = 0;
    while (k < n) {
        pi += (pow(-1., k) / pow(1024., k))
            * (
                -1 * 32. / (4. * k + 1)
                - 1. / (4. * k + 3)
                + 256. / (10. * k + 1)
                - 64. / (10. * k + 3)
                - 4. / (10. * k + 5)
                - 4 / (10. * k + 7)
                + 1. / (10. * k + 9)
                );
        k++;
    }
    pi *= 1 / (pow(2., 6));
}

void f1(double& v, int k, int n) {
    v = 0;
    while (k < n) {
        v += (pow(-1., k) / pow(1024., k))
            * (
                -1 * 32. / (4. * k + 1)
                - 1. / (4. * k + 3)
                + 256. / (10. * k + 1)
                - 64. / (10. * k + 3)
                - 4. / (10. * k + 5)
                - 4 / (10. * k + 7)
                + 1. / (10. * k + 9)
                );
        k++;
    }
}


void calculatePIinThreads(double& pi, int k, const int n) {
    pi = 0;
    double _f1, _f2, _f3, _f4;
    int count = n / 4;
    thread t1(f1, ref(_f1), k, count);
    thread t2(f1, ref(_f2), k + count, count * 2);
    thread t3(f1, ref(_f3), k + count * 2, count * 3);
    thread t4(f1, ref(_f4), k + count * 3, count * 4);
    t1.join();
    t2.join();
    t3.join();
    t4.join();
    pi += _f1 + _f2 + _f3 + _f4;
    pi *= 1 / (pow(2., 6));
}


int main()
{
    int k = 0;
    int n = 10000000;
    double pi = 1;
    auto t0 = system_clock::now();
    thread thr(calculatePI, ref(pi), k, n);
    thr.join();
    cout << "One thread " << endl;
    print_dt(t0);
    cout << pi;

    auto t1 = system_clock::now();
    calculatePIinThreads(pi, k, n);
    cout << endl;
    cout << endl;
    cout << "Many threads " << endl;
    print_dt(t1);
    cout << pi;
}
