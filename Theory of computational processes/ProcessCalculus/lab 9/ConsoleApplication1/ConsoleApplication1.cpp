#include <iostream>
#include <thread>
#include <cmath>
#include <mutex>
#include <chrono>
#include <vector>

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


void calculatePIinThreads(double& pi, int k, const int n, const int threadsCount) {
    pi = 0;
    int count = n / threadsCount;
    vector<thread*> threads(threadsCount);
    vector<double> ans(threadsCount);
    for (int i = 0; i < threadsCount; i++) 
        threads[i] = new thread(f1, ref(ans[i]), k + count * i, count * (i + 1));
    
    for (int i = 0; i < threadsCount; i++)
        threads[i]->join();
    
    for (int i = 0; i < threadsCount; i++)
        pi += ans[i];

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
    calculatePIinThreads(pi, k, n, 4);
    cout << endl;
    cout << endl;
    cout << "Many threads " << endl;
    print_dt(t1);
    cout << pi;
}
