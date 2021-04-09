#include "mainwindow.h"
#include "ui_mainwindow.h"

using namespace std;


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    // Создадим обхект для управления потоком
    this->th = new QThread( this );

    // Объект, который будет выполнять вычисления (в том числе в отдельном потоке)
    this->worker = new Worker( );
    // Он должен быть "сам по себе" (указатель на владельца не передаётся в конструктор),
    // чтобы его можно было перекинуть на другой поток


    // Запуск потока должен запустить вычисления в классе
    connect(th, &QThread::started, worker, &Worker::process);

    connect(worker, &Worker::finished, th, &QThread::quit);
    // остановка потока показывает рузультат
    connect(worker, &Worker::finished, this, &MainWindow::update_result);

    // нужно показывать, что идут вычисления
    connect(worker, &Worker::started, this, &MainWindow::show_process);


}

MainWindow::~MainWindow()
{
    delete worker;
    delete ui;
}

void MainWindow::on_btnCalculate_clicked()
{
    int n = pow(10, this->ui->spinBox->value());

    worker->set_param(n);
    worker->moveToThread(th);

    th->start();

}


void MainWindow::update_result(){
    ui->lineEdit->setText(QString::number(worker->get_result()));
}



void MainWindow::show_process(){
    ui->lineEdit->setText("Идут вычисления..");
}


void MainWindow::on_pushButton_clicked()
{
    int n = pow(10, this->ui->spinBox->value());

    worker->set_param(n);
//    worker->moveToThread(QApplication::instance()->thread());
    worker->process();

}
