#include "mat_utils.h"

double dot(const vector<double> &a, const vector<double> &b){
    double s = 0.0;
    int n = (int)a.size();
    for (int i = 0; i < n; i++){
        s += a[i]*b[i];
    } 
    return s;
} // dot

double norm_2(const vector<double> &a){
    return sqrt(dot(a,a);
} // norm_2

double norm_inf(const vector<double>&a){
    double target = 0.0;
    int n = (int)a.size();
    for (int i = 0; i < n; i++){
        if (fabs(a[i]) > target) target = fabs(a[i]);
    }
    return target;
} // norm_inf


void axpy(double a, const vector<double> &x, vector<double> &y){
    int n = (int)x.size();
    for (int i = 0; i < n; i++) y[i] += a * x[i];
} // axpy

void scale(vector<double> &x, double s){
    for (auto &v: x) v *= s;
} // scale
