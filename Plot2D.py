from ROOT import TCanvas, TPad, TFile, TPaveText
from ROOT import gBenchmark, gStyle, gROOT
import ROOT
from Plot2D_File_Tree_Variables_name import *
c1 = TCanvas('c1','The Ntuple canvas',200,10,700,780)

# ---------------- two loop to loop FileTree & variable name ---------------- #
i = 0
for nameFileTree in whatFileTree:
    pictureName = whatPictureName[i] 
    i = i+1
    f1 = TFile(nameFileTree)
    treeIn1 = f1.Get(whatFileTree[nameFileTree][0])
    for name in whatVaribles:
        a = ";"
        variable_name = whatVaribles[name][0] + ":" + whatVaribles[name][1]
        ybin = whatVaribles[name][2]
        ymin = whatVaribles[name][3]
        ymax = whatVaribles[name][4]
        xbin = whatVaribles[name][5]
        xmin = whatVaribles[name][6]
        xmax = whatVaribles[name][7]
        h1 = "h1" + variable_name
        h1 = ROOT.TH2F("h1",'',xbin,xmin,xmax,ybin,ymin,ymax)
        h1.SetTitleFont(100,"X")
        h1.SetTitleFont(100,"Y")
        h1.SetTitle(pictureName)
        h1.SetYTitle(whatVaribles[name][0])    
        h1.SetXTitle(whatVaribles[name][1])
        h1.SetLineColor(1)
        h1.SetLineWidth(2)
        h1.SetStats(0)
        ROOT.gPad.SetLeftMargin(0.15)
        ROOT.gPad.SetRightMargin(0.1)

        # --------------------- tree.Draw(py:px>>histogram,'cut') -------------------- #
        trDraw1 = variable_name + ">>" + "h1"
        cut = whatVaribles[name][8]
        print(trDraw1)
        treeIn1.Draw(trDraw1)


        # ----------------------- set legend for each histogram ---------------------- #
        # legend.AddEntry(h1,"HHTo2G4Q")

        h1.Draw('colz')

        pic = pictureName+ "_" + variable_name + ".png"
        c1.SaveAs(pic)

