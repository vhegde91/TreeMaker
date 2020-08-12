#!/bin/bash
input_Scan=$1
#anaExe="multijet"
#anaArg="FastSim_T5qqqqHg"
exeAtWorker="workerRun.sh"
#dataSetType="T5qqqqHg"
filesToTransfer=""
while read -a fileRun
do 
    echo ${fileRun[0]} ${fileRun[1]}
    jdl_file="condor_${fileRun[1]}_job.jdl"
    log_prefix="condor_${fileRun[1]}_job"
    echo $jdl_file
#    echo $log_prefix
    echo "universe = vanilla">$jdl_file
    echo "Executable = $exeAtWorker">>$jdl_file
    echo "Should_Transfer_Files = YES">>$jdl_file
    echo "WhenToTransferOutput = ON_EXIT_OR_EVICT">>$jdl_file
    echo "Transfer_Input_Files = ${filesToTransfer}">>$jdl_file
    echo "Output = ${log_prefix}.stdout">>$jdl_file
    echo "Error = ${log_prefix}.stderr">>$jdl_file
    echo "Log = ${log_prefix}.condor">>$jdl_file
    echo "notification = never">>$jdl_file
    echo "Arguments = ${massP[1]}">>$jdl_file
    echo "Queue">>$jdl_file
#    condor_submit $jdl_file
done < $input_Scan



# root://kodiak-se.baylor.edu//store/user/akanugan/TChipmWW/MINIAOD/SUS-RunIIAutumn18MiniAOD-99997-1000_100.root
