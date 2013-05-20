# Name: gmpgen.py -- helper script for making long GNU MP programs.
# Author: Philip Conrad on 4/30/2013 @ 2:35 PM
# License: MIT-License

import sys
from ast import literal_eval


#forward reaction rates of the sub-reactions:
r_f = [
    #// calculate rates for all elementary steps.
    ('//', ' calculate rates for all elementary steps.'),
    #r_f[0] = k_f[0]*p_A*free*free*free*free
    ('*', 'r_f[0]', 'k_f[0]', 'p_A'),
    ('*', 'r_f[0]', 'r_f[0]', 'free'),
    ('*', 'r_f[0]', 'r_f[0]', 'free'),
    ('*', 'r_f[0]', 'r_f[0]', 'free'),
    ('*', 'r_f[0]', 'r_f[0]', 'free'),
    #r_f[1] = k_f[1]*theta_A*theta_H
    ('*', 'r_f[1]', 'k_f[1]', 'theta_A'),
    ('*', 'r_f[1]', 'r_f[1]', 'theta_H'),
    #//r_f[2] and r_f[3] handled later on...
    ('//', 'r_f[2] and r_f[3] handled later on...'),
    #r_f[4] = k_f[4]*theta_A*free
    ('*', 'r_f[4]', 'k_f[4]', 'theta_A'),
    ('*', 'r_f[4]', 'r_f[4]', 'free'),
    #r_f[5] = k_f[5]*theta_A*free
    ('*', 'r_f[5]', 'k_f[5]', 'theta_A'),
    ('*', 'r_f[5]', 'r_f[5]', 'free'),
    #r_f[6] = k_f[6]*theta_A*free
    ('*', 'r_f[6]', 'k_f[6]', 'theta_A'),
    ('*', 'r_f[6]', 'r_f[6]', 'free'),
    #r_f[7] = k_f[7]*theta_A*free
    ('*', 'r_f[7]', 'k_f[7]', 'theta_A'),
    ('*', 'r_f[7]', 'r_f[7]', 'free'),
    #r_f[8] = k_f[8]*theta_B*free*free
    ('*', 'r_f[8]', 'k_f[8]', 'theta_B'),
    ('*', 'r_f[8]', 'r_f[8]', 'free'),
    ('*', 'r_f[8]', 'r_f[8]', 'free'),
    #//r_f[9] and r_f[10] handled later on...
    ('//', 'r_f[9] and r_f[10] handled later on...'),
    #r_f[11] = k_f[11]*theta_E*theta_H
    ('*', 'r_f[11]', 'k_f[11]', 'theta_E'),
    ('*', 'r_f[11]', 'r_f[11]', 'theta_H'),
    #r_f[12] = k_f[12]*theta_F*free
    ('*', 'r_f[12]', 'k_f[12]', 'theta_F'),
    ('*', 'r_f[12]', 'r_f[12]', 'free'),
    #r_f[13] = k_f[13]*theta_F*free
    ('*', 'r_f[13]', 'k_f[13]', 'theta_F'),
    ('*', 'r_f[13]', 'r_f[13]', 'free'),
    #r_f[14] = k_f[14]*theta_F
    ('*', 'r_f[14]', 'k_f[14]', 'theta_F'),
    #r_f[15] = k_f[15]*theta_G*theta_H
    ('*', 'r_f[15]', 'k_f[15]', 'theta_G'),
    ('*', 'r_f[15]', 'r_f[15]', 'theta_H'),
    #r_f[16] = k_f[16]*theta_G*free
    ('*', 'r_f[16]', 'k_f[16]', 'theta_G'),
    ('*', 'r_f[16]', 'r_f[16]', 'free'),
    #r_f[17] = k_f[17]*theta_I*free
    ('*', 'r_f[17]', 'k_f[17]', 'theta_I'),
    ('*', 'r_f[17]', 'r_f[17]', 'free'),
    #r_f[18] = k_f[18]*theta_I*free*free
    ('*', 'r_f[18]', 'k_f[18]', 'theta_I'),
    ('*', 'r_f[18]', 'r_f[18]', 'free'),
    ('*', 'r_f[18]', 'r_f[18]', 'free'),
    #r_f[19] = k_f[19]*theta_J
    ('*', 'r_f[19]', 'k_f[19]', 'theta_J'),
    #//r_f[20] handled later on...
    ('//', 'r_f[20] handled later on...'),
    #r_f[21] = k_f[21]*theta_L*free
    ('*', 'r_f[21]', 'k_f[21]', 'theta_L'),
    ('*', 'r_f[21]', 'r_f[21]', 'free'),
    #r_f[22] = k_f[22]*theta_L*free
    ('*', 'r_f[22]', 'k_f[22]', 'theta_L'),
    ('*', 'r_f[22]', 'r_f[22]', 'free'),
    #r_f[23] = k_f[23]*theta_M*free
    ('*', 'r_f[23]', 'k_f[23]', 'theta_M'),
    ('*', 'r_f[23]', 'r_f[23]', 'free'),
    #r_f[24] = k_f[24]*theta_M*theta_H
    ('*', 'r_f[24]', 'k_f[24]', 'theta_M'),
    ('*', 'r_f[24]', 'r_f[24]', 'theta_H'),
    #r_f[25] = k_f[25]*theta_N*theta_H
    ('*', 'r_f[25]', 'k_f[25]', 'theta_N'),
    ('*', 'r_f[25]', 'r_f[25]', 'theta_H'),
    #r_f[26] = k_f[26]*theta_O*free
    ('*', 'r_f[26]', 'k_f[26]', 'theta_O'),
    ('*', 'r_f[26]', 'r_f[26]', 'free'),
    #r_f[27] = k_f[27]*theta_O*free
    ('*', 'r_f[27]', 'k_f[27]', 'theta_O'),
    ('*', 'r_f[27]', 'r_f[27]', 'free'),
    #r_f[28] = k_f[28]*theta_P*theta_H
    ('*', 'r_f[28]', 'k_f[28]', 'theta_P'),
    ('*', 'r_f[28]', 'r_f[28]', 'theta_H'),
    #//r_f[29] handled later on...
    ('//', 'r[29] handled later on...'),
    #r_f[30] = k_f[30]*theta_R*theta_H
    ('*', 'r_f[30]', 'k_f[30]', 'theta_R'),
    ('*', 'r_f[30]', 'r_f[30]', 'theta_H'),
    #r_f[31] = k_f[31]*theta_S*free
    ('*', 'r_f[31]', 'k_f[31]', 'theta_S'),
    ('*', 'r_f[31]', 'r_f[31]', 'free'),
    #r_f[32] = k_f[32]*theta_S*theta_H
    ('*', 'r_f[32]', 'k_f[32]', 'theta_S'),
    ('*', 'r_f[32]', 'r_f[32]', 'theta_H'),
    #r_f[33] = k_f[33]*theta_T*free
    ('*', 'r_f[33]', 'k_f[33]', 'theta_T'),
    ('*', 'r_f[33]', 'r_f[33]', 'free'),
    #r_f[34] = k_f[34]*theta_U*theta_H
    ('*', 'r_f[34]', 'k_f[34]', 'theta_U'),
    ('*', 'r_f[34]', 'r_f[34]', 'theta_H'),
    #r_f[35] = k_f[35]*theta_V*theta_H
    ('*', 'r_f[35]', 'k_f[35]', 'theta_V'),
    ('*', 'r_f[35]', 'r_f[35]', 'theta_H'),
    #r_f[36] = k_f[36]*theta_W
    ('*', 'r_f[36]', 'k_f[36]', 'theta_W'),
    #r_f[37] = k_f[37]*theta_F*free
    ('*', 'r_f[37]', 'k_f[37]', 'theta_F'),
    ('*', 'r_f[37]', 'r_f[37]', 'free'),
    #//what happened to r_38?!
    ('//', 'what happened to r_38?!'),
    #r_f[39] = k_f[39]*theta_I*free*free
    ('*', 'r_f[39]', 'k_f[39]', 'theta_I'),
    ('*', 'r_f[39]', 'r_f[39]', 'free'),
    ('*', 'r_f[39]', 'r_f[39]', 'free'),
    #r_f[40] = k_f[40]*theta_B*free*free
    ('*', 'r_f[40]', 'k_f[40]', 'theta_B'),
    ('*', 'r_f[40]', 'r_f[40]', 'free'),
    ('*', 'r_f[40]', 'r_f[40]', 'free'),
    #r_f[41] = k_f[41]*theta_CH3O*theta_H
    ('*', 'r_f[41]', 'k_f[41]', 'theta_CH3O'),
    ('*', 'r_f[41]', 'r_f[41]', 'theta_H'),
    #r_f[42] = k_f[42]*theta_CH*theta_H
    ('*', 'r_f[42]', 'k_f[42]', 'theta_CH'),
    ('*', 'r_f[42]', 'r_f[42]', 'theta_H'),
    #r_f[43] = k_f[43]*theta_CH2*theta_H
    ('*', 'r_f[43]', 'k_f[43]', 'theta_CH2'),
    ('*', 'r_f[43]', 'r_f[43]', 'theta_H'),
    #r_f[44] = k_f[44]*theta_CH3*theta_H
    ('*', 'r_f[44]', 'k_f[44]', 'theta_CH3'),
    ('*', 'r_f[44]', 'r_f[44]', 'theta_H'),
    #r_f[45] = k_f[45]*theta_OH*theta_H
    ('*', 'r_f[45]', 'k_f[45]', 'theta_OH'),
    ('*', 'r_f[45]', 'r_f[45]', 'theta_H'),
    #r_f[46] = k_f[46]*theta_CHO*theta_H
    ('*', 'r_f[46]', 'k_f[46]', 'theta_CHO'),
    ('*', 'r_f[46]', 'r_f[46]', 'theta_H'),
    #r_f[47] = k_f[47]*theta_CH2O*theta_H
    ('*', 'r_f[47]', 'k_f[47]', 'theta_CH2O'),
    ('*', 'r_f[47]', 'r_f[47]', 'theta_H'),
    #r_f[48] = k_f[48]*theta_S //phenol   desorption
    ('*', 'r_f[48]', 'k_f[48]', 'theta_S'),
    #r_f[49] = k_f[49]*theta_M //catechol desorption
    ('*', 'r_f[49]', 'k_f[49]', 'theta_M'),
    #r_f[50] = k_f[50]*theta_X      //benzene  desorption
    ('*', 'r_f[50]', 'k_f[50]', 'theta_X'),
    #r_f[51] = k_f[51]*theta_CH3OH //CH3OH desorption
    ('*', 'r_f[51]', 'k_f[51]', 'theta_CH3OH'),
    #r_f[52] = k_f[52]*theta_CH4   //CH4   desorption
    ('*', 'r_f[52]', 'k_f[52]', 'theta_CH4'),
    #r_f[53] = k_f[53]*theta_H2O   //H2O   desorption
    ('*', 'r_f[53]', 'k_f[53]', 'theta_H2O'),
    #r_f[54] = k_f[54]*theta_K //anisole  desorption
    ('*', 'r_f[54]', 'k_f[54]', 'theta_K'),
    #//not using r_f[55] through r_f[74]?!
    #//also, consider making below assignments in-order (might help optimizer).
    ('//', 'not using r_f[55] through r_f[74]?!'),
    ('//', 'also, consider making below assignments in-order (might help optimizer).'),
    #r_f[71] = k_f[71]*theta_O*free
    ('*', 'r_f[71]', 'k_f[71]', 'theta_O'),
    ('*', 'r_f[71]', 'r_f[71]', 'free'),
    #r_f[72] = k_f[72]*theta_Z*free
    ('*', 'r_f[72]', 'k_f[72]', 'theta_Z'),
    ('*', 'r_f[72]', 'r_f[72]', 'free'),
    #r_f[73] = k_f[73]*theta_Z*free
    ('*', 'r_f[73]', 'k_f[73]', 'theta_Z'),
    ('*', 'r_f[73]', 'r_f[73]', 'free'),
    #r_f[74] = k_f[74]*theta_Z1
    ('*', 'r_f[74]', 'k_f[74]', 'theta_Z1'),
    #r_f[75] = k_f[75]*theta_G*theta_H
    ('*', 'r_f[75]', 'k_f[75]', 'theta_G'),
    ('*', 'r_f[75]', 'r_f[75]', 'theta_H'),
    #r_f[76] = k_f[76]*theta_Y*free
    ('*', 'r_f[76]', 'k_f[76]', 'theta_Y'),
    ('*', 'r_f[76]', 'r_f[76]', 'free'),
    #r_f[77] = k_f[77]*theta_CO*theta_H
    ('*', 'r_f[77]', 'k_f[77]', 'theta_CO'),
    ('*', 'r_f[77]', 'r_f[77]', 'theta_H'),
    #blank line for separation
    ('//', ''),
    #// steps including C, D, K, Q.
    ('//',' steps including C, D, K, Q.'),
    #r_f[2] = k_f[2]*theta_A*theta_H
    ('*', 'r_f[2]', 'k_f[2]', 'theta_A'),
    ('*', 'r_f[2]', 'r_f[2]', 'theta_H'),
    #r_f[3] = k_f[3] *theta_A*free
    ('*', 'r_f[3]', 'k_f[3]', 'theta_A'),
    ('*', 'r_f[3]', 'r_f[3]', 'free'),
    #r_f[9] = k_f[9] *theta_C*free
    ('*', 'r_f[9]', 'k_f[9]', 'theta_C'),
    ('*', 'r_f[9]', 'r_f[9]', 'free'),
    #r_f[10] = k_f[10]*theta_D*theta_H
    ('*', 'r_f[10]', 'k_f[10]', 'theta_D'),
    ('*', 'r_f[10]', 'r_f[10]', 'theta_H'),
    #r_f[20] = k_f[20]*theta_K*free
    ('*', 'r_f[20]', 'k_f[20]', 'theta_K'),
    ('*', 'r_f[20]', 'r_f[20]', 'free'),
    #r_f[29] = k_f[29]*theta_Q*free
    ('*', 'r_f[29]', 'k_f[29]', 'theta_Q'),
    ('*', 'r_f[29]', 'r_f[29]', 'free'),
]

