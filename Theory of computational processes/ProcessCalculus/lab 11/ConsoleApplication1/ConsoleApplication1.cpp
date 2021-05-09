#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>
#include <omp.h>

using namespace std;

using chrono::system_clock;
using Time = decltype (chrono::system_clock::now());

void print_dt(Time t0) {
    auto t1 = system_clock::now();
    cout << "dt = " << chrono::duration_cast<chrono::milliseconds>(t1 - t0).count() << "ms" << endl;
}

/*
    136o
*/
double fiveTask(vector<double>& arr, const int numThreads) {
    double sum = 0;
    #pragma omp parallel for num_threads(numThreads)
    for (int i = 0; i < arr.size(); i++) 
       sum += sqrt(10 + pow(arr[i], 2));
    return sum;
}

void fillVector(vector<double>& arr, int n) {
    for (int i = 0; i < n; i++)
        arr[i] = i + 1;
}

void calculatePI(double& pi, int k, const int n, int numThreads) {
    double sum = 0;
    #pragma omp parallel for reduction(+ : sum) num_threads(numThreads)
    for (int i = 0; i < n; i++) 
        sum += (pow(-1., i) / pow(1024., i))
            * (
                -1 * 32. / (4. * i + 1)
                - 1. / (4. * i + 3)
                + 256. / (10. * i + 1)
                - 64. / (10. * i + 3)
                - 4. / (10. * i + 5)
                - 4 / (10. * i + 7)
                + 1. / (10. * i + 9)
    );
  

    sum *= 1 / (pow(2., 6));
    pi = sum;
}


int main()
{
    int n = 10000000;
    vector<double> arr(n);
    fillVector(arr, n);
    
    cout << "Parallel" << endl;
    auto t0 = system_clock::now();
    double sum = fiveTask(arr, 2);
    print_dt(t0);
    cout << sum << endl << endl;
    
    cout << "No parallel" << endl;
    auto t1 = system_clock::now();
    sum = fiveTask(arr, 1);
    print_dt(t1);
    cout << sum << endl;
    
    double pi;
    int k = 0;
    cout << endl << endl;
    cout << "Parallel PI" << endl;
    auto t2 = system_clock::now();
    // n = 100;
    calculatePI(pi, k, n, 4);
    print_dt(t2);
    cout << pi;
}
