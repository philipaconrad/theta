// theta.cpp : Defines the entry point for the console application.
#include "stdafx.h"
#include "BzzMath.hpp"
#include <iostream>
#include <conio.h>
#include <math.h>
#include <cmath>
#include <stdio.h>
#include <iostream>
#include <fstream>

using namespace std; 

void Jianmin(BzzVector &y,BzzVector &f);

void main(void)
{
    // corresponding y[x] y[1],    y[2],     y[3],     y[4],     y[5],     y[6],     y[7],    y[8],     y[9],     y[10],    y[11],   y[12],    y[13],    y[14],    y[15],     y[16],   y[17],    y[18],     y[19]     y[20]      y[21]      y[22],     y[23],     y[24],      y[25],      y[26],       y[27],    y[28],    y[29],    y[30],    y[31],    y[32],    y[33],    y[34],    y[35],    y[36],    y[37],    y[38],    y[39].
	// initial guess for: theta_A, theta_E,  theta_F,  theta_G,  theta_I,  theta_L,  theta_M, theta_N,  theta_O,  theta_R,  theta_S, theta_U,  theta_V,  theta_X,  free_site, theta_H, theta_OH, theta_H2O, theta_CH, theta_CH2, theta_CH3, theta_CH4, theta_CHO, theta_CH2O, theta_CH3O, theta_CH3OH, theta_W,  theta_T,  theta_B,  theta_J,  theta_P,  theta_C,  theta_D,  theta_K,  theta_Q,  theta_Y,  theta_Z,  theta_Z1, theta_CO.
	BzzVector y,   y0(39, 3.9e-10, 4.2e-11,  3.92e-14, 2.61e-3,  4.75e-6,  6.21e-12, 5.01e-8, 2.13e-11, 5.32e-9,  5.66e-2,  2.80e-7, 2.60e-4,  4.99e-8,  6.69e-2,  4.50e-3,   0.554,   3.02e-17, 1.08e-18,  2.21e-3,  2.59e-6,   1.22e-6,   6.07e-19,  5.81e-15,  9.66e-16,   1.72e-08,   7.49e-20,    2.92e-10, 1.29e-11, 4.37e-11, 1.22e-15, 1.85e-10, 4.04e-15, 6.26e-13, 2.53e-11, 3.77e-17, 3.60e-09, 7.43e-10, 1.25e-12, 4.31e-06);
//	BzzVector y,   y0(39, 0.200,   1.47e-16, 3.33e-13, 7.93e-13, 3.25e-14, 1.45e-18, 0.100,   1.57e-11, 2.07e-13, 5.56e-10, 0.200,   6.45e-13, 1.63e-13, 8.89e-13, 0.5000,    0.2000,  1.42e-03, 8.77e-05,  8.80e-15, 2.88e-16,  4.34e-10,  4.34e-10,  4.34e-10,  1.42e-04,   8.77e-05,   8.80e-15,    1.00e-10, 1.00e-10, 1.00e-10, 1.00e-10, 1.00e-10, 1.00e-10, 1.00e-10, 1.00e-10, 1.00e-10, 1.00e-10, 1.00e-10, 1.00e-10, 0.001);
    BzzNonLinearSystem nls(y0,Jianmin);
	//                   y[1],  y[2],  y[3],  y[4],  y[5],  y[6],  y[7],  y[8],  y[9],  y[10],     y[11], y[12], y[13], y[14], y[15],  y[16], y[17], y[18], y[19], y[20];     y[21]  y[22], y[23], y[24], y[25], y[26], y[27], y[28], y[29], y[30];     y[31], y[32], y[33], y[34], y[35], y[36], y[37], y[38], y[39].
	BzzVector yMin(39,   1e-10, 1e-30, 1e-30, 1e-40, 1e-20, 1e-25, 1e-10, 1e-20, 1e-20, 1e-30,     1e-20, 1e-20, 1e-20, 1e-20, 1e-20,  1e-30, 1e-25, 1e-20, 1e-20, 1e-20,     1e-20, 1e-25, 1e-20, 1e-20, 1e-20, 1e-20, 1e-20, 1e-20, 1e-20, 1e-30,     1e-20, 1e-20, 1e-20, 1e-20, 1e-30, 1e-20, 1e-20, 1e-20, 1e-30),
		      yMax(39,   0.80,  0.01,  0.01,  0.80,  0.01,  0.01,  0.50,  0.01,  0.01,  0.80,      0.01,  0.90,  0.01,  0.8,  0.80,   0.80,  0.80,  0.80,  0.80,  0.50,      0.01,  0.01,  0.01,  0.10,  0.80,  0.50,  0.10,  0.10,  0.50,  0.10,      0.10,  0.10,  0.10,  0.10,  0.10,  0.10,  0.10,  0.10,  0.80);
    nls.SetMinimumConstraints(yMin);
    nls.SetMaximumConstraints(yMax);
    nls();
    nls.BzzPrint("Result");
}

