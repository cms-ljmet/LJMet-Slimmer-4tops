#include "step2.cc"
#include "Davismt2.cc"
#include "S2HardcodedConditions.cc"

using namespace std;

void testStep2(){
  TString inputFile=
   "/mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2016_Jan2021_4t_051321_step1hadds/nominal/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8_hadd.root";   
    //"/mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2018_Oct2019_4t_10072020_step1hadds/nominal/TTTT_TuneCP5_13TeV-amcatnlo-pythia8_hadd.root" ;
  // "/mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_032721_step1hadds/nominal/TTToSemiLepton_HT500Njet9_TuneCP5_PSweights_13TeV-powheg-pythia8_ttcc_hadd.root";
//  "/mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_02162021_step1hadds/nominal/SingleElectron_hadd.root";
// "/mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_02162021_step1hadds/nominal/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_tt1b_hadd.root";
//  "/mnt/hadoop/store/group/bruxljm/FWLJMET102X_1lep2017_Oct2019_4t_02162021_step1hadds/nominal/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8_hadd.root";
  TString outputFile="step2_test.root";

  gSystem->AddIncludePath("-I$CMSSW_BASE/src/");

  step2 t(inputFile,outputFile);
  t.Loop();
}

