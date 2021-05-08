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
double fiveTask(vector<double>& arr, bool isParallel = true) {
    double sum = 0;
    if (isParallel)
        #pragma omp parallel for
        for (int i = 0; i < arr.size(); i++) 
            sum += sqrt(10 + pow(arr[i], 2));
    else
        for (int i = 0; i < arr.size(); i++)
            sum += sqrt(10 + pow(arr[i], 2));
    return sum;
}

void fillVector(vector<double>& arr, int n) {
    for (int i = 0; i < n; i++)
        arr[i] = i + 1;
}

void calculatePI(double& pi, int k, const int n) {
    double sum = 0;
    int k1 = k;
    int k2 = k + 1;
    #pragma omp parallel sections reduction(+:sum)
    {
        #pragma omp section
        {
            while (k1 < n) {
                sum += (pow(-1., k1) / pow(1024., k1))
                    * (
                        -1 * 32. / (4. * k1 + 1)
                        - 1. / (4. * k1 + 3)
                        + 256. / (10. * k1 + 1)
                        - 64. / (10. * k1 + 3)
                        - 4. / (10. * k1 + 5)
                        - 4 / (10. * k1 + 7)
                        + 1. / (10. * k1 + 9)
                        );
                k1 += 2;
            }
        }

        #pragma omp section
        {
            while (k2 < n) {
                sum += (pow(-1., k2) / pow(1024., k2))
                    * (
                        -1 * 32. / (4. * k2 + 1)
                        - 1. / (4. * k2 + 3)
                        + 256. / (10. * k2 + 1)
                        - 64. / (10. * k2 + 3)
                        - 4. / (10. * k2 + 5)
                        - 4 / (10. * k2 + 7)
                        + 1. / (10. * k2 + 9)
                        );
                k2 += 2;
            }
        }
    }

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
    double sum = fiveTask(arr);
    print_dt(t0);
    cout << sum << endl << endl;
    
    cout << "No parallel" << endl;
    auto t1 = system_clock::now();
    sum = fiveTask(arr, false);
    print_dt(t1);
    cout << sum << endl;
    
    double pi;
    int k = 0;
    cout << endl << endl;
    cout << "Parallel PI" << endl;
    auto t2 = system_clock::now();
    // n = 100;
    calculatePI(pi, k, n);
    print_dt(t2);
    cout << pi;
}
