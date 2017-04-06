from keys import *
import numpy as np
"""
Primal/initial dictionary of parts
It contains:
    -Motor Cortex
    -Striatum
    -GPe:       globus pallidus external
    -GPi:       globus pallidus internal
    -STN:       subthalamic nucleus
    -SNr:       substantia nigra pars reticulata
    -SNc:       substantia nigra pars compacta
    -Thalamus
    -Prefrontal cortex
    -NAc:       Nucleus Accumbens
    -VTA:       Ventral Tegmental Area
    -PPTg:      Pedunculopontine Tegmental nucleus
    -Amygdala
Prefix description:
    -GABA - GABA
    -Glu  - glutamate
    -ACh  - acetylcholine
    -DA   - dopamine
"""
motor = ({k_name: 'Motor cortex'},)
motor_cortex = 0

"""
motor = ({k_name: 'Motor cortex [Glu0]'},
         {k_name: 'Motor cortex [Glu1]'})
motor_Glu0, motor_Glu1 = range(2)
"""


striatum = ({k_name: 'Striatum'},)
striatumR = 0

vta = ({k_name: 'Ventral Tegmental Area'},
       {k_name: 'VTA [a1]'})
ventral_tegmental_area, vta_a1 = np.arange(2)

lc = ({k_name: 'Locus Coeruleus'},
      {k_name: 'LC [D1]'},
      {k_name: 'LC [D2]'})
locus_coeruleus, lc_D1, lc_D2 = np.arange(3)

prh = ({k_name: 'Perirhinal cortex'},)
perirhinal_cortex = 0

pgi = ({k_name: 'Nucleus paragigantocellularis lateralis'},)
nucleus_paragigantocellularis_lateralis = 0

rn = ({k_name: 'RN [a1]'},
      {k_name: 'RN [a2]'})
rn_a1, rn_a2 = np.arange(2)

bnst = ({k_name: 'Bed nucleus of the stria terminalis'},)
bed_nucleus_of_the_stria_terminalis = 0

nts = ({k_name: 'NTS [A1]'},
       {k_name: 'NTS [A2]'})
nts_a1, nts_a2 = np.arange(2)

ldt = ({k_name: 'Laterodorsal tegmentum'},
       {k_name: 'LDT [A1]'},
       {k_name: 'LDT [A2]'})
laterodorsal_tegmentum,  LDT_a1, LDT_a2 = np.arange(3)

pf = ({k_name: 'Prefrontal Cortex'},)
prefrontal_cortex = 0

motor[motor_cortex][k_NN] = 60

striatum[striatumR][k_NN] = 30

vta[ventral_tegmental_area][k_NN] = 30
vta[vta_a1][k_NN] = 30

lc[locus_coeruleus][k_NN] = 30
lc[lc_D1][k_NN] = 30
lc[lc_D2][k_NN] = 30

prh[perirhinal_cortex][k_NN] = 30

pgi[nucleus_paragigantocellularis_lateralis][k_NN] = 30

rn[rn_a1][k_NN] = 30
rn[rn_a2][k_NN] = 30

bnst[bed_nucleus_of_the_stria_terminalis][k_NN] = 30

nts[nts_a1][k_NN] = 30
nts[nts_a2][k_NN] = 30

ldt[laterodorsal_tegmentum][k_NN] = 30
ldt[LDT_a1][k_NN] = 30
ldt[LDT_a2][k_NN] = 30

pf[prefrontal_cortex][k_NN] = 30


################################################### dopa
motor_d = ({k_name: 'Motor cortex [Glu0]'},
         {k_name: 'Motor cortex [Glu1]'})
motor_d_Glu0, motor_d_Glu1 = range(2)

striatum = ({k_name: 'Striatum [D1]'},
            {k_name: 'Striatum [D2]'},
            {k_name: 'Striatum [tan]'})
D1, D2, tan = range(3)

gpe = ({k_name: 'GPe [GABA]'}, )
gpe_GABA = 0

gpi = ({k_name: 'GPi [GABA]'}, )
gpi_GABA = 0

stn = ({k_name: 'STN [Glu]'}, )
stn_Glu = 0

snr = ({k_name: 'SNr [GABA]'}, )
snr_GABA = 0

snc = ({k_name: 'SNc [GABA]'},
       {k_name: 'SNc [DA]'})
snc_GABA, snc_DA = range(2)

thalamus = ({k_name: 'Thalamus [Glu]'}, )
thalamus_Glu = 0

prefrontal = ({k_name: 'Prefrontal cortex [Glu0]'},
              {k_name: 'Prefrontal cortex [Glu1]'})
pfc_Glu0, pfc_Glu1 = range(2)

nac = ({k_name: 'NAc [ACh]'},
       {k_name: 'NAc [GABA0]'},
       {k_name: 'NAc [GABA1]'})
nac_ACh, nac_GABA0, nac_GABA1  = range(3)

vta = ({k_name: 'VTA [GABA0]'},
       {k_name: 'VTA [DA0]'},
       {k_name: 'VTA [GABA1]'},
       {k_name: 'VTA [DA1]'},
       {k_name: 'VTA [GABA2]'})
vta_GABA0, vta_DA0, vta_GABA1, vta_DA1, vta_GABA2 = range(5)

pptg = ({k_name: 'PPTg [GABA]'},
        {k_name: 'PPTg [ACh]'},
        {k_name: 'PPTg [Glu]'})
pptg_GABA, pptg_ACh, pptg_Glu = range(3)

amygdala = ({k_name: 'Amygdala [Glu]'}, )
amygdala_Glu = 0

cerebral_cortex_NN = 30
motor[motor_d_Glu0][k_NN] = 10
#motor[motor_d_Glu1][k_NN] = int(cerebral_cortex_NN * 0.2 / 6)
striatum_NN = 3
striatum[D1][k_NN] = 1
striatum[D2][k_NN] = 1
striatum[tan][k_NN] = 1
gpe[gpe_GABA][k_NN] = 8
gpi[gpi_GABA][k_NN] = 1
stn[stn_Glu][k_NN] = 2
snc[snc_GABA][k_NN] = 3              #TODO check number of neurons
snc[snc_DA][k_NN] = 1              #TODO check number of neurons
snr[snr_GABA][k_NN] = 4
thalamus[thalamus_Glu][k_NN] = int(50 / 6) #!!!!

prefrontal[pfc_Glu0][k_NN] = 8
prefrontal[pfc_Glu1][k_NN] = 8
nac[nac_ACh][k_NN] = 1               #TODO not real!!!
nac[nac_GABA0][k_NN] = 1            #TODO not real!!!
nac[nac_GABA1][k_NN] = 1            #TODO not real!!!
vta[vta_GABA0][k_NN] = 7
vta[vta_DA0][k_NN] = 2
vta[vta_GABA1][k_NN] = 7
vta[vta_DA1][k_NN] = 2
vta[vta_GABA2][k_NN] = 7
pptg[pptg_GABA][k_NN] = 2
pptg[pptg_ACh][k_NN] = 1
pptg[pptg_Glu][k_NN] = 2

amygdala[amygdala_Glu][k_NN] = 3    #TODO not real!!!