#reverse reaction rates of the sub-reactions:
r_b = [
    #r[0] = k_b[0]*theta_A;
    ('*', 'r_b[0]', 'k_b[0]', 'theta_A'),
    #r[1] = k_f[1]*theta_B*free;
    ('*', 'r_b[1]', 'k_b[1]', 'theta_B'),
    ('*', 'r_b[1]', 'r_b[1]', 'free'),
    #//r[2] and r[3] handled later on...
    ('//', 'r[2] and r[3] handled later on...'),
    #r[4] = k_b[4]*theta_E*theta_CH3O;
    ('*', 'r_b[4]', 'k_b[4]', 'theta_E'),
    ('*', 'r_b[4]', 'r_b[4]', 'theta_CH3O'),
    #r[5] = k_b[5]*theta_F*theta_H;
    ('*', 'r_b[5]', 'k_b[5]', 'theta_F'),
    ('*', 'r_b[5]', 'r_b[5]', 'theta_H'),
    #r[6] = k_b[6]*theta_G*theta_CH3;
    ('*', 'r_b[6]', 'k_b[6]', 'theta_G'),
    ('*', 'r_b[6]', 'r_b[6]', 'theta_CH3'),
    #r[7] = k_b[7]*theta_I*theta_H;
    ('*', 'r_b[7]', 'k_b[7]', 'theta_I'),
    ('*', 'r_b[7]', 'r_b[7]', 'theta_H'),
    #r[8] = k_b[8]*theta_J*theta_H;
    ('*', 'r_b[8]', 'k_b[8]', 'theta_J'),
    ('*', 'r_b[8]', 'r_b[8]', 'theta_H'),
    #//r[9] and r[10] handled later on...
    ('//', 'r[9] and r[10] handled later on...'),
    #r[11] = k_b[11]*theta_S*free;
    ('*', 'r_b[11]', 'k_b[11]', 'theta_S'),
    ('*', 'r_b[11]', 'r_b[11]', 'free'),
    #r[12] = k_b[12]*theta_E*theta_CH2O;
    ('*', 'r_b[12]', 'k_b[12]', 'theta_E'),
    ('*', 'r_b[12]', 'r_b[12]', 'theta_CH2O'),
    #r[13] = k_b[13]*theta_L*theta_H;
    ('*', 'r_b[13]', 'k_b[13]', 'theta_L'),
    ('*', 'r_b[13]', 'r_b[13]', 'theta_H'),
    #r[14] = k_b[14]*theta_G*theta_CH2;
    ('*', 'r_b[14]', 'k_b[14]', 'theta_G'),
    ('*', 'r_b[14]', 'r_b[14]', 'theta_CH2'),
    #r[15] = k_b[15]*theta_M*free;
    ('*', 'r_b[15]', 'k_b[15]', 'theta_M'),
    ('*', 'r_b[15]', 'r_b[15]', 'free'),
    #r[16] = k_b[16]*theta_N*theta_OH;
    ('*', 'r_b[16]', 'k_b[16]', 'theta_N'),
    ('*', 'r_b[16]', 'r_b[16]', 'theta_OH'),
    #r[17] = k_b[17]*theta_N*theta_CH3O;
    ('*', 'r_b[17]', 'k_b[17]', 'theta_N'),
    ('*', 'r_b[17]', 'r_b[17]', 'theta_CH3O'),
    #r[18] = k_b[18]*theta_O*theta_H;
    ('*', 'r_b[18]', 'k_b[18]', 'theta_O'),
    ('*', 'r_b[18]', 'r_b[18]', 'theta_H'),
    #r[19] = k_b[19]*theta_P*theta_CH2;
    ('*', 'r_b[19]', 'k_b[19]', 'theta_P'),
    ('*', 'r_b[19]', 'r_b[19]', 'theta_CH2'),
    #//r[20] handled later on...
    ('//', 'r[20] handled later on...'),
    #//r[20] handled later on...
    #r[21] = k_b[21]*theta_E*theta_CHO;
    ('*', 'r_b[21]', 'k_b[21]', 'theta_E'),
    ('*', 'r_b[21]', 'r_b[21]', 'theta_CHO'),
    #r[22] = k_b[22]*theta_G*theta_CH;
    ('*', 'r_b[22]', 'k_b[22]', 'theta_G'),
    ('*', 'r_b[22]', 'r_b[22]', 'theta_CH'),
    #r[23] = k_b[23]*theta_E*theta_OH;
    ('*', 'r_b[23]', 'k_b[23]', 'theta_E'),
    ('*', 'r_b[23]', 'r_b[23]', 'theta_OH'),
    #r[24] = k_b[24]*theta_T;
    ('*', 'r_b[24]', 'k_b[24]', 'theta_T'),
    #r[25] = k_b[25]*theta_R*free;
    ('*', 'r_b[25]', 'k_b[25]', 'theta_R'),
    ('*', 'r_b[25]', 'r_b[25]', 'free'),
    #r[26] = k_b[26]*theta_N*theta_CH2O;
    ('*', 'r_b[26]', 'k_b[26]', 'theta_N'),
    ('*', 'r_b[26]', 'r_b[26]', 'theta_CH2O'),
    #r[27] = k_b[27]*theta_U*theta_CH2;
    ('*', 'r_b[27]', 'k_b[27]', 'theta_U'),
    ('*', 'r_b[27]', 'r_b[27]', 'theta_CH2'),
    #r[28] = k_b[28]*theta_T*free;
    ('*', 'r_b[28]', 'k_b[28]', 'theta_T'),
    ('*', 'r_b[28]', 'r_b[28]', 'free'),
    #//r[29] handled later on...
    ('//', 'r[29] handled later on...'),
    #r[30] = k_b[30]*theta_S*free;
    ('*', 'r_b[30]', 'k_b[30]', 'theta_S'),
    ('*', 'r_b[30]', 'r_b[30]', 'free'),
    #r[31] = k_b[31]*theta_V*theta_OH;
    ('*', 'r_b[31]', 'k_b[31]', 'theta_V'),
    ('*', 'r_b[31]', 'r_b[31]', 'theta_OH'),
    #r[32] = k_b[32]*theta_W*free;
    ('*', 'r_b[32]', 'k_b[32]', 'theta_W'),
    ('*', 'r_b[32]', 'r_b[32]', 'free'),
    #r[33] = k_b[33]*theta_S*theta_OH;
    ('*', 'r_b[33]', 'k_b[33]', 'theta_S'),
    ('*', 'r_b[33]', 'r_b[33]', 'theta_OH'),
    #r[34] = k_b[34]*theta_G*free*free;
    ('*', 'r_b[34]', 'k_b[34]', 'theta_G'),
    ('*', 'r_b[34]', 'r_b[34]', 'free'),
    ('*', 'r_b[34]', 'r_b[34]', 'free'),
    #r[35] = k_b[35]*theta_X*free*free;
    ('*', 'r_b[35]', 'k_b[35]', 'theta_X'),
    ('*', 'r_b[35]', 'r_b[35]', 'free'),
    ('*', 'r_b[35]', 'r_b[35]', 'free'),
    #r[36] = k_b[36]*theta_X*theta_OH;
    ('*', 'r_b[36]', 'k_b[36]', 'theta_X'),
    ('*', 'r_b[36]', 'r_b[36]', 'theta_OH'),
    #r[37] = k_b[37]*theta_O*theta_H;
    ('*', 'r_b[37]', 'k_b[37]', 'theta_O'),
    ('*', 'r_b[37]', 'r_b[37]', 'theta_H'),
    #//what happened to r_38?!
    ('//', 'what happened to r_38?!'),
    #r[39] = k_b[39]*theta_U*theta_CH3;
    ('*', 'r_b[39]', 'k_b[39]', 'theta_U'),
    ('*', 'r_b[39]', 'r_b[39]', 'theta_CH3'),
    #r[40] = k_b[40]*theta_S*theta_CH3O;
    ('*', 'r_b[40]', 'k_b[40]', 'theta_S'),
    ('*', 'r_b[40]', 'r_b[40]', 'theta_CH3O'),
    #r[41] = k_b[41]*theta_CH3OH*free;
    ('*', 'r_b[41]', 'k_b[41]', 'theta_CH3OH'),
    ('*', 'r_b[41]', 'r_b[41]', 'free'),
    #r[42] = k_b[42]*theta_CH2*free;
    ('*', 'r_b[42]', 'k_b[42]', 'theta_CH2'),
    ('*', 'r_b[42]', 'r_b[42]', 'free'),
    #r[43] = k_b[43]*theta_CH3*free;
    ('*', 'r_b[43]', 'k_b[43]', 'theta_CH3'),
    ('*', 'r_b[43]', 'r_b[43]', 'free'),
    #r[44] = k_b[44]*theta_CH4*free;
    ('*', 'r_b[44]', 'k_b[44]', 'theta_CH4'),
    ('*', 'r_b[44]', 'r_b[44]', 'free'),
    #r[45] = k_b[45]*theta_H2O*free;
    ('*', 'r_b[45]', 'k_b[45]', 'theta_H2O'),
    ('*', 'r_b[45]', 'r_b[45]', 'free'),
    #r[46] = k_b[46]*theta_CH2O*free;
    ('*', 'r_b[46]', 'k_b[46]', 'theta_CH2O'),
    ('*', 'r_b[46]', 'r_b[46]', 'free'),
    #r[47] = k_b[47]*theta_CH3O*free*free;
    ('*', 'r_b[47]', 'k_b[47]', 'theta_CH3O'),
    ('*', 'r_b[47]', 'r_b[47]', 'free'),
    ('*', 'r_b[47]', 'r_b[47]', 'free'),
    #r[48] = k_b[48]*p_S*free*free*free*free; //phenol desorption
    ('*', 'r_b[48]', 'k_b[48]', 'p_S'),
    ('*', 'r_b[48]', 'r_b[48]', 'free'),
    ('*', 'r_b[48]', 'r_b[48]', 'free'),
    ('*', 'r_b[48]', 'r_b[48]', 'free'),
    ('*', 'r_b[48]', 'r_b[48]', 'free'),
    #r[49] = k_b[49]*p_M*free*free*free*free; //catechol desorption
    ('*', 'r_b[49]', 'k_b[49]', 'p_M'),
    ('*', 'r_b[49]', 'r_b[49]', 'free'),
    ('*', 'r_b[49]', 'r_b[49]', 'free'),
    ('*', 'r_b[49]', 'r_b[49]', 'free'),
    ('*', 'r_b[49]', 'r_b[49]', 'free'),
    #r[50] = k_b[50]*p_X*free*free*free; //benzene desorption
    ('*', 'r_b[50]', 'k_b[50]', 'p_X'),
    ('*', 'r_b[50]', 'r_b[50]', 'free'),
    ('*', 'r_b[50]', 'r_b[50]', 'free'),
    ('*', 'r_b[50]', 'r_b[50]', 'free'),
    #r[51] = k_b[51]*p_CH3OH*free; //CH3OH desorption
    ('*', 'r_b[51]', 'k_b[51]', 'p_CH3OH'),
    ('*', 'r_b[51]', 'r_b[51]', 'free'),
    #r[52] = k_b[52]*p_CH4*free; //CH4 desorption
    ('*', 'r_b[52]', 'k_b[52]', 'p_CH4'),
    ('*', 'r_b[52]', 'r_b[52]', 'free'),
    #r[53] = k_b[53]*p_H2O*free; //H2O desorption
    ('*', 'r_b[53]', 'k_b[53]', 'p_H2O'),
    ('*', 'r_b[53]', 'r_b[53]', 'free'),
    #r[54] = k_b[54]*p_K*free*free*free*free; //anisole desorption
    ('*', 'r_b[54]', 'k_b[54]', 'p_K'),
    ('*', 'r_b[54]', 'r_b[54]', 'free'),
    ('*', 'r_b[54]', 'r_b[54]', 'free'),
    ('*', 'r_b[54]', 'r_b[54]', 'free'),
    ('*', 'r_b[54]', 'r_b[54]', 'free'),
    #//not using r[55] through r[74]?!
    #//also, consider making below assignments in-order (might help optimizer).
    ('//', 'not using r[55] through r[74]?!'),
    ('//', 'also, consider making below assignments in-order (might help optimizer).'),
    #r[71] = k_b[71]*theta_Z*theta_H;
    ('*', 'r_b[71]', 'k_b[71]', 'theta_Z'),
    ('*', 'r_b[71]', 'r_b[71]', 'theta_H'),
    #r[72] = k_b[72]*theta_U*theta_CH;
    ('*', 'r_b[72]', 'k_b[72]', 'theta_U'),
    ('*', 'r_b[72]', 'r_b[72]', 'theta_CH'),
    #r[73] = k_b[73]*theta_Z1*theta_H;
    ('*', 'r_b[73]', 'k_b[73]', 'theta_Z1'),
    ('*', 'r_b[73]', 'r_b[73]', 'theta_H'),
    #// r[74] = k_b[74]*theta_N*0.1; // 0.1 is the coverage of CO.
    #r[74] = k_f[74]*theta_Z1 - k_b[74]*theta_N*theta_CO;
    ('*', 'r_b[74]', 'k_b[74]', 'theta_N'),
    ('*', 'r_b[74]', 'r_b[74]', 'theta_CO'),
    #r[75] = k_b[75]*theta_Y*free;
    ('*', 'r_b[75]', 'k_b[75]', 'theta_Y'),
    ('*', 'r_b[75]', 'r_b[75]', 'free'),
    #r[76] = k_b[76]*theta_R*theta_OH;
    ('*', 'r_b[76]', 'k_b[76]', 'theta_R'),
    ('*', 'r_b[76]', 'r_b[76]', 'theta_OH'),
    #r[77] = k_b[77]*theta_CHO;
    ('*', 'r_b[77]', 'k_b[77]', 'theta_CHO'),
    #blank line for separation
    ('//', ''),
    #// steps including C, D, K, Q.
    ('//',' steps including C, D, K, Q.'),
    #r[2] = k_b[2] *theta_C*free;
    ('*', 'r_b[2]', 'k_b[2]', 'theta_C'),
    ('*', 'r_b[2]', 'r_b[2]', 'free'),
    #r[3] = k_b[3] *theta_D*theta_OH;
    ('*', 'r_b[3]', 'k_b[3]', 'theta_D'),
    ('*', 'r_b[3]', 'r_b[3]', 'theta_OH'),
    #r[9] = k_b[9] *theta_K*theta_OH;
    ('*', 'r_b[9]', 'k_b[9]', 'theta_K'),
    ('*', 'r_b[9]', 'r_b[9]', 'theta_OH'),
    #r[10] = k_b[10]*theta_K*free;
    ('*', 'r_b[10]', 'k_b[10]', 'theta_K'),
    ('*', 'r_b[10]', 'r_b[10]', 'free'),
    #r[20] = k_b[20]*theta_Q*theta_H;
    ('*', 'r_b[20]', 'k_b[20]', 'theta_Q'),
    ('*', 'r_b[20]', 'r_b[20]', 'theta_H'),
    #r[29] = k_b[29]*theta_R*theta_CH2;
    ('*', 'r_b[29]', 'k_b[29]', 'theta_R'),
    ('*', 'r_b[29]', 'r_b[29]', 'theta_CH2'),
]


#overall reaction rates of the sub-reactions:
r = [
    #the overall rates of the reactions are computed with this little loop:
    ('custom', 'for(i = 0; i < 74; i++) {'),
    ('-', 'r[i]', 'r_f[i]', 'r_b[i]'),
    ('custom', '}'),
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


summation_thetas = [
    #// finally the summation of all thetas should be 1.
    ('//', ' finally the summation of all thetas should be 1.'),
    #mpf_set(out[38], ...);
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
    src = [r_f, r_b, r]
    result = map(assemble, src)
    for item in result: print item