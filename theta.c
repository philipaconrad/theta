//-----------------------------------------------------------------------------
// theta.c -- A rewrite of 'theta.cpp' using GNU MP.
// Copyright (C) Philip Conrad 5/16/2013 -- MIT License
//
//-----------------------------------------------------------------------------


#include <stdio.h>
#include <gmp.h>
#include "types.h"


//---------------------------------------------------------
// DEFINITIONS & TYPEDEFS:

#define false 0
#define true 1
typedef int bool; // no built-in bool, so we roll our own.

typedef mpz_t bigInt;
typedef mpq_t bigFrac; //rational number
typedef mpf_t bigFloat;

//All the lists are of the same length.
typedef struct NLSystemContext {
    mpf_t* state;
    mpf_t* minBounds;
    mpf_t* maxBounds;
    uint32 listSize;
}NLSystemContext;


//---------------------------------------------------------
// INPUTS FOR THE NON-LINEAR SYSTEM:

double in_systemVars[39] = {
           3.9e-10,  4.2e-11, 3.92e-14,  2.61e-3,  4.75e-6, 6.21e-12,  5.01e-8, 2.13e-11,  5.32e-9,
 5.66e-2,  2.80e-7,  2.60e-4,  4.99e-8,  6.69e-2,  4.50e-3,    0.554, 3.02e-17, 1.08e-18,  2.21e-3,
 2.59e-6,  1.22e-6, 6.07e-19, 5.81e-15, 9.66e-16, 1.72e-08, 7.49e-20, 2.92e-10, 1.29e-11, 4.37e-11,
1.22e-15, 1.85e-10, 4.04e-15, 6.26e-13, 2.53e-11, 3.77e-17, 3.60e-09, 7.43e-10, 1.25e-12, 4.31e-06};

double in_minBounds[39] = {      1e-10, 1e-30, 1e-30, 1e-40, 1e-20, 1e-25, 1e-10, 1e-20, 1e-20,
                          1e-30, 1e-20, 1e-20, 1e-20, 1e-20, 1e-20, 1e-30, 1e-25, 1e-20, 1e-20,
                          1e-20, 1e-20, 1e-25, 1e-20, 1e-20, 1e-20, 1e-20, 1e-20, 1e-20, 1e-20,
                          1e-30, 1e-20, 1e-20, 1e-20, 1e-20, 1e-30, 1e-20, 1e-20, 1e-20, 1e-30};

double in_maxBounds[39] = {      0.80, 0.01, 0.01, 0.80, 0.01, 0.01, 0.50, 0.01, 0.01,
                           0.80, 0.01, 0.90, 0.01,  0.8, 0.80, 0.80, 0.80, 0.80, 0.80,
                           0.50, 0.01, 0.01, 0.01, 0.10, 0.80, 0.50, 0.10, 0.10, 0.50,
                           0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.80};


//---------------------------------------------------------
// GNU MP FLOAT ARRAYS:

static bigFloat state[39];
static bigFloat minBounds[39];
static bigFloat maxBounds[39];


//---------------------------------------------------------
// FUNCTION DEFINITIONS:

//initArray :: [bigFloat] -> [double] -> uint32 -> Effect
void initArray(bigFloat* dest, double* inputs, uint32 numVars) {
    uint32 i;
    for(i = 0; i < numVars; i++) {
        mpf_init_set_d(dest[i], inputs[i]);
    }
}


//initNLSystemContext :: NLSystemContext* -> [bigFloat] -> [bigFloat] -> [bigFloat] -> uint32 -> Effect
void initNLSystemContext(NLSystemContext* ctx, bigFloat* initialState, bigFloat* minBounds, bigFloat* maxBounds, uint32 listSize) {
    ctx->state     = initialState;
    ctx->minBounds = minBounds;
    ctx->maxBounds = maxBounds;
    ctx->listSize  = listSize;
}


//checkBounds :: NLSystemContext* -> uint32 -> bool
bool checkBounds(NLSystemContext* ctx, uint32 boundsSize) {
    bool out = false;
    int i;

    for(i = 0; i < boundsSize; i++) {
        if((ctx->state[i] >= ctx->minBounds[i]) && (ctx->state[i] <= ctx->minBounds[i])) {
            out = true;
            continue;
        }
        //Implicit else:
        out = false;
        break;
    }

    return out;
}


//clearArray :: [bigFloat] -> uint32 -> Effect
void clearArray(bigFloat* source, uint32 numVars) {
    uint32 i;
    for(i = 0; i < numVars; i++) {
        mpf_clear(source[i]);
    }
}


