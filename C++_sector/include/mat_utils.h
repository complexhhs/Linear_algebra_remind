#pragma once 
#include "common_include.h"

#ifndef MAT_UTILS_H
#define MAT_UTILS_H

double dot(const vector<double> &a, const vector<double> &b);
double norm_2(const vector<double> &a);
double norm_inf(const vector<double> &a);
void axpy(double a, const vector<double> &x, vector<double> &y);
void scale(vector<double> &x, double s);

#endif // MAT_UTILS_H
