# from ROOT import TCanvas, TPad, TFile, TPaveText
# from ROOT import gBenchmark, gStyle, gROOT
# import ROOT
# c1 = TCanvas('c1','The Ntuple canvas',200,10,700,780)
# # h1 = ROOT.TH2F("h1","h1;dsf;dsf",100,-4,4,100,-500,500)
# h2 = ROOT.TH1F("h2","h2",100,-500,500)
# # h2.SetLineColor(2)
# # h1 = ROOT.TProfile("hprof","Profile of pz versus px",100,-4,4,0,20)
# f = TFile("/hpcfs/bes/mlgpu/sharma/ML_GPU/Samples/FlashggNtuples_WithMoreVars/2017/DNN_Evaluate_HHWWyyDNN_NewModel6_E150_LR10em4_B150_VarMixV1MaxBRmvCorr_Trial2_BalanceYields/GluGluToHHTo2G2ZTo2G4Q_node_cHHH1_2017.root")
# treeIn1 = f.Get("GluGluToHHTo2G2ZTo2G4Q_node_cHHH1_13TeV_HHWWggTag_1")
# treeIn1.Draw("Leading_Photon_MVA>>h2")
# # gStyle.SetLineColor(2)
# h2.Draw("same")
# ROOT.gPad.SetBottomMargin(0.3)
# # treeIn1.Draw("Subleading_Photon_MVA")
# # treeIn1.SetLineColor(2)
# c1.SaveAs("Plot2D.png")
from ROOT import TCanvas, TPad, TFile, TPaveText
from ROOT import gBenchmark, gStyle, gROOT
import ROOT
# c1 = TCanvas('c1','The Ntuple canvas',200,10,700,780)
# ------------------------- Define the file and tree input ------------------------- #
whatFileTree = {'/hpcfs/bes/mlgpu/sharma/ML_GPU/Samples/FlashggNtuples_WithMoreVars/2017/DNN_Evaluate_HHWWyyDNN_NewModel6_E150_LR10em4_B150_VarMixV1MaxBRmvCorr_Trial2_BalanceYields/GluGluToHHTo2G4Q_node_cHHH1_2017.root':["GluGluToHHTo2G4Q_node_cHHH1_13TeV_HHWWggTag_1"],'/hpcfs/bes/mlgpu/sharma/ML_GPU/Samples/FlashggNtuples_WithMoreVars/2017/DNN_Evaluate_HHWWyyDNN_NewModel6_E150_LR10em4_B150_VarMixV1MaxBRmvCorr_Trial2_BalanceYields/GluGluToHHTo2B2G_node_cHHH1_2017.root':["GluGluToHHTo2B2G_node_cHHH1_13TeV_HHWWggTag_1"],'/hpcfs/bes/mlgpu/sharma/ML_GPU/Samples/FlashggNtuples_WithMoreVars/2017/DNN_Evaluate_HHWWyyDNN_NewModel6_E150_LR10em4_B150_VarMixV1MaxBRmvCorr_Trial2_BalanceYields/GluGluToHHTo2G2ZTo2G4Q_node_cHHH1_2017.root':["GluGluToHHTo2G2ZTo2G4Q_node_cHHH1_13TeV_HHWWggTag_1"],'/hpcfs/bes/mlgpu/sharma/ML_GPU/Samples/FlashggNtuples_WithMoreVars/2017/DNN_Evaluate_HHWWyyDNN_NewModel6_E150_LR10em4_B150_VarMixV1MaxBRmvCorr_Trial2_BalanceYields/Data_2017.root':["Data_13TeV_HHWWggTag_1"]}

for nameFileTree in whatFileTree:
    print(nameFileTree)
    i = 0
    i = i+