void Jianmin(BzzVector &y,BzzVector &f)
{
	double r_00, r_01, r_02, r_03, r_04, r_05, r_06, r_07, r_08, r_09, r_10, r_11, r_12, r_13, r_14, r_15, r_16, r_17, r_18, r_19, r_20, r_21, r_22, r_23, r_24, r_25, r_26, r_27, r_28, r_29, r_30, r_31, r_32, r_33, r_34, r_35, r_36, r_37, r_38, r_39, r_40, r_41, r_42, r_43, r_44, r_45, r_46, r_47, r_48, r_49, r_50, r_51, r_52, r_53, r_54, r_71, r_72, r_73, r_74, r_75, r_76, r_77;
	double r_01_f, r_01_b, r_02_f, r_02_b, r_03_f, r_03_b, r_04_f, r_04_b, r_05_f, r_05_b, r_06_f, r_06_b, r_07_f, r_07_b, r_08_f, r_08_b, r_09_f, r_09_b, r_10_f, r_10_b, r_11_f, r_11_b, r_12_f, r_12_b, r_13_f, r_13_b, r_14_f, r_14_b, r_15_f, r_15_b, r_16_f, r_16_b, r_17_f, r_17_b, r_18_f, r_18_b, r_19_f, r_19_b, r_20_f, r_20_b;
	double r_21_f, r_21_b, r_22_f, r_22_b, r_23_f, r_23_b, r_24_f, r_24_b, r_25_f, r_25_b, r_26_f, r_26_b, r_27_f, r_27_b, r_28_f, r_28_b, r_29_f, r_29_b, r_30_f, r_30_b, r_31_f, r_31_b, r_32_f, r_32_b, r_33_f, r_33_b, r_34_f, r_34_b, r_35_f, r_35_b, r_36_f, r_36_b, r_37_f, r_37_b, r_38_f, r_38_b, r_39_f, r_39_b, r_40_f, r_40_b;
	double r_41_f, r_41_b, r_42_f, r_42_b, r_43_f, r_43_b, r_44_f, r_44_b, r_45_f, r_45_b, r_46_f, r_46_b, r_47_f, r_47_b, r_48_f, r_48_b, r_49_f, r_49_b, r_50_f, r_50_b, r_51_f, r_51_b, r_52_f, r_52_b, r_53_f, r_53_b, r_71_f, r_71_b, r_72_f, r_72_b, r_73_f, r_73_b, r_74_f, r_74_b;
	double theta_A, theta_B, theta_C, theta_D, theta_E, theta_F, theta_G, theta_I, theta_J, theta_K, theta_L, theta_M, theta_N, theta_O, theta_P, theta_Q, theta_R, theta_S, theta_T, theta_U, theta_V, theta_W, theta_X, theta_Y, theta_Z, theta_Z1;
	double free, theta_H, theta_OH, theta_H2O, theta_CH, theta_CH2, theta_CH3, theta_CH4, theta_CO, theta_CHO, theta_CH2O, theta_CH3O, theta_CH3OH;
	double K_H, r_00_f, r_00_b;

	// define constants for forward and reverse rate constants.
	double k_00_f=6.249e7,  k_00_b=5.885e4;
	double k_01_f=1.831e3,  k_01_b=3.070e6,      k_02_f=9.567e2,  k_02_b=2.885e7,      k_03_f=8.447e3,  k_03_b=8.560e1,      k_04_f=1.863e5,  k_04_b=8.721,        k_05_f=5.509e8,  k_05_b=3.131e5;
	double k_06_f=5.982,    k_06_b=6.828e-12,    k_07_f=2.106e10, k_07_b=4.823e3,      k_08_f=7.139e4,  k_08_b=1.020e4,      k_09_f=2.243e8,  k_09_b=1.566,        k_10_f=2.418e7,  k_10_b=5.024e5;
	double k_11_f=1.247e8,  k_11_b=3.056e6,      k_12_f=1.100e2,  k_12_b=6.318e-1,     k_13_f=5.791e12, k_13_b=1.247e8,      k_14_f=1.114e9,  k_14_b=8.518e-3,     k_15_f=9.955e3,  k_15_b=6.388e10;
	double k_16_f=5.396e2,  k_16_b=1.625e7,      k_17_f=3.706e3,  k_17_b=1.514e5,      k_18_f=2.705e8,  k_18_b=4.864e5,      k_19_f=7.040e9,  k_19_b=1.941e2,      k_20_f=5.501e8,  k_20_b=1.750e6;
	double k_21_f=2.335e4,  k_21_b=8.974e1,      k_22_f=1.630e10, k_22_b=5.505e-2,     k_23_f=6.622e2,  k_23_b=1.555e1,      k_24_f=6.464e2,  k_24_b=2.380e7,      k_25_f=2.109e8,  k_25_b=1.986;
	double k_26_f=8.910,    k_26_b=1.865e7,      k_27_f=3.268e5,  k_27_b=1.668,        k_28_f=1.890e5,  k_28_b=1.108e7,      k_29_f=9.014e11, k_29_b=1.962,        k_30_f=7.631e3,  k_30_b=1.902e11;
	double k_31_f=6.303e2,  k_31_b=5.235e1,      k_32_f=1.075e2,  k_32_b=1.311e7,      k_33_f=9.362e7,  k_33_b=2.729,        k_34_f=9.540e4,  k_34_b=2.606e8,      k_35_f=2.636e8,  k_35_b=5.388e6;
	double k_36_f=3.368e8,  k_36_b=4.689,        k_37_f=1.615e10, k_37_b=1.170e4,      k_38_f=3.290e-3, k_38_b=2.457e-15,    k_39_f=1.004e3,  k_39_b=1.833e-6,     k_40_f=1.457e5,  k_40_b=7.225e-5;
	double k_41_f=2.380e2,  k_41_b=5.142e8,      k_42_f=3.845e7,  k_42_b=4.046e12,     k_43_f=3.778e7,  k_43_b=9.921e9,      k_44_f=9.432e3,  k_44_b=3.620e7,      k_45_f=1.666e3,  k_45_b=2.431e7,      k_46_f=3.094e8,  k_46_b=1.802e13,     k_47_f=1.557e7,  k_47_b=2.232e8;
	double k_48_f=6.575e1,  k_48_b=7.117e7,      k_49_f=1.372e2,  k_49_b=6.635e7,      k_50_f=3.003,    k_50_b=7.879e7,      k_51_f=3.044e13, k_51_b=1.230e8,      k_52_f=1.047e16, k_52_b=1.740e8,      k_53_f=2.092e12, k_53_b=1.640e8,      k_54_f=1.020e3,  k_54_b=6.696e7;
// k_55_f - k_70_f don't get initialized!?!
	double k_71_f=5.056e9,  k_71_b=2.126e8,      k_72_f=1.396e9,  k_72_b=1.611,        k_73_f=4.831e9,  k_73_b=1.848e6,      k_74_f=9.712e6,  k_74_b=1.828e2,      k_75_f=4.000,    k_75_b=3.558e8,      k_76_f=2.403e6,  k_76_b=1.593e5,      k_77_f=1.404e-1, k_77_b=1.336e10;
	
	// define partial pressures, Boltzman constant and temperature.
	//     guaiacol,  H2,       catechol,   phenol,     benzene,    anisole.
	double p_A=1.0,   p_H2=1.0, p_M=1.0e-5, p_S=1.0e-5, p_X=1.0e-5, p_K=1.0e-5, p_CO=1.0e-6, p_H2O=0.0, p_CH4=0.0, p_CH3OH=0.0, KB=8.6173324e-5, T=573;

	theta_A  = y[1];
	theta_E  = y[2];
	theta_F  = y[3];
	theta_G  = y[4];
	theta_I  = y[5];
	theta_L  = y[6];
	theta_M  = y[7];
	theta_N  = y[8];
	theta_O  = y[9];
	theta_R  = y[10];
	theta_S  = y[11];
	theta_U  = y[12];
	theta_V  = y[13];
	theta_X  = y[14];
	free        = y[15];
	theta_H     = y[16];
	theta_OH    = y[17];
	theta_H2O   = y[18];
	theta_CH    = y[19];
	theta_CH2   = y[20];
	theta_CH3   = y[21];
	theta_CH4   = y[22];
	theta_CHO   = y[23];
	theta_CH2O  = y[24];
	theta_CH3O  = y[25];
	theta_CH3OH = y[26];
	theta_W     = y[27];
	theta_T     = y[28];
	theta_B     = y[29];
	theta_J     = y[30];
	theta_P     = y[31];
	theta_C     = y[32];
	theta_D     = y[33];
	theta_K     = y[34];
	theta_Q     = y[35];
	theta_Y     = y[36];
	theta_Z     = y[37];
	theta_Z1    = y[38];
	theta_CO    = y[39];

	// calculate rates for all elementary steps.
	r_00 = k_00_f*p_A*free*free*free*free - k_00_b*theta_A;
	r_01 = k_01_f*theta_A*theta_H     - k_01_b*theta_B*free;
	r_04 = k_04_f*theta_A*free        - k_04_b*theta_E*theta_CH3O;
	r_05 = k_05_f*theta_A*free        - k_05_b*theta_F*theta_H;
	r_06 = k_06_f*theta_A*free        - k_06_b*theta_G*theta_CH3;
	r_07 = k_07_f*theta_A*free        - k_07_b*theta_I*theta_H;
	r_08 = k_08_f*theta_B*free*free   - k_08_b*theta_J*theta_H;
	r_11 = k_11_f*theta_E*theta_H     - k_11_b*theta_S*free;
	r_12 = k_12_f*theta_F*free        - k_12_b*theta_E*theta_CH2O;
	r_13 = k_13_f*theta_F*free        - k_13_b*theta_L*theta_H;
	r_14 = k_14_f*theta_F             - k_14_b*theta_G*theta_CH2;
	r_15 = k_15_f*theta_G*theta_H     - k_15_b*theta_M*free;
	r_16 = k_16_f*theta_G*free        - k_16_b*theta_N*theta_OH;
	r_17 = k_17_f*theta_I*free        - k_17_b*theta_N*theta_CH3O;
	r_18 = k_18_f*theta_I*free*free   - k_18_b*theta_O*theta_H;
	r_19 = k_19_f*theta_J             - k_19_b*theta_P*theta_CH2;
	r_21 = k_21_f*theta_L*free        - k_21_b*theta_E*theta_CHO;
	r_22 = k_22_f*theta_L*free        - k_22_b*theta_G*theta_CH;
	r_23 = k_23_f*theta_M*free        - k_23_b*theta_E*theta_OH;
	r_24 = k_24_f*theta_M*theta_H     - k_24_b*theta_T;
	r_25 = k_25_f*theta_N*theta_H     - k_25_b*theta_R*free;
	r_26 = k_26_f*theta_O*free        - k_26_b*theta_N*theta_CH2O;
	r_27 = k_27_f*theta_O*free        - k_27_b*theta_U*theta_CH2;
	r_28 = k_28_f*theta_P*theta_H     - k_28_b*theta_T*free;
	r_30 = k_30_f*theta_R*theta_H     - k_30_b*theta_S*free;
	r_31 = k_31_f*theta_S*free        - k_31_b*theta_V*theta_OH;
	r_32 = k_32_f*theta_S*theta_H     - k_32_b*theta_W*free;
	r_33 = k_33_f*theta_T*free        - k_33_b*theta_S*theta_OH;
	r_34 = k_34_f*theta_U*theta_H     - k_34_b*theta_G*free*free;
	r_35 = k_35_f*theta_V*theta_H     - k_35_b*theta_X*free*free;
	r_36 = k_36_f*theta_W             - k_36_b*theta_X*theta_OH;
	r_37 = k_37_f*theta_F*free        - k_37_b*theta_O*theta_H;
	r_39 = k_39_f*theta_I*free*free   - k_39_b*theta_U*theta_CH3;
	r_40 = k_40_f*theta_B*free*free   - k_40_b*theta_S*theta_CH3O;
	r_41 = k_41_f*theta_CH3O*theta_H  - k_41_b*theta_CH3OH*free;
	r_42 = k_42_f*theta_CH*theta_H    - k_42_b*theta_CH2*free;
	r_43 = k_43_f*theta_CH2*theta_H   - k_43_b*theta_CH3*free;
	r_44 = k_44_f*theta_CH3*theta_H   - k_44_b*theta_CH4*free;
	r_45 = k_45_f*theta_OH*theta_H    - k_45_b*theta_H2O*free;
	r_46 = k_46_f*theta_CHO*theta_H   - k_46_b*theta_CH2O*free;
	r_47 = k_47_f*theta_CH2O*theta_H  - k_47_b*theta_CH3O*free*free;
	r_48 = k_48_f*theta_S             - k_48_b*p_S*free*free*free*free; //phenol   desorption
	r_49 = k_49_f*theta_M             - k_49_b*p_M*free*free*free*free; //catechol desorption
	r_50 = k_50_f*theta_X             - k_50_b*p_X*free*free*free;      //benzene  desorption
	r_51 = k_51_f*theta_CH3OH         - k_51_b*p_CH3OH*free; //CH3OH desorption
	r_52 = k_52_f*theta_CH4           - k_52_b*p_CH4*free;   //CH4   desorption
	r_53 = k_53_f*theta_H2O           - k_53_b*p_H2O*free;   //H2O   desorption
	r_54 = k_54_f*theta_K             - k_54_b*p_K*free*free*free*free; //anisole  desorption
	
	r_75 = k_75_f*theta_G*theta_H     - k_75_b*theta_Y*free;
	r_76 = k_76_f*theta_Y*free        - k_76_b*theta_R*theta_OH;
	r_71 = k_71_f*theta_O*free        - k_71_b*theta_Z*theta_H;
	r_72 = k_72_f*theta_Z*free        - k_72_b*theta_U*theta_CH;
	r_73 = k_73_f*theta_Z*free        - k_73_b*theta_Z1*theta_H;
//	r_74 = k_74_f*theta_Z1            - k_74_b*theta_N*0.1; // 0.1 is the coverage of CO.
	r_74 = k_74_f*theta_Z1            - k_74_b*theta_N*theta_CO;
	r_77 = k_77_f*theta_CO*theta_H    - k_77_b*theta_CHO;

	// steps including C, D, K, Q.
	r_02 = k_02_f*theta_A*theta_H     - k_02_b*theta_C*free;
	r_03 = k_03_f*theta_A*free        - k_03_b*theta_D*theta_OH;
	r_09 = k_09_f*theta_C*free        - k_09_b*theta_K*theta_OH;
	r_10 = k_10_f*theta_D*theta_H     - k_10_b*theta_K*free;
	r_20 = k_20_f*theta_K*free        - k_20_b*theta_Q*theta_H;
	r_29 = k_29_f*theta_Q*free        - k_29_b*theta_R*theta_CH2;

	// apply the steady state approximation for all thetas.
	f[1]  = r_04 + r_12 + r_21 + r_23 - r_11;     // d(theta_E)/dt=0
	f[2]  = r_05 - r_12 - r_13 - r_14 - r_37;     // d(theta_F)/dt=0
	f[3]  = r_06 + r_14 + r_22 + r_34 - r_15 - r_16 - r_75; // d(theta_G)/dt=0
	f[4]  = r_07 - r_17 - r_18 - r_39;            // d(theta_I)/dt=0
	f[5]  = r_13 - r_21 - r_22;                   // d(theta_L)/dt=0
	f[6]  = r_15 - r_23 - r_24 - r_49;            // d(theta_M)/dt=0 catechol
	f[7]  = r_16 + r_17 + r_26 + r_74 - r_25;     // d(theta_N)/dt=0
	f[8]  = r_18 + r_37 - r_26 - r_27 - r_71;     // d(theta_O)/dt=0
	f[9]  = r_25 + r_29 + r_76 - r_30;            // d(theta_R)/dt=0
	f[10] = r_11 + r_30 + r_33 + r_40 - r_31 - r_32 - r_48; // d(theta_S)/dt=0 phenol
	f[11] = r_27 + r_39 + r_72 - r_34;            // d(theta_U)/dt=0
	f[12] = r_31 - r_35;                          // d(theta_V)/dt=0
	f[13] = r_35 + r_36 - r_50;                   // d(theta_X)/dt=0 benzene

	f[14] = r_03 + r_09 + r_23 + r_31 + r_31 + r_33 - r_45; // d(theta_OH)/dt=0
	f[15] = r_45 - r_53;                          // d(theta_H2O)/dt=0
	f[16] = r_22 + r_72 - r_42;                   // d(theta_CH)/dt =0
	f[17] = r_14 + r_19 + r_27 + r_29 + r_42 - r_43; // d(theta_CH2)/dt=0	
	f[18] = r_06 + r_43 - r_44;                   // d(theta_CH3)/dt=0
	f[19] = r_44 - r_52;                          // d(theta_CH4)/dt=0
	f[20] = r_21 + r_77 - r_46;                   // d(theta_CHO)/dt=0
	f[21] = r_12 + r_26 + r_46 - r_47;            // d(theta_CH2O)/dt=0
	f[22] = r_04 + r_17 + r_47 - r_41;            // d(theta_CH3O)/dt=0
	f[23] = r_41 - r_51;                          // d(theta_CH3OH)/dt=0
	f[24] = r_00 - r_01 - r_04 - r_05 - r_06 - r_07; // d(theta_A)/dt=0
//	f[24] = theta_A - k_00_f/k_00_b*p_A*free*free*free*free; // d(theta_A)/dt=0 if step 0 is in equilibrium.
	f[25] = r_32 - r_36;                          // d(theta_W)/dt=0
	f[26] = r_24 + r_28 - r_33;                   // d(theta_T)/dt=0
	f[27] = r_01 - r_08 - r_40;                   // d(theta_B)/dt=0
	f[28] = r_08 - r_19;                          // d(theta_J)/dt=0
	f[29] = r_19 - r_28;                          // d(theta_P)/dt=0
	f[30] = theta_H - exp(-( (-1.374+0.076+0.683)/2 + 2*0.084*(theta_H-0.139))/KB/T)*pow(p_H2,0.5)*free; //theta_H
	f[31] = r_02 - r_09;                          // d(theta_C)/dt=0
	f[32] = r_03 - r_10;                          // d(theta_D)/dt=0
	f[33] = r_09 + r_10 - r_20 - r_54;            // d(theta_K)/dt=0
	f[34] = r_20 - r_29;                          // d(theta_Q)/dt=0
	f[35] = r_75 - r_76;                          // d(theta_Y)/dt=0
	f[36] = r_71 - r_72 - r_73;                   // d(theta_Z)/dt=0
	f[37] = r_73 - r_74;                          // d(theta_Z1)/dt=0
	f[38] = theta_CO - exp(-(-2.131+0.028+1.764)/KB/T)*p_CO*free; // d(theta_CO)/dt=0

    // finally the summation of all thetas should be 1.
	f[39] = 4*y[1]+4*y[2]+4*y[3]+4*y[4]+4*y[5]+4*y[6]+4*y[7]+4*y[8]+4*y[9]+4*y[10]+4*y[11]+5*y[12]+3*y[13]+3*y[14]+y[15]+y[16]+y[17]+y[18]+y[19]+2*y[20]+y[21]+y[22]+2*y[23]+2*y[24]+y[25]+y[26]+4*y[27]+5*y[28]+4*y[29]+4*y[30]+5*y[31]+4*y[32]+4*y[33]+4*y[34]+5*y[35]+4*y[36]+4*y[37]+4*y[38]+y[39] - 1.00;

	K_H = exp(-( (-1.374+0.076+0.683)/2 + 2*0.084*(theta_H-0.139))/KB/T);

	r_00_f = k_00_f*p_A*free*free*free*free; r_00_b = k_00_b*theta_A;
	r_01_f = k_01_f*theta_A*theta_H;     r_01_b = k_01_b*theta_B*free;
	r_02_f = k_02_f*theta_A*theta_H;     r_02_b = k_02_b*theta_C*free;
	r_03_f = k_03_f*theta_A*free;        r_03_b = k_03_b*theta_D*theta_OH;
	r_04_f = k_04_f*theta_A*free;        r_04_b = k_04_b*theta_E*theta_CH3O;
	r_05_f = k_05_f*theta_A*free;        r_05_b = k_05_b*theta_F*theta_H;
	r_06_f = k_06_f*theta_A*free;        r_06_b = k_06_b*theta_G*theta_CH3;
	r_07_f = k_07_f*theta_A*free;        r_07_b = k_07_b*theta_I*theta_H;
	r_15_f = k_15_f*theta_G*theta_H;     r_15_b = k_15_b*theta_M*free;
	r_18_f = k_18_f*theta_I*free*free;   r_18_b = k_18_b*theta_O*theta_H;
	r_22_f = k_22_f*theta_L*free;        r_22_b = k_22_b*theta_G*theta_CH;
	r_23_f = k_23_f*theta_M*free;        r_23_b = k_23_b*theta_E*theta_OH;
	r_24_f = k_24_f*theta_M*theta_H;     r_24_b = k_24_b*theta_T;
	r_25_f = k_25_f*theta_N*theta_H;     r_25_b = k_25_b*theta_R*free;
	r_30_f = k_30_f*theta_R*theta_H;     r_30_b = k_30_b*theta_S*free;
	r_34_f = k_34_f*theta_U*theta_H;     r_34_b = k_34_b*theta_G*free*free;
	r_42_f = k_42_f*theta_CH*theta_H;    r_42_b = k_42_b*theta_CH2*free;
	r_43_f = k_43_f*theta_CH2*theta_H;   r_43_b = k_43_b*theta_CH3*free;
	r_44_f = k_44_f*theta_CH3*theta_H;   r_44_b = k_44_b*theta_CH4*free;

	r_48_f = k_48_f*theta_S;             r_48_b = k_48_b*p_S*free*free*free*free; //phenol   desorption
	r_49_f = k_49_f*theta_M;             r_49_b = k_49_b*p_M*free*free*free*free;           //catechol desorption
	r_71_f = k_71_f*theta_O*free;        r_71_b = k_71_b*theta_Z*theta_H;
	r_72_f = k_72_f*theta_Z*free;        r_72_b = k_72_b*theta_U*theta_CH;
	r_73_f = k_73_f*theta_Z*free;        r_73_b = k_73_b*theta_Z1*theta_H;
	r_74_f = k_74_f*theta_Z1;            r_74_b = k_74_b*theta_N*0.01;

//	creat a text file named rates.txt (an empty rates.txt file should be created by me in advance).
	fstream myfile("output_rates.txt");
	myfile.is_open();
	myfile<<"r_01 = "; myfile<<r_01; myfile<<"\n";   myfile<<"r_02 = "; myfile<<r_02; myfile<<"\n";   myfile<<"r_03 = "; myfile<<r_03; myfile<<"\n";   myfile<<"r_04 = "; myfile<<r_04; myfile<<"\n";   myfile<<"r_05 = "; myfile<<r_05; myfile<<"\n";
	myfile<<"r_06 = "; myfile<<r_06; myfile<<"\n";   myfile<<"r_07 = "; myfile<<r_07; myfile<<"\n";   myfile<<"r_08 = "; myfile<<r_08; myfile<<"\n";   myfile<<"r_09 = "; myfile<<r_09; myfile<<"\n";   myfile<<"r_10 = "; myfile<<r_10; myfile<<"\n";
	myfile<<"r_11 = "; myfile<<r_11; myfile<<"\n";   myfile<<"r_12 = "; myfile<<r_12; myfile<<"\n";   myfile<<"r_13 = "; myfile<<r_13; myfile<<"\n";   myfile<<"r_14 = "; myfile<<r_14; myfile<<"\n";   myfile<<"r_15 = "; myfile<<r_15; myfile<<"\n";
	myfile<<"r_16 = "; myfile<<r_16; myfile<<"\n";   myfile<<"r_17 = "; myfile<<r_17; myfile<<"\n";   myfile<<"r_18 = "; myfile<<r_18; myfile<<"\n";   myfile<<"r_19 = "; myfile<<r_19; myfile<<"\n";   myfile<<"r_20 = "; myfile<<r_20; myfile<<"\n";
	myfile<<"r_21 = "; myfile<<r_21; myfile<<"\n";   myfile<<"r_22 = "; myfile<<r_22; myfile<<"\n";   myfile<<"r_23 = "; myfile<<r_23; myfile<<"\n";   myfile<<"r_24 = "; myfile<<r_24; myfile<<"\n";   myfile<<"r_25 = "; myfile<<r_25; myfile<<"\n";
	myfile<<"r_26 = "; myfile<<r_26; myfile<<"\n";   myfile<<"r_27 = "; myfile<<r_27; myfile<<"\n";   myfile<<"r_28 = "; myfile<<r_28; myfile<<"\n";   myfile<<"r_29 = "; myfile<<r_29; myfile<<"\n";   myfile<<"r_30 = "; myfile<<r_30; myfile<<"\n";
	myfile<<"r_31 = "; myfile<<r_31; myfile<<"\n";   myfile<<"r_32 = "; myfile<<r_32; myfile<<"\n";   myfile<<"r_33 = "; myfile<<r_33; myfile<<"\n";   myfile<<"r_34 = "; myfile<<r_34; myfile<<"\n";   myfile<<"r_35 = "; myfile<<r_35; myfile<<"\n";
	myfile<<"r_36 = "; myfile<<r_36; myfile<<"\n";   myfile<<"r_37 = "; myfile<<r_37; myfile<<"\n";   myfile<<"r_39 = "; myfile<<r_39; myfile<<"\n";   myfile<<"r_40 = "; myfile<<r_40; myfile<<"\n";
	myfile<<"r_41 = "; myfile<<r_41; myfile<<"\n";   myfile<<"r_42 = "; myfile<<r_42; myfile<<"\n";   myfile<<"r_43 = "; myfile<<r_43; myfile<<"\n";   myfile<<"r_44 = "; myfile<<r_44; myfile<<"\n";   myfile<<"r_45 = "; myfile<<r_45; myfile<<"\n";
    myfile<<"r_46 = "; myfile<<r_46; myfile<<"\n";   myfile<<"r_47 = "; myfile<<r_47; myfile<<"\n";   myfile<<"r_48 = "; myfile<<r_48; myfile<<"\n";   myfile<<"r_49 = "; myfile<<r_49; myfile<<"\n";   myfile<<"r_50 = "; myfile<<r_50; myfile<<"\n";   myfile<<"\n";
    myfile<<"r_51 = "; myfile<<r_51; myfile<<"\n";   myfile<<"r_52 = "; myfile<<r_52; myfile<<"\n";   myfile<<"r_53 = "; myfile<<r_53; myfile<<"\n";   myfile<<"r_54 = "; myfile<<r_54; myfile<<"\n";   myfile<<"\n";
	myfile<<"r_71 = "; myfile<<r_71; myfile<<"\n";   myfile<<"r_72 = "; myfile<<r_72; myfile<<"\n";   myfile<<"r_73 = "; myfile<<r_73; myfile<<"\n";   myfile<<"r_74 = "; myfile<<r_74; myfile<<"\n";   myfile<<"r_75 = "; myfile<<r_75; myfile<<"\n";   myfile<<"r_76 = "; myfile<<r_76; myfile<<"\n";    myfile<<"r_77 = "; myfile<<r_77; myfile<<"\n"; myfile<<"\n";
	
	myfile<<"r_00_f = "; myfile<<r_00_f; myfile<<"\n";   myfile<<"r_00_b = "; myfile<<r_00_b; myfile<<"\n";
	myfile<<"r_01_f = "; myfile<<r_01_f; myfile<<"\n";   myfile<<"r_01_b = "; myfile<<r_01_b; myfile<<"\n";
	myfile<<"r_02_f = "; myfile<<r_02_f; myfile<<"\n";   myfile<<"r_02_b = "; myfile<<r_02_b; myfile<<"\n";
	myfile<<"r_03_f = "; myfile<<r_03_f; myfile<<"\n";   myfile<<"r_03_b = "; myfile<<r_03_b; myfile<<"\n";
	myfile<<"r_04_f = "; myfile<<r_04_f; myfile<<"\n";   myfile<<"r_04_b = "; myfile<<r_04_b; myfile<<"\n";
	myfile<<"r_05_f = "; myfile<<r_05_f; myfile<<"\n";   myfile<<"r_05_b = "; myfile<<r_05_b; myfile<<"\n";
	myfile<<"r_06_f = "; myfile<<r_06_f; myfile<<"\n";   myfile<<"r_06_b = "; myfile<<r_06_b; myfile<<"\n";
	myfile<<"r_07_f = "; myfile<<r_07_f; myfile<<"\n";   myfile<<"r_07_b = "; myfile<<r_07_b; myfile<<"\n";   myfile<<"\n";
	myfile<<"r_15_f = "; myfile<<r_15_f; myfile<<"\n";   myfile<<"r_15_b = "; myfile<<r_15_b; myfile<<"\n";   myfile<<"\n";
	myfile<<"r_18_f = "; myfile<<r_18_f; myfile<<"\n";   myfile<<"r_18_b = "; myfile<<r_18_b; myfile<<"\n";   myfile<<"\n";
	myfile<<"r_22_f = "; myfile<<r_22_f; myfile<<"\n";   myfile<<"r_22_b = "; myfile<<r_22_b; myfile<<"\n";   myfile<<"\n";
	myfile<<"r_23_f = "; myfile<<r_23_f; myfile<<"\n";   myfile<<"r_23_b = "; myfile<<r_23_b; myfile<<"\n";   myfile<<"\n";
	myfile<<"r_24_f = "; myfile<<r_24_f; myfile<<"\n";   myfile<<"r_24_b = "; myfile<<r_24_b; myfile<<"\n";   myfile<<"\n";
	myfile<<"r_25_f = "; myfile<<r_25_f; myfile<<"\n";   myfile<<"r_25_b = "; myfile<<r_25_b; myfile<<"\n";   myfile<<"\n";
	myfile<<"r_30_f = "; myfile<<r_30_f; myfile<<"\n";   myfile<<"r_30_b = "; myfile<<r_30_b; myfile<<"\n";   myfile<<"\n";
	myfile<<"r_34_f = "; myfile<<r_34_f; myfile<<"\n";   myfile<<"r_34_b = "; myfile<<r_34_b; myfile<<"\n";   myfile<<"\n";
	myfile<<"r_42_f = "; myfile<<r_42_f; myfile<<"\n";   myfile<<"r_42_b = "; myfile<<r_42_b; myfile<<"\n";   myfile<<"\n";
	myfile<<"r_43_f = "; myfile<<r_43_f; myfile<<"\n";   myfile<<"r_43_b = "; myfile<<r_43_b; myfile<<"\n";   myfile<<"\n";
	myfile<<"r_44_f = "; myfile<<r_44_f; myfile<<"\n";   myfile<<"r_44_b = "; myfile<<r_44_b; myfile<<"\n";   myfile<<"\n";
	myfile<<"r_48_f = "; myfile<<r_48_f; myfile<<"\n";   myfile<<"r_48_b = "; myfile<<r_48_b; myfile<<"\n";   myfile<<"\n";
	myfile<<"r_49_f = "; myfile<<r_49_f; myfile<<"\n";   myfile<<"r_49_b = "; myfile<<r_49_b; myfile<<"\n";   myfile<<"\n";
	myfile<<"r_71_f = "; myfile<<r_71_f; myfile<<"\n";   myfile<<"r_71_b = "; myfile<<r_71_b; myfile<<"\n";   myfile<<"\n";
	myfile<<"r_72_f = "; myfile<<r_72_f; myfile<<"\n";   myfile<<"r_72_b = "; myfile<<r_72_b; myfile<<"\n";   myfile<<"\n";
	myfile<<"r_73_f = "; myfile<<r_73_f; myfile<<"\n";   myfile<<"r_73_b = "; myfile<<r_73_b; myfile<<"\n";   myfile<<"\n";
	myfile<<"r_74_f = "; myfile<<r_74_f; myfile<<"\n";   myfile<<"r_74_b = "; myfile<<r_74_b; myfile<<"\n";   myfile<<"\n";

	myfile<<"K_H = "; myfile<<K_H; myfile<<"\n";
	myfile.close();
}
