#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <thread>
#include <QThread>
#include <cmath>
#include "worker.h"


QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_btnCalculate_clicked();
    void update_result();
    void show_process();

    void on_pushButton_clicked();

private:
    Ui::MainWindow *ui;

    // поток для отдельных вычислений
    QThread *th;
    // класс выполняющий отдельные вычисления
    Worker *worker;

signals:
    void started();
    void finished();
};
#endif // MAINWINDOW_H
