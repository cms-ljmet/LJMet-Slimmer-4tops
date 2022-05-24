#!/bin/bash

echo 'NOMINAL'
python -u makeStep2condor.py nominal
sleep 1

#echo "JECUP"
#python -u makeStep2condor.py JECup
#sleep 1
#
#echo "JECDOWN"
#python -u makeStep2condor.py JECdown
#sleep 1
#
#echo "JERUP"
#python -u makeStep2condor.py JERup
#sleep 1
#
#echo "JERDOWN"
#python -u makeStep2condor.py JERdown
#

shiftList=(JEC_Absolute_2016down  JECdown            JEC_HF_2016up                JEC_Totalup
		   JEC_Absolute_2016up    JEC_EC2_2016down   JEC_HFdown                   JECup
		   JEC_Absolutedown       JEC_EC2_2016up     JEC_HFup                     JERdown
		   JEC_Absoluteup         JEC_EC2down        JEC_RelativeBaldown          JERup
		   JEC_BBEC1_2016down     JEC_EC2up          JEC_RelativeBalup            
		   JEC_BBEC1_2016up       JEC_FlavorQCDdown  JEC_RelativeSample_2016down
		   JEC_BBEC1down          JEC_FlavorQCDup    JEC_RelativeSample_2016up
		   JEC_BBEC1up            JEC_HF_2016down    JEC_Totaldown
)
for sft in ${shiftList[@]}; do
    echo ${sft}
    python -u makeStep2condor.py ${sft}
done

echo "SUBMIT DONE"
