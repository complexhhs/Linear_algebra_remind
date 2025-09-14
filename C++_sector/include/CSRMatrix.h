#pragma once
#include "common_include.h"

#ifndef CSR_MATRIX_H
#define CSR_MATRIX_H

struct CSRMatrix 
{
    int nrows, ncols;
    vector<double> values;
    vector<int> col_idx;
    vector<int> row_ptr;  // nrows+1

    CSRMatrix() = default;
    CSRMatrix(int row, int column): nrows(row), ncols(column), row_ptr(row+1, 0) {}

    void fromTriplets(int rows, int cols, vector<tuple<int, int, double>> &triplets){
        nrows = rows;
        ncols = cols; 

        sort(triplets.begin(), triplets.end(), [](auto &a, auto&b){
            if (get<0>(a) != get<0>(b)) {
                return get<0>(a) < get<0>(b);}
            else{
                return get<1> (a) < get<1>(b);}    
        };
        vector<tuple<int, int, double>> comp;
        for (auto &t: triplets){
            if(!comp.empty() && get<0>(comp.back()) == get<0>(t) && get<1>(comp.back()) == get<1>(t)){
                
            }else{
                comp.push_back(t);
            }
        }
        values.clear();
        col_idx.clear();
        row_ptr.assign(nrows+1, 0);
        for (auto &t: comp) row_ptr[get<0>(t)+1]++;
        for (int i = 0; i < nrows; i++) row_ptr[i+1] += row_ptr[i];
        int nnz = comp.size();
        value.resize(nnz);
        col_idx.resize(nnz);
        vector<int> cur = row_ptr;
        for (auto &t: comp){
            int r = get<0>(t);
            int c = get<1>(t);
            double v = get<2>(t);
            int p = cur[r]++;
            values[p] = v;
            col_idx[p] = c;
        }
    } // fromTriplets


    void multiply(const vector<double> &x, vector<double> &y) const {
        y.assign(nrows, 0.0);
        for (int r = 0; r < nrows; r++){
            for (int idx = row_ptr[r]; idx < row_ptr[r+1]; idx++){
                y[r] += values[idx] * x[col_idx[idx]];
            }
        }
    } // multiply

    vector<double> diagonal() const{
        vector<double> d(nrows, 0.0);
        for (int r = 0; r < nrows; r++){
            for (int idx = row_ptr[r]; idx < row_ptr[r+1]; idx++){
                if (col_idx[idx] == r){d[r] = values[idx]; break;}
            }
        return d;
    }
}; // CSRMatrix

#endif // CSR_MATRIX_H
