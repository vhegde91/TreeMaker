# Read parameters
from TreeMaker.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()
name = parameters.value("name","")
nstart = parameters.value("nstart",0)
nfiles = parameters.value("nfiles",-1)
redir = parameters.value("redir","root://cmsxrootd.fnal.gov/")

# handle site name usage
if redir[0]=="T":
    redir = "root://cmsxrootd.fnal.gov//store/test/xrootd/"+redir

import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

# this inputs the input files
if nfiles==-1:
    process.load("TreeMaker.Production."+name+"_cff")
else:
    readFiles = getattr(__import__("TreeMaker.Production."+name+"_cff",fromlist=["readFiles"]),"readFiles")
    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(readFiles[nstart:(nstart+nfiles)])
    )

# log output
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.categories.append('TreeMaker')
process.MessageLogger.cerr.TreeMaker = cms.untracked.PSet(
    optionalPSet = cms.untracked.bool(True),
    limit = cms.untracked.int32(10000000),
)

# temporary redirector fix
for f,val in enumerate(process.source.fileNames):
    if process.source.fileNames[f][0:6]=="/store":
        process.source.fileNames[f] = redir+process.source.fileNames[f]

process.demo = cms.EDAnalyzer('NeffFinder',
    name = cms.string(name)
)

process.p = cms.Path(process.demo)

process.MessageLogger.cerr.FwkReport.reportEvery = 10000
