# Name: gmpgen.py -- helper script for making long GNU MP programs.
# Author: Philip Conrad on 4/30/2013 @ 2:35 PM
# License: MIT-License

import sys
from ast import literal_eval


rate_calc = [
    #// calculate rates for all elementary steps.
    ('//', ' calculate rates for all elementary steps.'),
    #r[0] = k_f[0]*p_A*free*free*free*free - k_b[0]*theta_A;
    ('*', 'r[0]', 'k_f[0]', 'p_A'),
    ('*', 'r[0]', 'r[0]', 'free'),
    ('*', 'r[0]', 'r[0]', 'free'),
    ('*', 'r[0]', 'r[0]', 'free'),
    ('*', 'r[0]', 'r[0]', 'free'),
    ('*', 'temp', 'k_b[0]', 'theta_A'),
    ('-', 'r[0]', 'r[0]', 'temp'),
    #r[1] = k_f[1]*theta_A*theta_H - k_f[1]*theta_B*free;
    ('*', 'r[1]', 'k_f[1]', 'theta_A'),
    ('*', 'r[1]', 'r[1]', 'theta_H'),
    ('*', 'temp', 'k_b[1]', 'theta_B'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[1]', 'r[1]', 'temp'),
    #//r[2] and r[3] handled later on...
    ('//', 'r[2] and r[3] handled later on...'),
    #r[4] = k_f[4]*theta_A*free - k_b[4]*theta_E*theta_CH3O;
    ('*', 'r[4]', 'k_f[4]', 'theta_A'),
    ('*', 'r[4]', 'r[4]', 'free'),
    ('*', 'temp', 'k_b[4]', 'theta_E'),
    ('*', 'temp', 'temp', 'theta_CH3O'),
    ('-', 'r[4]', 'r[4]', 'temp'),
    #r[5] = k_f[5]*theta_A*free - k_b[5]*theta_F*theta_H;
    ('*', 'r[5]', 'k_f[5]', 'theta_A'),
    ('*', 'r[5]', 'r[5]', 'free'),
    ('*', 'temp', 'k_b[5]', 'theta_F'),
    ('*', 'temp', 'temp', 'theta_H'),
    ('-', 'r[5]', 'r[5]', 'temp'),
    #r[6] = k_f[6]*theta_A*free - k_b[6]*theta_G*theta_CH3;
    ('*', 'r[6]', 'k_f[6]', 'theta_A'),
    ('*', 'r[6]', 'r[6]', 'free'),
    ('*', 'temp', 'k_b[6]', 'theta_G'),
    ('*', 'temp', 'temp', 'theta_CH3'),
    ('-', 'r[6]', 'r[6]', 'temp'),
    #r[7] = k_f[7]*theta_A*free - k_b[7]*theta_I*theta_H;
    ('*', 'r[7]', 'k_f[7]', 'theta_A'),
    ('*', 'r[7]', 'r[7]', 'free'),
    ('*', 'temp', 'k_b[7]', 'theta_I'),
    ('*', 'temp', 'temp', 'theta_H'),
    ('-', 'r[7]', 'r[7]', 'temp'),
    #r[8] = k_f[8]*theta_B*free*free - k_b[8]*theta_J*theta_H;
    ('*', 'r[8]', 'k_f[8]', 'theta_B'),
    ('*', 'r[8]', 'r[8]', 'free'),
    ('*', 'r[8]', 'r[8]', 'free'),
    ('*', 'temp', 'k_b[8]', 'theta_J'),
    ('*', 'temp', 'temp', 'theta_H'),
    ('-', 'r[8]', 'r[8]', 'temp'),
    #//r[10] handled later on...
    ('//', 'r[10] handled later on...'),
    #r[11] = k_f[11]*theta_E*theta_H - k_b[11]*theta_S*free;
    ('*', 'r[11]', 'k_f[11]', 'theta_E'),
    ('*', 'r[11]', 'r[11]', 'theta_H'),
    ('*', 'temp', 'k_b[11]', 'theta_S'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[11]', 'r[11]', 'temp'),
    #r[12] = k_f[12]*theta_F*free - k_b[12]*theta_E*theta_CH2O;
    ('*', 'r[12]', 'k_f[12]', 'theta_F'),
    ('*', 'r[12]', 'r[12]', 'free'),
    ('*', 'temp', 'k_b[12]', 'theta_E'),
    ('*', 'temp', 'temp', 'theta_CH2O'),
    ('-', 'r[12]', 'r[12]', 'temp'),
    #r[13] = k_f[13]*theta_F*free - k_b[13]*theta_L*theta_H;
    ('*', 'r[13]', 'k_f[13]', 'theta_F'),
    ('*', 'r[13]', 'r[13]', 'free'),
    ('*', 'temp', 'k_b[13]', 'theta_L'),
    ('*', 'temp', 'temp', 'theta_H'),
    ('-', 'r[13]', 'r[13]', 'temp'),
    #r[14] = k_f[14]*theta_F - k_b[14]*theta_G*theta_CH2;
    ('*', 'r[14]', 'k_f[14]', 'theta_F'),
    ('*', 'temp', 'k_b[14]', 'theta_G'),
    ('*', 'temp', 'temp', 'theta_CH2'),
    ('-', 'r[14]', 'r[14]', 'temp'),
    #r[15] = k_f[15]*theta_G*theta_H - k_b[15]*theta_M*free;
    ('*', 'r[15]', 'k_f[15]', 'theta_G'),
    ('*', 'r[15]', 'r[15]', 'theta_H'),
    ('*', 'temp', 'k_b[15]', 'theta_M'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[15]', 'r[15]', 'temp'),
    #r[16] = k_f[16]*theta_G*free - k_b[16]*theta_N*theta_OH;
    ('*', 'r[16]', 'k_f[16]', 'theta_G'),
    ('*', 'r[16]', 'r[16]', 'free'),
    ('*', 'temp', 'k_b[16]', 'theta_N'),
    ('*', 'temp', 'temp', 'theta_OH'),
    ('-', 'r[16]', 'r[16]', 'temp'),
    #r[17] = k_f[17]*theta_I*free - k_b[17]*theta_N*theta_CH3O;
    ('*', 'r[17]', 'k_f[17]', 'theta_I'),
    ('*', 'r[17]', 'r[17]', 'free'),
    ('*', 'temp', 'k_b[17]', 'theta_N'),
    ('*', 'temp', 'temp', 'theta_CH3O'),
    ('-', 'r[17]', 'r[17]', 'temp'),
    #r[18] = k_f[18]*theta_I*free*free - k_b[18]*theta_O*theta_H;
    ('*', 'r[18]', 'k_f[18]', 'theta_I'),
    ('*', 'r[18]', 'r[18]', 'free'),
    ('*', 'r[18]', 'r[18]', 'free'),
    ('*', 'temp', 'k_b[18]', 'theta_O'),
    ('*', 'temp', 'temp', 'theta_H'),
    ('-', 'r[18]', 'r[18]', 'temp'),
    #//r[20] handled later on...
    ('//', 'r[20] handled later on...'),
    #r[21] = k_f[21]*theta_L*free - k_b[21]*theta_E*theta_CHO;
    ('*', 'r[21]', 'k_f[21]', 'theta_L'),
    ('*', 'r[21]', 'r[21]', 'free'),
    ('*', 'temp', 'k_b[21]', 'theta_E'),
    ('*', 'temp', 'temp', 'theta_CHO'),
    ('-', 'r[21]', 'r[21]', 'temp'),
    #r[22] = k_f[22]*theta_L*free - k_b[22]*theta_G*theta_CH;
    ('*', 'r[22]', 'k_f[22]', 'theta_L'),
    ('*', 'r[22]', 'r[22]', 'free'),
    ('*', 'temp', 'k_b[22]', 'theta_G'),
    ('*', 'temp', 'temp', 'theta_CH'),
    ('-', 'r[22]', 'r[22]', 'temp'),
    #r[23] = k_f[23]*theta_M*free - k_b[23]*theta_E*theta_OH;
    ('*', 'r[23]', 'k_f[23]', 'theta_M'),
    ('*', 'r[23]', 'r[23]', 'free'),
    ('*', 'temp', 'k_b[23]', 'theta_E'),
    ('*', 'temp', 'temp', 'theta_OH'),
    ('-', 'r[23]', 'r[23]', 'temp'),
    #r[24] = k_f[24]*theta_M*theta_H - k_b[24]*theta_T;
    ('*', 'r[25]', 'k_f[25]', 'theta_M'),
    ('*', 'r[25]', 'r[25]', 'theta_H'),
    ('*', 'temp', 'k_b[25]', 'theta_T'),
    ('-', 'r[25]', 'r[25]', 'temp'),
    #r[25] = k_f[25]*theta_N*theta_H - k_b[25]*theta_R*free;
    ('*', 'r[25]', 'k_f[25]', 'theta_N'),
    ('*', 'r[25]', 'r[25]', 'theta_H'),
    ('*', 'temp', 'k_b[25]', 'theta_R'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[25]', 'r[25]', 'temp'),
    #r[26] = k_f[26]*theta_O*free - k_b[26]*theta_N*theta_CH2O;
    ('*', 'r[26]', 'k_f[26]', 'theta_O'),
    ('*', 'r[26]', 'r[26]', 'free'),
    ('*', 'temp', 'k_b[26]', 'theta_N'),
    ('*', 'temp', 'temp', 'theta_CH2O'),
    ('-', 'r[26]', 'r[26]', 'temp'),
    #r[27] = k_f[27]*theta_O*free - k_b[27]*theta_U*theta_CH2;
    ('*', 'r[27]', 'k_f[27]', 'theta_O'),
    ('*', 'r[27]', 'r[27]', 'free'),
    ('*', 'temp', 'k_b[27]', 'theta_U'),
    ('*', 'temp', 'temp', 'theta_CH2'),
    ('-', 'r[27]', 'r[27]', 'temp'),
    #r[28] = k_f[28]*theta_P*theta_H - k_b[28]*theta_T*free;
    ('*', 'r[28]', 'k_f[28]', 'theta_P'),
    ('*', 'r[28]', 'r[28]', 'theta_H'),
    ('*', 'temp', 'k_b[28]', 'theta_T'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[28]', 'r[28]', 'temp'),
    #//r[29] handled later on...
    ('//', 'r[29] handled later on...'),
    #r[30] = k_f[30]*theta_R*theta_H - k_b[30]*theta_S*free;
    ('*', 'r[30]', 'k_f[30]', 'theta_R'),
    ('*', 'r[30]', 'r[30]', 'theta_H'),
    ('*', 'temp', 'k_b[30]', 'theta_S'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[30]', 'r[30]', 'temp'),
    #r[31] = k_f[31]*theta_S*free - k_b[31]*theta_V*theta_OH;
    ('*', 'r[31]', 'k_f[31]', 'theta_S'),
    ('*', 'r[31]', 'r[31]', 'free'),
    ('*', 'temp', 'k_b[31]', 'theta_V'),
    ('*', 'temp', 'temp', 'theta_OH'),
    ('-', 'r[31]', 'r[31]', 'temp'),
    #r[32] = k_f[32]*theta_S*theta_H - k_b[32]*theta_W*free;
    ('*', 'r[32]', 'k_f[32]', 'theta_S'),
    ('*', 'r[32]', 'r[32]', 'theta_H'),
    ('*', 'temp', 'k_b[32]', 'theta_W'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[32]', 'r[32]', 'temp'),
    #r[33] = k_f[33]*theta_T*free - k_b[33]*theta_S*theta_OH;
    ('*', 'r[33]', 'k_f[33]', 'theta_T'),
    ('*', 'r[33]', 'r[33]', 'free'),
    ('*', 'temp', 'k_b[33]', 'theta_S'),
    ('*', 'temp', 'temp', 'theta_OH'),
    ('-', 'r[33]', 'r[33]', 'temp'),
    #r[34] = k_f[34]*theta_U*theta_H - k_b[34]*theta_G*free*free;
    ('*', 'r[34]', 'k_f[34]', 'theta_U'),
    ('*', 'r[34]', 'r[34]', 'theta_H'),
    ('*', 'temp', 'k_b[34]', 'theta_G'),
    ('*', 'temp', 'temp', 'free'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[34]', 'r[34]', 'temp'),
    #r[35] = k_f[35]*theta_V*theta_H - k_b[35]*theta_X*free*free;
    ('*', 'r[35]', 'k_f[35]', 'theta_V'),
    ('*', 'r[35]', 'r[35]', 'theta_H'),
    ('*', 'temp', 'k_b[35]', 'theta_X'),
    ('*', 'temp', 'temp', 'free'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[35]', 'r[35]', 'temp'),
    #r[36] = k_f[36]*theta_W - k_b[36]*theta_X*theta_OH;
    ('*', 'r[36]', 'k_f[36]', 'theta_W'),
    ('*', 'temp', 'k_b[36]', 'theta_X'),
    ('*', 'temp', 'temp', 'theta_OH'),
    ('-', 'r[36]', 'r[36]', 'temp'),
    #r[37] = k_f[37]*theta_F*free - k_b[37]*theta_O*theta_H;
    ('*', 'r[34]', 'k_f[34]', 'theta_F'),
    ('*', 'r[34]', 'r[34]', 'free'),
    ('*', 'temp', 'k_b[34]', 'theta_O'),
    ('*', 'temp', 'temp', 'theta_H'),
    ('-', 'r[34]', 'r[34]', 'temp'),
    #//what happened to r_38?!
    ('//', 'what happened to r_38?!'),
    #r[39] = k_f[39]*theta_I*free*free - k_b[39]*theta_U*theta_CH3;
    ('*', 'r[39]', 'k_f[39]', 'theta_I'),
    ('*', 'r[39]', 'r[39]', 'free'),
    ('*', 'r[39]', 'r[39]', 'free'),
    ('*', 'temp', 'k_b[39]', 'theta_U'),
    ('*', 'temp', 'temp', 'theta_CH3'),
    ('-', 'r[39]', 'r[39]', 'temp'),
    #r[40] = k_f[40]*theta_B*free*free - k_b[40]*theta_S*theta_CH3O;
    ('*', 'r[40]', 'k_f[40]', 'theta_B'),
    ('*', 'r[40]', 'r[40]', 'free'),
    ('*', 'r[40]', 'r[40]', 'free'),
    ('*', 'temp', 'k_b[40]', 'theta_S'),
    ('*', 'temp', 'temp', 'theta_CH3O'),
    ('-', 'r[40]', 'r[40]', 'temp'),
    #r[41] = k_f[41]*theta_CH3O*theta_H - k_b[41]*theta_CH3OH*free;
    ('*', 'r[41]', 'k_f[41]', 'theta_CH3O'),
    ('*', 'r[41]', 'r[41]', 'theta_H'),
    ('*', 'temp', 'k_b[41]', 'theta_CH3OH'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[41]', 'r[41]', 'temp'),
    #r[42] = k_f[42]*theta_CH*theta_H - k_b[42]*theta_CH2*free;
    ('*', 'r[42]', 'k_f[42]', 'theta_CH'),
    ('*', 'r[42]', 'r[42]', 'theta_H'),
    ('*', 'temp', 'k_b[42]', 'theta_CH2'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[42]', 'r[42]', 'temp'),
    #r[43] = k_f[43]*theta_CH2*theta_H   - k_b[43]*theta_CH3*free;
    ('*', 'r[43]', 'k_f[43]', 'theta_CH2'),
    ('*', 'r[43]', 'r[43]', 'theta_H'),
    ('*', 'temp', 'k_b[43]', 'theta_CH3'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[43]', 'r[43]', 'temp'),
    #r[44] = k_f[44]*theta_CH3*theta_H   - k_b[44]*theta_CH4*free;
    ('*', 'r[44]', 'k_f[44]', 'theta_CH3'),
    ('*', 'r[44]', 'r[44]', 'theta_H'),
    ('*', 'temp', 'k_b[44]', 'theta_CH4'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[44]', 'r[44]', 'temp'),
    #r[45] = k_f[45]*theta_OH*theta_H    - k_b[45]*theta_H2O*free;
    ('*', 'r[45]', 'k_f[45]', 'theta_OH'),
    ('*', 'r[45]', 'r[45]', 'theta_H'),
    ('*', 'temp', 'k_b[45]', 'theta_H2O'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[45]', 'r[45]', 'temp'),
    #r[46] = k_f[46]*theta_CHO*theta_H   - k_b[46]*theta_CH2O*free;
    ('*', 'r[46]', 'k_f[46]', 'theta_CHO'),
    ('*', 'r[46]', 'r[46]', 'theta_H'),
    ('*', 'temp', 'k_b[46]', 'theta_CH2O'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[46]', 'r[46]', 'temp'),
    #r[47] = k_f[47]*theta_CH2O*theta_H  - k_b[47]*theta_CH3O*free*free;
    ('*', 'r[47]', 'k_f[47]', 'theta_CH2O'),
    ('*', 'r[47]', 'r[47]', 'theta_H'),
    ('*', 'temp', 'k_b[47]', 'theta_CH3O'),
    ('*', 'temp', 'temp', 'free'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[47]', 'r[47]', 'temp'),
    #r[48] = k_f[48]*theta_S - k_b[48]*p_S*free*free*free*free; //phenol   desorption
    ('*', 'r[48]', 'k_f[48]', 'theta_S'),
    ('*', 'temp', 'k_b[48]', 'p_S'),
    ('*', 'temp', 'temp', 'free'),
    ('*', 'temp', 'temp', 'free'),
    ('*', 'temp', 'temp', 'free'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[48]', 'r[48]', 'temp'),
    #r[49] = k_f[49]*theta_M - k_b[49]*p_M*free*free*free*free; //catechol desorption
    ('*', 'r[49]', 'k_f[49]', 'theta_M'),
    ('*', 'temp', 'k_b[49]', 'p_M'),
    ('*', 'temp', 'temp', 'free'),
    ('*', 'temp', 'temp', 'free'),
    ('*', 'temp', 'temp', 'free'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[49]', 'r[49]', 'temp'),
    #r[50] = k_f[50]*theta_X - k_b[50]*p_X*free*free*free;      //benzene  desorption
    ('*', 'r[50]', 'k_f[50]', 'theta_X'),
    ('*', 'temp', 'k_b[50]', 'p_X'),
    ('*', 'temp', 'temp', 'free'),
    ('*', 'temp', 'temp', 'free'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[50]', 'r[50]', 'temp'),
    #r[51] = k_f[51]*theta_CH3OH - k_b[51]*p_CH3OH*free; //CH3OH desorption
    ('*', 'r[51]', 'k_f[51]', 'theta_CH3OH'),
    ('*', 'temp', 'k_b[51]', 'p_CH3OH'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[51]', 'r[51]', 'temp'),
    #r[52] = k_f[52]*theta_CH4 - k_b[52]*p_CH4*free;   //CH4   desorption
    ('*', 'r[52]', 'k_f[52]', 'theta_CH4'),
    ('*', 'temp', 'k_b[52]', 'p_CH4'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[52]', 'r[52]', 'temp'),
    #r[53] = k_f[53]*theta_H2O - k_b[53]*p_H2O*free;   //H2O   desorption
    ('*', 'r[53]', 'k_f[53]', 'theta_H2O'),
    ('*', 'temp', 'k_b[53]', 'p_H2O'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[53]', 'r[53]', 'temp'),
    #r[54] = k_f[54]*theta_K - k_b[54]*p_K*free*free*free*free; //anisole  desorption
    ('*', 'r[54]', 'k_f[54]', 'theta_K'),
    ('*', 'temp', 'k_b[54]', 'p_K'),
    ('*', 'temp', 'temp', 'free'),
    ('*', 'temp', 'temp', 'free'),
    ('*', 'temp', 'temp', 'free'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[54]', 'r[54]', 'temp'),
    #//not using r[55] through r[74]?!
    #//also, consider making below assignments in-order (might help optimizer).
    ('//', 'not using r[55] through r[74]?!'),
    ('//', 'also, consider making below assignments in-order (might help optimizer).'),
    #r[71] = k_f[71]*theta_O*free - k_b[71]*theta_Z*theta_H;
    ('*', 'r[71]', 'k_f[71]', 'theta_O'),
    ('*', 'r[71]', 'r[71]', 'free'),
    ('*', 'temp', 'k_b[71]', 'theta_Z'),
    ('*', 'temp', 'temp', 'theta_H'),
    ('-', 'r[71]', 'r[71]', 'temp'),
    #r[72] = k_f[72]*theta_Z*free - k_b[72]*theta_U*theta_CH;
    ('*', 'r[72]', 'k_f[72]', 'theta_Z'),
    ('*', 'r[72]', 'r[72]', 'free'),
    ('*', 'temp', 'k_b[72]', 'theta_U'),
    ('*', 'temp', 'temp', 'theta_CH'),
    ('-', 'r[72]', 'r[72]', 'temp'),
    #r[73] = k_f[73]*theta_Z*free - k_b[73]*theta_Z1*theta_H;
    ('*', 'r[73]', 'k_f[73]', 'theta_Z'),
    ('*', 'r[73]', 'r[73]', 'free'),
    ('*', 'temp', 'k_b[73]', 'theta_Z1'),
    ('*', 'temp', 'temp', 'theta_H'),
    ('-', 'r[73]', 'r[73]', 'temp'),
    #r[74] = k_f[74]*theta_Z1 - k_b[74]*theta_N*theta_CO;
    ('*', 'r[74]', 'k_f[74]', 'theta_Z1'),
    ('*', 'temp', 'k_b[74]', 'theta_N'),
    ('*', 'temp', 'temp', 'theta_CO'),
    ('-', 'r[74]', 'r[74]', 'temp'),
    #r[75] = k_f[75]*theta_G*theta_H - k_b[75]*theta_Y*free;
    ('*', 'r[75]', 'k_f[75]', 'theta_G'),
    ('*', 'r[75]', 'r[75]', 'theta_H'),
    ('*', 'temp', 'k_b[75]', 'theta_Y'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[75]', 'r[75]', 'temp'),
    #r[76] = k_f[76]*theta_Y*free - k_b[76]*theta_R*theta_OH;
    ('*', 'r[76]', 'k_f[76]', 'theta_Y'),
    ('*', 'r[76]', 'r[76]', 'free'),
    ('*', 'temp', 'k_b[76]', 'theta_R'),
    ('*', 'temp', 'temp', 'theta_OH'),
    ('-', 'r[76]', 'r[76]', 'temp'),
    #r[77] = k_f[77]*theta_CO*theta_H - k_b[77]*theta_CHO;
    ('*', 'r[77]', 'k_f[77]', 'theta_CO'),
    ('*', 'r[77]', 'r[77]', 'theta_H'),
    ('*', 'temp', 'k_b[77]', 'theta_CHO'),
    ('-', 'r[77]', 'r[77]', 'temp'),
    #blank line for separation
    ('//', ''),
    #// steps including C, D, K, Q.
    ('//',' steps including C, D, K, Q.'),
    #r[2] = k_f[2]*theta_A*theta_H - k_b[2] *theta_C*free;
    ('*', 'r[2]', 'k_f[2]', 'theta_A'),
    ('*', 'r[2]', 'r[2]', 'theta_H'),
    ('*', 'temp', 'k_b[2]', 'theta_C'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[2]', 'r[2]', 'temp'),
    #r[3] = k_f[3] *theta_A*free - k_b[3] *theta_D*theta_OH;
    ('*', 'r[3]', 'k_f[3]', 'theta_A'),
    ('*', 'r[3]', 'r[3]', 'free'),
    ('*', 'temp', 'k_b[3]', 'theta_D'),
    ('*', 'temp', 'temp', 'theta_OH'),
    ('-', 'r[3]', 'r[3]', 'temp'),
    #r[9] = k_f[9] *theta_C*free - k_b[9] *theta_K*theta_OH;
    ('*', 'r[9]', 'k_f[9]', 'theta_C'),
    ('*', 'r[9]', 'r[9]', 'free'),
    ('*', 'temp', 'k_b[9]', 'theta_K'),
    ('*', 'temp', 'temp', 'theta_OH'),
    ('-', 'r[9]', 'r[9]', 'temp'),
    #r[10] = k_f[10]*theta_D*theta_H - k_b[10]*theta_K*free;
    ('*', 'r[10]', 'k_f[10]', 'theta_D'),
    ('*', 'r[10]', 'r[10]', 'theta_H'),
    ('*', 'temp', 'k_b[10]', 'theta_K'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'r[10]', 'r[10]', 'temp'),
    #r[20] = k_f[20]*theta_K*free - k_b[20]*theta_Q*theta_H;
    ('*', 'r[20]', 'k_f[20]', 'theta_K'),
    ('*', 'r[20]', 'r[20]', 'free'),
    ('*', 'temp', 'k_b[20]', 'theta_Q'),
    ('*', 'temp', 'temp', 'theta_H'),
    ('-', 'r[20]', 'r[20]', 'temp'),
    #r[29] = k_f[29]*theta_Q*free - k_b[29]*theta_R*theta_CH2;
    ('*', 'r[29]', 'k_f[29]', 'theta_Q'),
    ('*', 'r[29]', 'r[29]', 'free'),
    ('*', 'temp', 'k_b[29]', 'theta_R'),
    ('*', 'temp', 'temp', 'theta_CH2'),
    ('-', 'r[29]', 'r[29]', 'temp')
]

steady_state_approx = [
    ('//', ' apply the steady state approximation for all thetas.'),
    #out[0]  = r_04 + r_12 + r_21 + r_23 - r_11;     // d(theta_E)/dt=0
    ('+', 'out[0]', 'r[4]', 'r[12]'),
    ('+', 'out[0]', 'out[0]', 'r[21]'),
    ('+', 'out[0]', 'out[0]', 'r[23]'),
    ('-', 'out[0]', 'out[0]', 'r[11]'),
    #out[1]  = r_05 - r_12 - r_13 - r_14 - r_37;     // d(theta_F)/dt=0
    ('-', 'out[1]', 'r[5]', 'r[12]'),
    ('-', 'out[1]', 'out[1]', 'r[13]'),
    ('-', 'out[1]', 'out[1]', 'r[14]'),
    ('-', 'out[1]', 'out[1]', 'r[37]'),
    #out[2]  = r_06 + r_14 + r_22 + r_34 - r_15 - r_16 - r_75; // d(theta_G)/dt=0
    ('+', 'out[2]', 'r[6]', 'r[14]'),
    ('+', 'out[2]', 'out[2]', 'r[22]'),
    ('+', 'out[2]', 'out[2]', 'r[34]'),
    ('-', 'out[2]', 'out[2]', 'r[15]'),
    ('-', 'out[2]', 'out[2]', 'r[16]'),
    ('-', 'out[2]', 'out[2]', 'r[75]'),
    #out[3]  = r_07 - r_17 - r_18 - r_39;            // d(theta_I)/dt=0
    ('-', 'out[3]', 'r[7]', 'r[17]'),
    ('-', 'out[3]', 'out[3]', 'r[18]'),
    ('-', 'out[3]', 'out[3]', 'r[39]'),
    #out[4]  = r_13 - r_21 - r_22;                   // d(theta_L)/dt=0
    ('-', 'out[4]', 'r[13]', 'r[21]'),
    ('-', 'out[4]', 'out[4]', 'r[22]'),
    #out[5]  = r_15 - r_23 - r_24 - r_49;            // d(theta_M)/dt=0 catechol
    ('-', 'out[5]', 'r[15]', 'r[23]'),
    ('-', 'out[5]', 'out[5]', 'r[24]'),
    ('-', 'out[5]', 'out[5]', 'r[49]'),
    #out[6]  = r_16 + r_17 + r_26 + r_74 - r_25;     // d(theta_N)/dt=0
    ('+', 'out[6]', 'r[16]', 'r[17]'),
    ('+', 'out[6]', 'out[6]', 'r[26]'),
    ('+', 'out[6]', 'out[6]', 'r[74]'),
    ('-', 'out[6]', 'out[6]', 'r[25]'),
    #out[7]  = r_18 + r_37 - r_26 - r_27 - r_71;     // d(theta_O)/dt=0
    ('+', 'out[7]', 'r[18]', 'r[37]'),
    ('-', 'out[7]', 'out[7]', 'r[26]'),
    ('-', 'out[7]', 'out[7]', 'r[27]'),
    ('-', 'out[7]', 'out[7]', 'r[71]'),
    #out[8]  = r_25 + r_29 + r_76 - r_30;            // d(theta_R)/dt=0
    ('+', 'out[8]', 'r[25]', 'r[29]'),
    ('+', 'out[8]', 'out[8]', 'r[76]'),
    ('-', 'out[8]', 'out[8]', 'r[30]'),
    #out[9] = r_11 + r_30 + r_33 + r_40 - r_31 - r_32 - r_48; // d(theta_S)/dt=0 phenol
    ('+', 'out[9]', 'r[11]', 'r[30]'),
    ('+', 'out[9]', 'out[9]', 'r[33]'),
    ('+', 'out[9]', 'out[9]', 'r[40]'),
    ('-', 'out[9]', 'out[9]', 'r[31]'),
    ('-', 'out[9]', 'out[9]', 'r[32]'),
    ('-', 'out[9]', 'out[9]', 'r[48]'),
    #out[10] = r_27 + r_39 + r_72 - r_34;            // d(theta_U)/dt=0
    ('+', 'out[10]', 'r[27]', 'r[39]'),
    ('+', 'out[10]', 'out[10]', 'r[72]'),
    ('-', 'out[10]', 'out[10]', 'r[34]'),
    #out[11] = r_31 - r_35;                          // d(theta_V)/dt=0
    ('+', 'out[11]', 'r[31]', 'r[35]'),
    #out[12] = r_35 + r_36 - r_50;                   // d(theta_X)/dt=0 benzene
    ('+', 'out[12]', 'r[35]', 'r[36]'),
    ('+', 'out[12]', 'out[12]', 'r[50]'),
    #blank line
    ('//', ''),
    #out[13] = r_03 + r_09 + r_23 + r_31 + r_31 + r_33 - r_45; // d(theta_OH)/dt=0
    ('+', 'out[13]', 'r[3]', 'r[9]'),
    ('+', 'out[13]', 'out[13]', 'r[23]'),
    ('+', 'out[13]', 'out[13]', 'r[31]'), #did you mean to add this twice?
    ('+', 'out[13]', 'out[13]', 'r[31]'),
    ('+', 'out[13]', 'out[13]', 'r[33]'),
    ('-', 'out[13]', 'out[13]', 'r[45]'),
    #out[14] = r_45 - r_53;                          // d(theta_H2O)/dt=0
    ('+', 'out[14]', 'out[45]', 'r[53]'),
    #out[15] = r_22 + r_72 - r_42;                   // d(theta_CH)/dt =0
    ('+', 'out[15]', 'r[22]', 'r[72]'),
    ('-', 'out[15]', 'out[15]', 'r[42]'),
    #out[16] = r_14 + r_19 + r_27 + r_29 + r_42 - r_43; // d(theta_CH2)/dt=0
    ('+', 'out[16]', 'r[14]', 'r[19]'),
    ('+', 'out[16]', 'out[16]', 'r[27]'),
    ('+', 'out[16]', 'out[16]', 'r[29]'),
    ('+', 'out[16]', 'out[16]', 'r[42]'),
    ('-', 'out[16]', 'out[16]', 'r[43]'),
    #out[17] = r_06 + r_43 - r_44;                   // d(theta_CH3)/dt=0
    ('+', 'out[17]', 'r[6]', 'r[43]'),
    ('-', 'out[17]', 'out[17]', 'r[44]'),
    #out[18] = r_44 - r_52;                          // d(theta_CH4)/dt=0
    ('-', 'out[16]', 'r[44]', 'r[52]'),
    #out[19] = r_21 + r_77 - r_46;                   // d(theta_CHO)/dt=0
    ('+', 'out[19]', 'r[21]', 'r[77]'),
    ('-', 'out[19]', 'out[16]', 'r[46]'),
    #out[20] = r_12 + r_26 + r_46 - r_47;            // d(theta_CH2O)/dt=0
    ('+', 'out[20]', 'r[12]', 'r[26]'),
    ('+', 'out[20]', 'out[20]', 'r[46]'),
    ('-', 'out[20]', 'out[20]', 'r[47]'),
    #out[21] = r_04 + r_17 + r_47 - r_41;            // d(theta_CH3O)/dt=0
    ('+', 'out[21]', 'r[4]', 'r[17]'),
    ('+', 'out[21]', 'out[21]', 'r[47]'),
    ('-', 'out[21]', 'out[21]', 'r[41]'),
    #out[22] = r_41 - r_51;                          // d(theta_CH3OH)/dt=0
    ('-', 'out[22]', 'r[41]', 'r[51]'),
    #out[23] = r_00 - r_01 - r_04 - r_05 - r_06 - r_07; // d(theta_A)/dt=0
    ('-', 'out[23]', 'r[0]', 'r[1]'),
    ('-', 'out[23]', 'out[23]', 'r[4]'),
    ('-', 'out[23]', 'out[23]', 'r[5]'),
    ('-', 'out[23]', 'out[23]', 'r[6]'),
    ('-', 'out[23]', 'out[23]', 'r[7]'),
    #//    out[23] = theta_A - k_00_f/k_00_b*p_A*free*free*free*free; // d(theta_A)/dt=0 if step 0 is in equilibrium.
    ('//', '    out[23] = theta_A - k_00_f/k_00_b*p_A*free*free*free*free; // d(theta_A)/dt=0 if step 0 is in equilibrium.'),
    #out[24] = r_32 - r_36;                          // d(theta_W)/dt=0
    ('-', 'out[24]', 'r[32]', 'r[36]'),
    #out[25] = r_24 + r_28 - r_33;                   // d(theta_T)/dt=0
    ('+', 'out[24]', 'r[24]', 'r[28]'),
    ('-', 'out[24]', 'out[25]', 'r[33]'),
    #out[26] = r_01 - r_08 - r_40;                   // d(theta_B)/dt=0
    ('-', 'out[26]', 'r[1]', 'r[8]'),
    ('-', 'out[26]', 'out[26]', 'r[40]'),
    #out[27] = r_08 - r_19;                          // d(theta_J)/dt=0
    ('-', 'out[27]', 'r[8]', 'r[19]'),
    #out[28] = r_19 - r_28;                          // d(theta_P)/dt=0
    ('-', 'out[28]', 'r[19]', 'r[28]'),
    #out[29] = theta_H - exp(-( (-1.374+0.076+0.683)/2 + 2*0.084*(theta_H-0.139))/KB/T)*pow(p_H2,0.5)*free; //theta_H
    #                     e^(-((-0.615 / 2 = -0.3075) + (0.168)*(theta_H-0.139)) /KB/T) *pow(p_H2,0.5)*free;
    #since this expression is such a pain, we'll use out[29] as temp storage.
    ('=d', 'temp', '0.139'),
    ('-', 'out[29]', 'theta_H', 'temp'),
    ('=d', 'temp', '0.168'),
    ('*', 'out[29]', 'out[29]', 'temp'),
    ('=d', 'temp', '-0.3075'),
    ('+', 'out[29]', 'out[29]', 'temp'),
    ('neg', 'out[29]', 'out[29]'), #-((-0.3075) + (0.168)*(theta_H-0.139)) taken care of...
    ('/', 'out[29]', 'out[29]', 'KB'),
    ('/', 'out[29]', 'out[29]', 'T'),
    ('custom', 'exponent = mpf_get_ui(out[29]);'),
    ('//', 'expect to see some truncation here...'),
    ('pow', 'out[29]', 'e', 'exponent'), #e^(-((-0.3075) + (0.168)*(theta_H-0.139))/KB/T) taken care of...
    ('sqrt', 'temp', 'p_H2'),
    ('*', 'temp', 'temp', 'free'),
    ('*', 'temp', 'out[29]', 'temp'), #e^(-((-0.3075) + (0.168)*(theta_H-0.139))/KB/T)*pow(p_H2,0.5)*free taken care of...
    ('=', 'out[29]', 'theta_H'),
    ('-', 'out[29]', 'out[29]', 'temp'), #entire source expression taken care of!
    #out[30] = r_02 - r_09;                          // d(theta_C)/dt=0
    ('-', 'out[30]', 'r[2]', 'r[9]'),
    #out[31] = r_03 - r_10;                          // d(theta_D)/dt=0
    ('-', 'out[31]', 'r[3]', 'r[10]'),
    #out[32] = r_09 + r_10 - r_20 - r_54;            // d(theta_K)/dt=0
    ('+', 'out[32]', 'r[9]', 'r[10]'),
    ('-', 'out[32]', 'out[32]', 'r[20]'),
    ('-', 'out[32]', 'out[32]', 'r[54]'),
    #out[33] = r_20 - r_29;                          // d(theta_Q)/dt=0
    ('-', 'out[33]', 'r[20]', 'r[29]'),
    #out[34] = r_75 - r_76;                          // d(theta_Y)/dt=0
    ('-', 'out[34]', 'r[75]', 'r[76]'),
    #out[35] = r_71 - r_72 - r_73;                   // d(theta_Z)/dt=0
    ('-', 'out[35]', 'r[71]', 'r[72]'),
    ('-', 'out[35]', 'out[35]', 'r[73]'),
    #out[36] = r_73 - r_74;                          // d(theta_Z1)/dt=0
    ('-', 'out[36]', 'r[73]', 'r[74]'),
    #out[37] = theta_CO - exp(-(-2.131+0.028+1.764)/KB/T)*p_CO*free; // d(theta_CO)/dt=0*/
    ('=d', 'out[37]', 'theta_C0'),
    ('=d', 'temp', '-0.339'),
    ('/', 'temp', 'temp', 'KB'),
    ('/', 'temp', 'temp', 'T'),
    ('neg', 'temp', 'temp'),
    ('custom', 'exponent = mpf_get_ui(temp);'),
    ('//', 'expect to see some truncation here...'),
    ('pow', 'temp', 'e', 'exponent'),
    ('*', 'temp', 'temp', 'p_CO'),
    ('*', 'temp', 'temp', 'free'),
    ('-', 'out[37]', 'out[37]', 'temp'),
]


def assemble(bytelist):
    final = ""
    for item in bytelist:
        if item[0] == "=":
            final += "mpf_set(" + '{:>10}'.format(item[1]) + ", " + '{:>10}'.format(item[2]) + ");"
        elif item[0] == "=d":
            final += "mpf_set_d(" + '{:>10}'.format(item[1]) + ", " + '{:>10}'.format(item[2]) + ");"
        elif item[0] == "+":
            final += "mpf_add(" + '{:>10}'.format(item[1]) + ", " + '{:>10}'.format(item[2]) + ", " + '{:>10}'.format(item[3]) + ");"
        elif item[0] == "-":
            final += "mpf_sub(" + '{:>10}'.format(item[1]) + ", " + '{:>10}'.format(item[2]) + ", " + '{:>10}'.format(item[3]) + ");"
        elif item[0] == "*":
            final += "mpf_mul(" + '{:>10}'.format(item[1]) + ", " + '{:>10}'.format(item[2]) + ", " + '{:>10}'.format(item[3]) + ");"
        elif item[0] == "/":
            final += "mpf_sub(" + '{:>10}'.format(item[1]) + ", " + '{:>10}'.format(item[2]) + ", " + '{:>10}'.format(item[3]) + ");"
        elif item[0] == "pow":
            final += "mpf_pow_ui(" + '{:>10}'.format(item[1]) + ", " + '{:>10}'.format(item[2]) + ", " + '{:>10}'.format(item[3]) + ");"
        elif item[0] == "neg":
            final += "mpf_neg(" + '{:>10}'.format(item[1]) + ", " + '{:>10}'.format(item[2]) + ");"
        elif item[0] == "abs":
            final += "mpf_abs(" + '{:>10}'.format(item[1]) + ", " + '{:>10}'.format(item[2]) + ");"
        elif item[0] == "sqrt":
            final += "mpf_sqrt(" + '{:>10}'.format(item[1]) + ", " + '{:>10}'.format(item[2]) + ");"
        elif item[0] == "//":
            final += "//" + item[1]
        elif item[0] == "custom":
            final += item[1]
        else:
            pass
        #on each pass:
        final += "\n"
    return final


#main:
if __name__ == '__main__':
    #src = sys.argv[1]
    #bytelist = literal_eval(src)
    #bytelist = list(bytelist)
    src = [rate_calc, steady_state_approx]
    result = map(assemble, src)
    for item in result: print item