//Jianmin :: NLSystemContext* -> Effect -> IO
void Jianmin(NLSystemContext* ctx) {
    uint32 i;
    unsigned long exponent;
    //Reactions:
    bigFloat r[78];     //temp-storage during calculations
    bigFloat r_f[74];   //forward reaction
    bigFloat r_b[74];   //backward reaction

    //Note: 'theta_H' is initialized in second bigFloat group below.
    bigFloat theta_A, theta_B, theta_C, theta_D, theta_E, theta_F, theta_G, theta_I, theta_J, theta_K,
             theta_L, theta_M, theta_N, theta_O, theta_P, theta_Q, theta_R, theta_S, theta_T, theta_U,
             theta_V, theta_W, theta_X, theta_Y, theta_Z, theta_Z1;
    bigFloat   free,   theta_H,   theta_OH,  theta_H2O,    theta_CH, theta_CH2, theta_CH3, theta_CH4,
           theta_CO, theta_CHO, theta_CH2O, theta_CH3O, theta_CH3OH;
    bigFloat K_H;
    bigFloat temp;
    bigFloat e;

    // define constants for forward and reverse rate constants.
    //NOTE: constants for k_f[55]-k_f[70] are not defined! (same for k_b[].)
    double in_k_f[78] = {
        6.249e7,  1.831e3,  9.567e2,  8.447e3, 1.863e5, 5.509e8,   5.982, 2.106e10,  7.139e4,  2.243e8,
        2.418e7,  1.247e8,  1.100e2, 5.791e12, 1.114e9, 9.955e3, 5.396e2,  3.706e3,  2.705e8,  7.040e9,
        5.501e8,  2.335e4, 1.630e10,  6.622e2, 6.464e2, 2.109e8,   8.910,  3.268e5,  1.890e5, 9.014e11,
        7.631e3,  6.303e2,  1.075e2,  9.362e7, 9.540e4, 2.636e8, 3.368e8, 1.615e10, 3.290e-3,  1.004e3,
        1.457e5,  2.380e2,  3.845e7,  3.778e7, 9.432e3, 1.666e3, 3.094e8,  1.557e7,  6.575e1,  1.372e2,
          3.003, 3.044e13, 1.047e16, 2.092e12, 1.020e3,       0,       0,        0,        0,        0,
              0,        0,        0,        0,       0,       0,       0,        0,        0,        0,
              0,  5.056e9,  1.396e9,  4.831e9, 9.712e6,   4.000, 2.403e6, 1.404e-1};

    double in_k_b[78] = {
         5.885e4, 3.070e6,  2.885e7, 8.560e1,    8.721,  3.131e5, 6.828e-12,  4.823e3,   1.020e4,    1.566,
         5.024e5, 3.056e6, 6.318e-1, 1.247e8, 8.518e-3, 6.388e10,   1.625e7,  1.514e5,   4.864e5,  1.941e2,
         1.750e6, 8.974e1, 5.505e-2, 1.555e1,  2.380e7,    1.986,   1.865e7,    1.668,   1.108e7,    1.962,
        1.902e11, 5.235e1,  1.311e7,   2.729,  2.606e8,  5.388e6,     4.689,  1.170e4, 2.457e-15, 1.833e-6,
        7.225e-5, 5.142e8, 4.046e12, 9.921e9,  3.620e7,  2.431e7,  1.802e13,  2.232e8,   7.117e7,  6.635e7,
         7.879e7, 1.230e8,  1.740e8, 1.640e8,  6.696e7,        0,         0,        0,         0,        0,
               0,       0,        0,       0,        0,        0,         0,        0,         0,        0,
               0, 2.126e8,    1.611, 1.848e6,  1.828e2,  3.558e8,   1.593e5, 1.336e10};

    bigFloat k_f[78];
    bigFloat k_b[78];
    
    // define partial pressures, Boltzman constant and temperature.
    //       guaiacol,    H2, catechol,  phenol, benzene, anisole.
    bigFloat      p_A,  p_H2,      p_M,     p_S,     p_X,     p_K, 
                 p_CO, p_H2O,    p_CH4, p_CH3OH,      KB,       T;

 
    double partialPressures[12] = {1.0, 1.0, 1.0e-5, 1.0e-5,       1.0e-5, 1.0e-5,
                                1.0e-6, 0.0,    0.0,    0.0, 8.6173324e-5,    573};


    //---------------------------------------------------------
    //INITIALIZATIONS:

    //init r[]:
    for(i = 0; i < 78; i++) {
        mpf_init(r[i]);
    }
    //init r_f[]:
    for(i = 0; i < 74; i++) {
        mpf_init(r_f[i]);
    }
    //init r_b[]:
    for(i = 0; i < 74; i++) {
        mpf_init(r_b[i]);
    }

    //init forward and reverse rate constants:
    initArray(k_f, in_k_f, 78);
    initArray(k_b, in_k_b, 78);

    //init the various thetas:
    mpf_init_set(theta_A     , ctx->state[0]);
    mpf_init_set(theta_E     , ctx->state[1]);
    mpf_init_set(theta_F     , ctx->state[2]);
    mpf_init_set(theta_G     , ctx->state[3]);
    mpf_init_set(theta_I     , ctx->state[4]);
    mpf_init_set(theta_L     , ctx->state[5]);
    mpf_init_set(theta_M     , ctx->state[6]);
    mpf_init_set(theta_N     , ctx->state[7]);
    mpf_init_set(theta_O     , ctx->state[8]);
    mpf_init_set(theta_R     , ctx->state[9]);
    mpf_init_set(theta_S     , ctx->state[10]);
    mpf_init_set(theta_U     , ctx->state[11]);
    mpf_init_set(theta_V     , ctx->state[12]);
    mpf_init_set(theta_X     , ctx->state[13]);
    mpf_init_set(free        , ctx->state[14]);
    mpf_init_set(theta_H     , ctx->state[15]);
    mpf_init_set(theta_OH    , ctx->state[16]);
    mpf_init_set(theta_H2O   , ctx->state[17]);
    mpf_init_set(theta_CH    , ctx->state[18]);
    mpf_init_set(theta_CH2   , ctx->state[19]);
    mpf_init_set(theta_CH3   , ctx->state[20]);
    mpf_init_set(theta_CH4   , ctx->state[21]);
    mpf_init_set(theta_CHO   , ctx->state[22]);
    mpf_init_set(theta_CH2O  , ctx->state[23]);
    mpf_init_set(theta_CH3O  , ctx->state[24]);
    mpf_init_set(theta_CH3OH , ctx->state[25]);
    mpf_init_set(theta_W     , ctx->state[26]);
    mpf_init_set(theta_T     , ctx->state[27]);
    mpf_init_set(theta_B     , ctx->state[28]);
    mpf_init_set(theta_J     , ctx->state[29]);
    mpf_init_set(theta_P     , ctx->state[30]);
    mpf_init_set(theta_C     , ctx->state[31]);
    mpf_init_set(theta_D     , ctx->state[32]);
    mpf_init_set(theta_K     , ctx->state[33]);
    mpf_init_set(theta_Q     , ctx->state[34]);
    mpf_init_set(theta_Y     , ctx->state[35]);
    mpf_init_set(theta_Z     , ctx->state[36]);
    mpf_init_set(theta_Z1    , ctx->state[37]);
    mpf_init_set(theta_CO    , ctx->state[38]);
    
    //init K_H, temp, and e:
    mpf_init(K_H);
    mpf_init(temp);
    mpf_init(e);
    //define e to 50 digits of precision:
    gmp_sscanf("2.71828182845904523536028747135266249775724709369995", "%F", e);
    
    //init partial pressures:
    mpf_init_set_d(p_A       , partialPressures[0]);
    mpf_init_set_d(p_H2      , partialPressures[1]);
    mpf_init_set_d(p_M       , partialPressures[2]);
    mpf_init_set_d(p_S       , partialPressures[3]);
    mpf_init_set_d(p_X       , partialPressures[4]);
    mpf_init_set_d(p_K       , partialPressures[5]); 
    mpf_init_set_d(p_CO      , partialPressures[6]);
    mpf_init_set_d(p_H2O     , partialPressures[7]);
    mpf_init_set_d(p_CH4     , partialPressures[8]);
    mpf_init_set_d(p_CH3OH   , partialPressures[9]);
    mpf_init_set_d(KB        , partialPressures[10]);
    mpf_init_set_d(T         , partialPressures[11]);


    //---------------------------------------------------------
    //MAIN MATH KERNEL:

    //FORWARD REACTION RATES:
    // calculate rates for all elementary steps.
    mpf_mul(    r_f[0],     k_f[0],        p_A);
    mpf_mul(    r_f[0],     r_f[0],       free);
    mpf_mul(    r_f[0],     r_f[0],       free);
    mpf_mul(    r_f[0],     r_f[0],       free);
    mpf_mul(    r_f[0],     r_f[0],       free);
    mpf_mul(    r_f[1],     k_f[1],    theta_A);
    mpf_mul(    r_f[1],     r_f[1],    theta_H);
    //r_f[2] and r_f[3] handled later on...
    mpf_mul(    r_f[4],     k_f[4],    theta_A);
    mpf_mul(    r_f[4],     r_f[4],       free);
    mpf_mul(    r_f[5],     k_f[5],    theta_A);
    mpf_mul(    r_f[5],     r_f[5],       free);
    mpf_mul(    r_f[6],     k_f[6],    theta_A);
    mpf_mul(    r_f[6],     r_f[6],       free);
    mpf_mul(    r_f[7],     k_f[7],    theta_A);
    mpf_mul(    r_f[7],     r_f[7],       free);
    mpf_mul(    r_f[8],     k_f[8],    theta_B);
    mpf_mul(    r_f[8],     r_f[8],       free);
    mpf_mul(    r_f[8],     r_f[8],       free);
    //r_f[9] and r_f[10] handled later on...
    mpf_mul(   r_f[11],    k_f[11],    theta_E);
    mpf_mul(   r_f[11],    r_f[11],    theta_H);
    mpf_mul(   r_f[12],    k_f[12],    theta_F);
    mpf_mul(   r_f[12],    r_f[12],       free);
    mpf_mul(   r_f[13],    k_f[13],    theta_F);
    mpf_mul(   r_f[13],    r_f[13],       free);
    mpf_mul(   r_f[14],    k_f[14],    theta_F);
    mpf_mul(   r_f[15],    k_f[15],    theta_G);
    mpf_mul(   r_f[15],    r_f[15],    theta_H);
    mpf_mul(   r_f[16],    k_f[16],    theta_G);
    mpf_mul(   r_f[16],    r_f[16],       free);
    mpf_mul(   r_f[17],    k_f[17],    theta_I);
    mpf_mul(   r_f[17],    r_f[17],       free);
    mpf_mul(   r_f[18],    k_f[18],    theta_I);
    mpf_mul(   r_f[18],    r_f[18],       free);
    mpf_mul(   r_f[18],    r_f[18],       free);
    mpf_mul(   r_f[19],    k_f[19],    theta_J);
    //r_f[20] handled later on...
    mpf_mul(   r_f[21],    k_f[21],    theta_L);
    mpf_mul(   r_f[21],    r_f[21],       free);
    mpf_mul(   r_f[22],    k_f[22],    theta_L);
    mpf_mul(   r_f[22],    r_f[22],       free);
    mpf_mul(   r_f[23],    k_f[23],    theta_M);
    mpf_mul(   r_f[23],    r_f[23],       free);
    mpf_mul(   r_f[24],    k_f[24],    theta_M);
    mpf_mul(   r_f[24],    r_f[24],    theta_H);
    mpf_mul(   r_f[25],    k_f[25],    theta_N);
    mpf_mul(   r_f[25],    r_f[25],    theta_H);
    mpf_mul(   r_f[26],    k_f[26],    theta_O);
    mpf_mul(   r_f[26],    r_f[26],       free);
    mpf_mul(   r_f[27],    k_f[27],    theta_O);
    mpf_mul(   r_f[27],    r_f[27],       free);
    mpf_mul(   r_f[28],    k_f[28],    theta_P);
    mpf_mul(   r_f[28],    r_f[28],    theta_H);
    //r[29] handled later on...
    mpf_mul(   r_f[30],    k_f[30],    theta_R);
    mpf_mul(   r_f[30],    r_f[30],    theta_H);
    mpf_mul(   r_f[31],    k_f[31],    theta_S);
    mpf_mul(   r_f[31],    r_f[31],       free);
    mpf_mul(   r_f[32],    k_f[32],    theta_S);
    mpf_mul(   r_f[32],    r_f[32],    theta_H);
    mpf_mul(   r_f[33],    k_f[33],    theta_T);
    mpf_mul(   r_f[33],    r_f[33],       free);
    mpf_mul(   r_f[34],    k_f[34],    theta_U);
    mpf_mul(   r_f[34],    r_f[34],    theta_H);
    mpf_mul(   r_f[35],    k_f[35],    theta_V);
    mpf_mul(   r_f[35],    r_f[35],    theta_H);
    mpf_mul(   r_f[36],    k_f[36],    theta_W);
    mpf_mul(   r_f[37],    k_f[37],    theta_F);
    mpf_mul(   r_f[37],    r_f[37],       free);
    //what happened to r_38?!
    mpf_mul(   r_f[39],    k_f[39],    theta_I);
    mpf_mul(   r_f[39],    r_f[39],       free);
    mpf_mul(   r_f[39],    r_f[39],       free);
    mpf_mul(   r_f[40],    k_f[40],    theta_B);
    mpf_mul(   r_f[40],    r_f[40],       free);
    mpf_mul(   r_f[40],    r_f[40],       free);
    mpf_mul(   r_f[41],    k_f[41], theta_CH3O);
    mpf_mul(   r_f[41],    r_f[41],    theta_H);
    mpf_mul(   r_f[42],    k_f[42],   theta_CH);
    mpf_mul(   r_f[42],    r_f[42],    theta_H);
    mpf_mul(   r_f[43],    k_f[43],  theta_CH2);
    mpf_mul(   r_f[43],    r_f[43],    theta_H);
    mpf_mul(   r_f[44],    k_f[44],  theta_CH3);
    mpf_mul(   r_f[44],    r_f[44],    theta_H);
    mpf_mul(   r_f[45],    k_f[45],   theta_OH);
    mpf_mul(   r_f[45],    r_f[45],    theta_H);
    mpf_mul(   r_f[46],    k_f[46],  theta_CHO);
    mpf_mul(   r_f[46],    r_f[46],    theta_H);
    mpf_mul(   r_f[47],    k_f[47], theta_CH2O);
    mpf_mul(   r_f[47],    r_f[47],    theta_H);
    mpf_mul(   r_f[48],    k_f[48],    theta_S);
    mpf_mul(   r_f[49],    k_f[49],    theta_M);
    mpf_mul(   r_f[50],    k_f[50],    theta_X);
    mpf_mul(   r_f[51],    k_f[51], theta_CH3OH);
    mpf_mul(   r_f[52],    k_f[52],  theta_CH4);
    mpf_mul(   r_f[53],    k_f[53],  theta_H2O);
    mpf_mul(   r_f[54],    k_f[54],    theta_K);
    //not using r_f[55] through r_f[74]?!
    //also, consider making below assignments in-order (might help optimizer).
    mpf_mul(   r_f[71],    k_f[71],    theta_O);
    mpf_mul(   r_f[71],    r_f[71],       free);
    mpf_mul(   r_f[72],    k_f[72],    theta_Z);
    mpf_mul(   r_f[72],    r_f[72],       free);
    mpf_mul(   r_f[73],    k_f[73],    theta_Z);
    mpf_mul(   r_f[73],    r_f[73],       free);
    mpf_mul(   r_f[74],    k_f[74],   theta_Z1);
    mpf_mul(   r_f[75],    k_f[75],    theta_G);
    mpf_mul(   r_f[75],    r_f[75],    theta_H);
    mpf_mul(   r_f[76],    k_f[76],    theta_Y);
    mpf_mul(   r_f[76],    r_f[76],       free);
    mpf_mul(   r_f[77],    k_f[77],   theta_CO);
    mpf_mul(   r_f[77],    r_f[77],    theta_H);
    //
    // steps including C, D, K, Q.
    mpf_mul(    r_f[2],     k_f[2],    theta_A);
    mpf_mul(    r_f[2],     r_f[2],    theta_H);
    mpf_mul(    r_f[3],     k_f[3],    theta_A);
    mpf_mul(    r_f[3],     r_f[3],       free);
    mpf_mul(    r_f[9],     k_f[9],    theta_C);
    mpf_mul(    r_f[9],     r_f[9],       free);
    mpf_mul(   r_f[10],    k_f[10],    theta_D);
    mpf_mul(   r_f[10],    r_f[10],    theta_H);
    mpf_mul(   r_f[20],    k_f[20],    theta_K);
    mpf_mul(   r_f[20],    r_f[20],       free);
    mpf_mul(   r_f[29],    k_f[29],    theta_Q);
    mpf_mul(   r_f[29],    r_f[29],       free);


    //REVERSE REACTION RATES:
    mpf_mul(    r_b[0],     k_b[0],    theta_A);
    mpf_mul(    r_b[1],     k_b[1],    theta_B);
    mpf_mul(    r_b[1],     r_b[1],       free);
    //r[2] and r[3] handled later on...
    mpf_mul(    r_b[4],     k_b[4],    theta_E);
    mpf_mul(    r_b[4],     r_b[4], theta_CH3O);
    mpf_mul(    r_b[5],     k_b[5],    theta_F);
    mpf_mul(    r_b[5],     r_b[5],    theta_H);
    mpf_mul(    r_b[6],     k_b[6],    theta_G);
    mpf_mul(    r_b[6],     r_b[6],  theta_CH3);
    mpf_mul(    r_b[7],     k_b[7],    theta_I);
    mpf_mul(    r_b[7],     r_b[7],    theta_H);
    mpf_mul(    r_b[8],     k_b[8],    theta_J);
    mpf_mul(    r_b[8],     r_b[8],    theta_H);
    //r[9] and r[10] handled later on...
    mpf_mul(   r_b[11],    k_b[11],    theta_S);
    mpf_mul(   r_b[11],    r_b[11],       free);
    mpf_mul(   r_b[12],    k_b[12],    theta_E);
    mpf_mul(   r_b[12],    r_b[12], theta_CH2O);
    mpf_mul(   r_b[13],    k_b[13],    theta_L);
    mpf_mul(   r_b[13],    r_b[13],    theta_H);
    mpf_mul(   r_b[14],    k_b[14],    theta_G);
    mpf_mul(   r_b[14],    r_b[14],  theta_CH2);
    mpf_mul(   r_b[15],    k_b[15],    theta_M);
    mpf_mul(   r_b[15],    r_b[15],       free);
    mpf_mul(   r_b[16],    k_b[16],    theta_N);
    mpf_mul(   r_b[16],    r_b[16],   theta_OH);
    mpf_mul(   r_b[17],    k_b[17],    theta_N);
    mpf_mul(   r_b[17],    r_b[17], theta_CH3O);
    mpf_mul(   r_b[18],    k_b[18],    theta_O);
    mpf_mul(   r_b[18],    r_b[18],    theta_H);
    mpf_mul(   r_b[19],    k_b[19],    theta_P);
    mpf_mul(   r_b[19],    r_b[19],  theta_CH2);
    //r[20] handled later on...
    mpf_mul(   r_b[21],    k_b[21],    theta_E);
    mpf_mul(   r_b[21],    r_b[21],  theta_CHO);
    mpf_mul(   r_b[22],    k_b[22],    theta_G);
    mpf_mul(   r_b[22],    r_b[22],   theta_CH);
    mpf_mul(   r_b[23],    k_b[23],    theta_E);
    mpf_mul(   r_b[23],    r_b[23],   theta_OH);
    mpf_mul(   r_b[24],    k_b[24],    theta_T);
    mpf_mul(   r_b[25],    k_b[25],    theta_R);
    mpf_mul(   r_b[25],    r_b[25],       free);
    mpf_mul(   r_b[26],    k_b[26],    theta_N);
    mpf_mul(   r_b[26],    r_b[26], theta_CH2O);
    mpf_mul(   r_b[27],    k_b[27],    theta_U);
    mpf_mul(   r_b[27],    r_b[27],  theta_CH2);
    mpf_mul(   r_b[28],    k_b[28],    theta_T);
    mpf_mul(   r_b[28],    r_b[28],       free);
    //r[29] handled later on...
    mpf_mul(   r_b[30],    k_b[30],    theta_S);
    mpf_mul(   r_b[30],    r_b[30],       free);
    mpf_mul(   r_b[31],    k_b[31],    theta_V);
    mpf_mul(   r_b[31],    r_b[31],   theta_OH);
    mpf_mul(   r_b[32],    k_b[32],    theta_W);
    mpf_mul(   r_b[32],    r_b[32],       free);
    mpf_mul(   r_b[33],    k_b[33],    theta_S);
    mpf_mul(   r_b[33],    r_b[33],   theta_OH);
    mpf_mul(   r_b[34],    k_b[34],    theta_G);
    mpf_mul(   r_b[34],    r_b[34],       free);
    mpf_mul(   r_b[34],    r_b[34],       free);
    mpf_mul(   r_b[35],    k_b[35],    theta_X);
    mpf_mul(   r_b[35],    r_b[35],       free);
    mpf_mul(   r_b[35],    r_b[35],       free);
    mpf_mul(   r_b[36],    k_b[36],    theta_X);
    mpf_mul(   r_b[36],    r_b[36],   theta_OH);
    mpf_mul(   r_b[37],    k_b[37],    theta_O);
    mpf_mul(   r_b[37],    r_b[37],    theta_H);
    //what happened to r_38?!
    mpf_mul(   r_b[39],    k_b[39],    theta_U);
    mpf_mul(   r_b[39],    r_b[39],  theta_CH3);
    mpf_mul(   r_b[40],    k_b[40],    theta_S);
    mpf_mul(   r_b[40],    r_b[40], theta_CH3O);
    mpf_mul(   r_b[41],    k_b[41], theta_CH3OH);
    mpf_mul(   r_b[41],    r_b[41],       free);
    mpf_mul(   r_b[42],    k_b[42],  theta_CH2);
    mpf_mul(   r_b[42],    r_b[42],       free);
    mpf_mul(   r_b[43],    k_b[43],  theta_CH3);
    mpf_mul(   r_b[43],    r_b[43],       free);
    mpf_mul(   r_b[44],    k_b[44],  theta_CH4);
    mpf_mul(   r_b[44],    r_b[44],       free);
    mpf_mul(   r_b[45],    k_b[45],  theta_H2O);
    mpf_mul(   r_b[45],    r_b[45],       free);
    mpf_mul(   r_b[46],    k_b[46], theta_CH2O);
    mpf_mul(   r_b[46],    r_b[46],       free);
    mpf_mul(   r_b[47],    k_b[47], theta_CH3O);
    mpf_mul(   r_b[47],    r_b[47],       free);
    mpf_mul(   r_b[47],    r_b[47],       free);
    mpf_mul(   r_b[48],    k_b[48],        p_S);
    mpf_mul(   r_b[48],    r_b[48],       free);
    mpf_mul(   r_b[48],    r_b[48],       free);
    mpf_mul(   r_b[48],    r_b[48],       free);
    mpf_mul(   r_b[48],    r_b[48],       free);
    mpf_mul(   r_b[49],    k_b[49],        p_M);
    mpf_mul(   r_b[49],    r_b[49],       free);
    mpf_mul(   r_b[49],    r_b[49],       free);
    mpf_mul(   r_b[49],    r_b[49],       free);
    mpf_mul(   r_b[49],    r_b[49],       free);
    mpf_mul(   r_b[50],    k_b[50],        p_X);
    mpf_mul(   r_b[50],    r_b[50],       free);
    mpf_mul(   r_b[50],    r_b[50],       free);
    mpf_mul(   r_b[50],    r_b[50],       free);
    mpf_mul(   r_b[51],    k_b[51],    p_CH3OH);
    mpf_mul(   r_b[51],    r_b[51],       free);
    mpf_mul(   r_b[52],    k_b[52],      p_CH4);
    mpf_mul(   r_b[52],    r_b[52],       free);
    mpf_mul(   r_b[53],    k_b[53],      p_H2O);
    mpf_mul(   r_b[53],    r_b[53],       free);
    mpf_mul(   r_b[54],    k_b[54],        p_K);
    mpf_mul(   r_b[54],    r_b[54],       free);
    mpf_mul(   r_b[54],    r_b[54],       free);
    mpf_mul(   r_b[54],    r_b[54],       free);
    mpf_mul(   r_b[54],    r_b[54],       free);
    //not using r[55] through r[74]?!
    //also, consider making below assignments in-order (might help optimizer).
    mpf_mul(   r_b[71],    k_b[71],    theta_Z);
    mpf_mul(   r_b[71],    r_b[71],    theta_H);
    mpf_mul(   r_b[72],    k_b[72],    theta_U);
    mpf_mul(   r_b[72],    r_b[72],   theta_CH);
    mpf_mul(   r_b[73],    k_b[73],   theta_Z1);
    mpf_mul(   r_b[73],    r_b[73],    theta_H);
    mpf_mul(   r_b[74],    k_b[74],    theta_N);
    mpf_mul(   r_b[74],    r_b[74],   theta_CO);
    mpf_mul(   r_b[75],    k_b[75],    theta_Y);
    mpf_mul(   r_b[75],    r_b[75],       free);
    mpf_mul(   r_b[76],    k_b[76],    theta_R);
    mpf_mul(   r_b[76],    r_b[76],   theta_OH);
    mpf_mul(   r_b[77],    k_b[77],  theta_CHO);
    //
    // steps including C, D, K, Q.
    mpf_mul(    r_b[2],     k_b[2],    theta_C);
    mpf_mul(    r_b[2],     r_b[2],       free);
    mpf_mul(    r_b[3],     k_b[3],    theta_D);
    mpf_mul(    r_b[3],     r_b[3],   theta_OH);
    mpf_mul(    r_b[9],     k_b[9],    theta_K);
    mpf_mul(    r_b[9],     r_b[9],   theta_OH);
    mpf_mul(   r_b[10],    k_b[10],    theta_K);
    mpf_mul(   r_b[10],    r_b[10],       free);
    mpf_mul(   r_b[20],    k_b[20],    theta_Q);
    mpf_mul(   r_b[20],    r_b[20],    theta_H);
    mpf_mul(   r_b[29],    k_b[29],    theta_R);
    mpf_mul(   r_b[29],    r_b[29],  theta_CH2);


    //OVERALL REACTION RATES:
    for(i = 0; i < 74; i++) {
        mpf_sub(      r[i],     r_f[i],     r_b[i]);
    }
    

    //---------------------------------------------------------


    // apply the steady state approximation for all thetas.
    //NOTE: need to put in GNU MP ops + rewrite to array accesses.
    /*out[0]  = r_04 + r_12 + r_21 + r_23 - r_11;     // d(theta_E)/dt=0
    out[1]  = r_05 - r_12 - r_13 - r_14 - r_37;     // d(theta_F)/dt=0
    out[2]  = r_06 + r_14 + r_22 + r_34 - r_15 - r_16 - r_75; // d(theta_G)/dt=0
    out[3]  = r_07 - r_17 - r_18 - r_39;            // d(theta_I)/dt=0
    out[4]  = r_13 - r_21 - r_22;                   // d(theta_L)/dt=0
    out[5]  = r_15 - r_23 - r_24 - r_49;            // d(theta_M)/dt=0 catechol
    out[6]  = r_16 + r_17 + r_26 + r_74 - r_25;     // d(theta_N)/dt=0
    out[7]  = r_18 + r_37 - r_26 - r_27 - r_71;     // d(theta_O)/dt=0
    out[8]  = r_25 + r_29 + r_76 - r_30;            // d(theta_R)/dt=0
    out[9] = r_11 + r_30 + r_33 + r_40 - r_31 - r_32 - r_48; // d(theta_S)/dt=0 phenol
    out[10] = r_27 + r_39 + r_72 - r_34;            // d(theta_U)/dt=0
    out[11] = r_31 - r_35;                          // d(theta_V)/dt=0
    out[12] = r_35 + r_36 - r_50;                   // d(theta_X)/dt=0 benzene

    out[13] = r_03 + r_09 + r_23 + r_31 + r_31 + r_33 - r_45; // d(theta_OH)/dt=0
    out[14] = r_45 - r_53;                          // d(theta_H2O)/dt=0
    out[15] = r_22 + r_72 - r_42;                   // d(theta_CH)/dt =0
    out[16] = r_14 + r_19 + r_27 + r_29 + r_42 - r_43; // d(theta_CH2)/dt=0    
    out[17] = r_06 + r_43 - r_44;                   // d(theta_CH3)/dt=0
    out[18] = r_44 - r_52;                          // d(theta_CH4)/dt=0
    out[19] = r_21 + r_77 - r_46;                   // d(theta_CHO)/dt=0
    out[20] = r_12 + r_26 + r_46 - r_47;            // d(theta_CH2O)/dt=0
    out[21] = r_04 + r_17 + r_47 - r_41;            // d(theta_CH3O)/dt=0
    out[22] = r_41 - r_51;                          // d(theta_CH3OH)/dt=0
    out[23] = r_00 - r_01 - r_04 - r_05 - r_06 - r_07; // d(theta_A)/dt=0
//    out[23] = theta_A - k_00_f/k_00_b*p_A*free*free*free*free; // d(theta_A)/dt=0 if step 0 is in equilibrium.
    out[24] = r_32 - r_36;                          // d(theta_W)/dt=0
    out[25] = r_24 + r_28 - r_33;                   // d(theta_T)/dt=0
    out[26] = r_01 - r_08 - r_40;                   // d(theta_B)/dt=0
    out[27] = r_08 - r_19;                          // d(theta_J)/dt=0
    out[28] = r_19 - r_28;                          // d(theta_P)/dt=0
    out[29] = theta_H - exp(-( (-1.374+0.076+0.683)/2 + 2*0.084*(theta_H-0.139))/KB/T)*pow(p_H2,0.5)*free; //theta_H
    out[30] = r_02 - r_09;                          // d(theta_C)/dt=0
    out[31] = r_03 - r_10;                          // d(theta_D)/dt=0
    out[32] = r_09 + r_10 - r_20 - r_54;            // d(theta_K)/dt=0
    out[33] = r_20 - r_29;                          // d(theta_Q)/dt=0
    out[34] = r_75 - r_76;                          // d(theta_Y)/dt=0
    out[35] = r_71 - r_72 - r_73;                   // d(theta_Z)/dt=0
    out[36] = r_73 - r_74;                          // d(theta_Z1)/dt=0
    out[37] = theta_CO - exp(-(-2.131+0.028+1.764)/KB/T)*p_CO*free; // d(theta_CO)/dt=0*/

    // finally the summation of all thetas should be 1.
    //NOTE: need to put in GNU MP ops.
    /*mpf_set(out[38], ( 4*ctx->state[0]  + 4*ctx->state[1]  + 4*ctx->state[2]  + 4*ctx->state[3]
                     + 4*ctx->state[4]  + 4*ctx->state[5]  + 4*ctx->state[6]  + 4*ctx->state[7]
                     + 4*ctx->state[8]  + 4*ctx->state[9]  + 4*ctx->state[10] + 5*ctx->state[11]
                     + 3*ctx->state[12] + 3*ctx->state[13] + ctx->state[14]   + ctx->state[15]
                     + ctx->state[16]   + ctx->state[17]   + ctx->state[18]   + 2*ctx->state[19]
                     + ctx->state[20]   + ctx->state[21]   + 2*ctx->state[22] + 2*ctx->state[23]
                     + ctx->state[24]   + ctx->state[25]   + 4*ctx->state[26] + 5*ctx->state[27]
                     + 4*ctx->state[28] + 4*ctx->state[29] + 5*ctx->state[30] + 4*ctx->state[31]
                     + 4*ctx->state[32] + 4*ctx->state[33] + 5*ctx->state[34] + 4*ctx->state[35]
                     + 4*ctx->state[36] + 4*ctx->state[37] + ctx->state[38]   - 1.00 )
             );*/

    //NOTE: need to put in GNU MP ops + rewrite to array accesses.
    /*K_H = exp(-( (-1.374+0.076+0.683)/2 + 2*0.084*(theta_H-0.139))/KB/T);*/


    //---------------------------------------------------------
    //OUTPUT:
    //To send output to a file, run this program like so:
    //`$ ./theta.exe > output.txt`
    printf("OVERALL REACTION RATES:\n");
    for(i = 0; i < 78; i++) {
        gmp_printf("r[%d] = %Fg\n", i, r[i]);
    }
    gmp_printf("K_H = %Fg\n", K_H);

    printf("\nFORWARD REACTION RATES:\n");
    for(i = 0; i < 74; i++) {
        gmp_printf("r_f[%d] = %Fg\n", i, r_f[i]);
    }

    printf("\nREVERSE REACTION RATES:\n");
    for(i = 0; i < 74; i++) {
        gmp_printf("r_b[%d] = %Fg\n", i, r_b[i]);
    }


    //---------------------------------------------------------
    //FREES:

    //free up the memory GNU MP allocated behind the scenes:

    //free r[]:
    for(i = 0; i < 78; i++) {
        mpf_clear(r[i]);
    }
    //free r_f[]:
    for(i = 0; i < 74; i++) {
        mpf_clear(r_f[i]);
    }
    //free r_b[]:
    for(i = 0; i < 74; i++) {
        mpf_clear(r_b[i]);
    }

    //free forward and reverse rate constants:
    clearArray(k_f, 78);
    clearArray(k_b, 78);

    //free the various thetas:
    mpf_clear(theta_A);
    mpf_clear(theta_E);
    mpf_clear(theta_F);
    mpf_clear(theta_G);
    mpf_clear(theta_I);
    mpf_clear(theta_L);
    mpf_clear(theta_M);
    mpf_clear(theta_N);
    mpf_clear(theta_O);
    mpf_clear(theta_R);
    mpf_clear(theta_S);
    mpf_clear(theta_U);
    mpf_clear(theta_V);
    mpf_clear(theta_X);
    mpf_clear(free);
    mpf_clear(theta_H);
    mpf_clear(theta_OH);
    mpf_clear(theta_H2O);
    mpf_clear(theta_CH);
    mpf_clear(theta_CH2);
    mpf_clear(theta_CH3);
    mpf_clear(theta_CH4);
    mpf_clear(theta_CHO);
    mpf_clear(theta_CH2O);
    mpf_clear(theta_CH3O);
    mpf_clear(theta_CH3OH);
    mpf_clear(theta_W);
    mpf_clear(theta_T);
    mpf_clear(theta_B);
    mpf_clear(theta_J);
    mpf_clear(theta_P);
    mpf_clear(theta_C);
    mpf_clear(theta_D);
    mpf_clear(theta_K);
    mpf_clear(theta_Q);
    mpf_clear(theta_Y);
    mpf_clear(theta_Z);
    mpf_clear(theta_Z1);
    mpf_clear(theta_CO);

    //free K_H, temp, and e:
    mpf_clear(K_H);
    mpf_clear(temp);
    mpf_clear(e);

    //free partial pressures:
    mpf_clear(p_A);
    mpf_clear(p_H2);
    mpf_clear(p_M);
    mpf_clear(p_S);
    mpf_clear(p_X);
    mpf_clear(p_K); 
    mpf_clear(p_CO);
    mpf_clear(p_H2O);
    mpf_clear(p_CH4);
    mpf_clear(p_CH3OH);
    mpf_clear(KB);
    mpf_clear(T);


    //---------------------------------------------------------

}


int main(int argc, char** argv[]) {
    NLSystemContext ctx;
    bool inBounds;
    uint32 i;

    //Set default precision for GNU MP:
    mpf_set_default_prec(256);

    //Initialize our bigFloat arrays:
    initArray(state, in_systemVars, 39);
    initArray(minBounds, in_minBounds, 39);
    initArray(maxBounds, in_maxBounds, 39);

    //Initialize our NLSystemContext:
    initNLSystemContext(&ctx, state, minBounds, maxBounds, 39);

    //Run the main non-linear function:
    Jianmin(&ctx);

    //Check to make sure the system stayed within constraints:
    inBounds = checkBounds(&ctx, 39);

    if(inBounds == false) {
        printf("\nThe system strayed outside of its constraints! Please check your math.\n");
    }
    
    //free up the memory GNU MP allocated behind the scenes:
    clearArray(state, 39);
    clearArray(minBounds, 39);
    clearArray(maxBounds, 39);

    return 0;
}
