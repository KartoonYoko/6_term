#include <math.h>
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
    double v = 0;
    for (unsigned long i = 1; i <= this->n; i += 4) {  // increment by 4
        v +=  1 / i - 1 / (i + 2); // add the value of the series
    }

    this->result = 4 * v;

    emit finished();
}


double Worker::get_result() const{
    return this->result;
}


Worker::~Worker(){

}
