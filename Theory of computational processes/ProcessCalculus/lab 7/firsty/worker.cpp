#include <cmath>
#include "worker.h"

Worker::Worker(QObject *parent):QObject(parent)
{
    n = 0;
    result = 0;

}

void Worker::set_param(unsigned long n){
    this->n = n;
}


void Worker::process(){
    this->result = 0;

    emit started();
    double pi = 0;
        int k = 0;
        int n = this->n;
        while (k < n){
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
    this->result = pi;

    emit finished();
}


double Worker::get_result() const{
    return this->result;
}


Worker::~Worker(){

}
