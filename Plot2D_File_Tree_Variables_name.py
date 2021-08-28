# ------------------------- Define the file and tree input ------------------------- #
whatFileTree = {'/hpcfs/bes/mlgpu/sharma/ML_GPU/Samples/FlashggNtuples_WithMoreVars/2017/DNN_Evaluate_HHWWyyDNN_NewModel6_E150_LR10em4_B150_VarMixV1MaxBRmvCorr_Trial2_BalanceYields/GluGluToHHTo2G4Q_node_cHHH1_2017.root':["GluGluToHHTo2G4Q_node_cHHH1_13TeV_HHWWggTag_1"],'/hpcfs/bes/mlgpu/sharma/ML_GPU/Samples/FlashggNtuples_WithMoreVars/2017/DNN_Evaluate_HHWWyyDNN_NewModel6_E150_LR10em4_B150_VarMixV1MaxBRmvCorr_Trial2_BalanceYields/GluGluToHHTo2B2G_node_cHHH1_2017.root':["GluGluToHHTo2B2G_node_cHHH1_13TeV_HHWWggTag_1"],'/hpcfs/bes/mlgpu/sharma/ML_GPU/Samples/FlashggNtuples_WithMoreVars/2017/DNN_Evaluate_HHWWyyDNN_NewModel6_E150_LR10em4_B150_VarMixV1MaxBRmvCorr_Trial2_BalanceYields/GluGluToHHTo2G2ZTo2G4Q_node_cHHH1_2017.root':["GluGluToHHTo2G2ZTo2G4Q_node_cHHH1_13TeV_HHWWggTag_1"],'/hpcfs/bes/mlgpu/sharma/ML_GPU/Samples/FlashggNtuples_WithMoreVars/2017/DNN_Evaluate_HHWWyyDNN_NewModel6_E150_LR10em4_B150_VarMixV1MaxBRmvCorr_Trial2_BalanceYields/Data_2017.root':["Data_13TeV_HHWWggTag_1"]}

# --------------------- Define the variable name we input -------------------- #
whatVaribles = {

        " Leading_Photon_pt:Leading_Photon_phi":["Leading_Photon_pt","Leading_Photon_phi",100,0,700 ,100,-4,4,"Leading_Photon_pt>0 && 4>Leading_Photon_phi>-4"],

        " Leading_Photon_pt:Leading_Photon_eta":["Leading_Photon_pt","Leading_Photon_eta",100 ,0 ,700 ,100,-3,3,"Leading_Photon_pt>0 && 3>Leading_Photon_eta>-3"],

         " Subleading_Photon_pt:Subleading_Photon_phi":["Subleading_Photon_pt","Subleading_Photon_phi",100,0,700 ,100,-4,4,"Subleading_Photon_pt>0 && 4>Subleading_Photon_phi>-4"],

        " Subleading_Photon_pt:Subleading_Photon_eta":["Subleading_Photon_pt","Subleading_Photon_eta",100 ,0 ,700 ,100,-3,3,"Subleading_Photon_pt>0 && 3>Subleading_Photon_eta>-3"],

        " goodJets_0_pt:goodJets_0_eta":["goodJets_0_pt","goodJets_0_eta",100 ,0 ,1000 ,100,-3,3,"goodJets_0_pt>0 && 3>goodJets_0_eta>-3"],

        " goodJets_0_pt:goodJets_0_phi":["goodJets_0_pt","goodJets_0_phi",100 ,0 ,1000 ,100,-4,4,"goodJets_0_pt>0 && 4>goodJets_0_phi>-4"],

       " goodJets_1_pt:goodJets_1_eta":["goodJets_1_pt","goodJets_1_eta",100 ,0 ,700 ,100,-3,3,"goodJets_1_pt>0 && 3>goodJets_1_eta>-3"],

        " goodJets_1_pt:goodJets_1_phi":["goodJets_1_pt","goodJets_1_phi",100 ,0 ,700 ,100,-4,4,"goodJets_1_pt>0 && 4>goodJets_1_phi>-4"],        
       
       " goodJets_2_pt:goodJets_2_eta":["goodJets_2_pt","goodJets_2_eta",100 ,0 ,300 ,100,-3,3,"goodJets_2_pt>0 && 3>goodJets_2_eta>-3"],

        " goodJets_2_pt:goodJets_2_phi":["goodJets_2_pt","goodJets_2_phi",100 ,0 ,300 ,100,-4,4,"goodJets_2_pt>0 && 4>goodJets_2_phi>-4"],    

       " goodJets_3_pt:goodJets_3_eta":["goodJets_3_pt","goodJets_3_eta",100 ,0 ,200 ,100,-3,3,"goodJets_3_pt>0 && 3>goodJets_3_eta>-3"],

        " goodJets_3_pt:goodJets_3_phi":["goodJets_3_pt","goodJets_3_phi",100 ,0 ,200 ,100,-4,4,"goodJets_3_pt>0 && 4>goodJets_3_phi>-4"],

       " goodJets_4_pt:goodJets_4_eta":["goodJets_4_pt","goodJets_4_eta",100 ,0 ,100 ,100,-3,3,"goodJets_4_pt>0 && 3>goodJets_4_eta>-3"],

        " goodJets_4_pt:goodJets_4_phi":["goodJets_4_pt","goodJets_4_phi",100 ,0 ,100 ,100,-4,4,"goodJets_4_pt>0 && 4>goodJets_4_phi>-4"]

        }
whatPictureName = ["HHTo2G4Q","HHTo2B2G","2G2ZTo2G4Q","Data"]