import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/817/00000/B407B17A-9F63-E611-9581-02163E01369A.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/819/00000/3EC4D153-A063-E611-A5ED-FA163E1D2B6C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/820/00000/0CC16E28-6D64-E611-A510-02163E014147.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/820/00000/42D2BDD7-A464-E611-9FD9-02163E0133B3.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/820/00000/4A7780B1-5B64-E611-BC57-02163E0134D4.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/820/00000/4AB128D4-7964-E611-935F-02163E014560.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/820/00000/4C74F368-5064-E611-ABA6-02163E0144F8.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/820/00000/4E442D91-5D64-E611-855B-02163E011855.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/820/00000/62F55CCB-5164-E611-B9E1-02163E011852.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/820/00000/64894A9D-6064-E611-87B6-02163E01369D.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/820/00000/6CB6C378-6864-E611-A85A-02163E014156.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/820/00000/989E957A-5364-E611-B062-FA163EFEAA70.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/820/00000/C0C31D73-6264-E611-9AC3-FA163E101E0E.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/820/00000/C477180E-5664-E611-B7CE-FA163E1286C4.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/820/00000/DA58C729-5864-E611-9E2F-FA163E9F796D.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/820/00000/DCB481FF-6464-E611-A46E-02163E0145DF.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/820/00000/F0FEC385-4D64-E611-A9F6-02163E014111.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/820/00000/FCABCF69-5964-E611-B126-02163E011A36.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/821/00000/C8885E41-8664-E611-94B9-02163E013621.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/822/00000/1CFB3DA3-9264-E611-873F-FA163E6648C8.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/822/00000/36148F48-9664-E611-A049-02163E0142C5.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/822/00000/3A305090-CC64-E611-BD1E-FA163E15C6C6.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/822/00000/440B9F47-A564-E611-AB7F-02163E012704.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/822/00000/58190F17-9964-E611-B5A7-FA163E4B0BC1.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/822/00000/9E4177B4-9D64-E611-A50A-FA163ECB5AED.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/822/00000/C40FA684-8C64-E611-9CA9-02163E0142FD.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/822/00000/CEDF30E6-8E64-E611-97C8-FA163EE31E0B.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/822/00000/E8DD41C5-9064-E611-8186-02163E011940.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/822/00000/F43A501D-9464-E611-8726-FA163E4C6E71.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/822/00000/FE997A26-8E64-E611-84EE-FA163E839D37.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/873/00000/1071CCEB-F164-E611-861E-FA163E77AD59.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/874/00000/4611B7E5-3665-E611-9C0D-02163E0139AB.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/874/00000/6E597E59-0E65-E611-B543-02163E013427.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/874/00000/70F8036B-1765-E611-9DA6-FA163E7C40F9.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/874/00000/A20D86FF-3165-E611-8B64-02163E01338C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/874/00000/B8E625CE-1A65-E611-878B-FA163E30E307.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/874/00000/F4F459AF-1F65-E611-BE96-02163E01384C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/875/00000/362A20B5-4A65-E611-B465-FA163EED9AA1.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/875/00000/3CBDF718-4465-E611-85B5-02163E01195D.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/875/00000/4A5845F5-8965-E611-BAA1-FA163E8EA972.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/875/00000/A2FA8FCC-3B65-E611-BA31-FA163E9F796D.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/875/00000/A6A51114-3765-E611-871D-FA163EF21BCF.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/875/00000/B04DF953-3F65-E611-AC2E-FA163E29A92E.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/875/00000/B8A5CB69-6065-E611-A1EF-FA163E0D7C05.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/875/00000/E283AEB1-3265-E611-9E0A-FA163E070691.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/904/00000/22A4F4E4-1C65-E611-A997-02163E013845.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/922/00000/8833FD53-2D65-E611-A3CC-02163E011C17.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/923/00000/04DC4502-9E65-E611-B4FD-FA163E4C7298.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/923/00000/60A6A864-7B65-E611-AE4A-02163E013980.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/923/00000/7239C75F-7165-E611-A66B-FA163E8EEDBB.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/923/00000/7677D742-7865-E611-BE01-02163E01180F.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/923/00000/98F4C2DA-8265-E611-9671-02163E0129F0.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/923/00000/DC7F6224-8E65-E611-AE90-FA163E3551CD.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/941/00000/BCC1E2FC-5965-E611-B99A-02163E012134.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/957/00000/081B0E69-D665-E611-A5E8-FA163E1A9393.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/957/00000/B03C975A-B565-E611-9344-FA163EF0A849.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/957/00000/DE22AFAA-D465-E611-A900-FA163E69931D.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/962/00000/1624FA4B-0466-E611-93AC-02163E013620.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/962/00000/16FA7138-DE65-E611-B528-02163E011B59.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/962/00000/36E52433-E465-E611-989E-FA163E71426D.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/962/00000/A0417A15-EB65-E611-9B80-02163E012773.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/962/00000/BE205D2C-0D66-E611-8F7A-FA163E6AC788.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/963/00000/0EF0185B-EF65-E611-83B0-02163E0133B2.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/963/00000/E69356A4-0066-E611-8C59-02163E0133D8.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/969/00000/06E51CE4-C966-E611-9143-FA163E4826AB.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/969/00000/2499C42C-A866-E611-8F37-02163E011BA5.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/969/00000/3CA76B28-9466-E611-8D6B-02163E014589.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/969/00000/4E216D24-9C66-E611-8236-FA163E2405C6.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/969/00000/806A1824-9966-E611-B9DA-FA163E7FD727.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/969/00000/921B82A7-A266-E611-A8EB-FA163E9C879A.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/969/00000/B01A1973-A066-E611-9648-FA163E958BFE.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/969/00000/C888CA68-A566-E611-A056-02163E0134C9.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/969/00000/CE30EEA0-9666-E611-AB4F-02163E014411.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/969/00000/D8581E7D-9E66-E611-A4A5-02163E01421A.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/969/00000/E254A343-9D66-E611-884B-02163E011B61.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/969/00000/EEF35B7A-B766-E611-8F42-02163E0133D6.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/969/00000/F4F154A3-AF66-E611-B9B9-FA163E5CC44B.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/969/00000/FC58D690-9A66-E611-9AFC-02163E011BA5.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/975/00000/3269B2D6-B966-E611-912C-02163E01231C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/975/00000/32B8D183-A866-E611-AD0C-FA163EAE50CA.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/975/00000/38C86073-A566-E611-9FC0-02163E0135EB.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/975/00000/3A40EE0A-AC66-E611-B1E3-FA163E8E8695.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/975/00000/84430F6B-A166-E611-84A3-02163E012719.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/975/00000/CA75C7DC-9A66-E611-ACC5-FA163E096FCE.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/975/00000/F21D8983-E466-E611-8957-02163E0144BB.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/976/00000/4043C089-C066-E611-BDE9-FA163EA3EA50.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/986/00000/0A98A889-F566-E611-A06E-02163E012439.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/278/986/00000/80DEB3C9-D466-E611-8BF8-02163E01357B.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/024/00000/08B562C1-7967-E611-B9E6-02163E0146AF.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/024/00000/1465D0C9-A167-E611-9007-FA163E9F0571.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/024/00000/3A3435BC-7367-E611-B5AF-02163E013599.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/024/00000/4A4FA4EE-7E67-E611-99BA-02163E0125C5.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/024/00000/F015C445-AF67-E611-B215-02163E0143C9.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/028/00000/4456DF1B-8E67-E611-A1B9-02163E011D24.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/029/00000/18A0FCCD-A067-E611-AA2E-FA163ED92227.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/029/00000/1AD0619B-8C67-E611-960A-02163E01342A.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/029/00000/22EEE405-9C67-E611-B7CB-02163E011C20.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/071/00000/2A9D30F7-1568-E611-A93D-FA163E91A1EC.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/071/00000/908461B9-1668-E611-9547-02163E013403.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/071/00000/96C60D07-1668-E611-8B77-FA163E1851FB.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/071/00000/A4880527-0168-E611-947F-02163E011BA5.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/080/00000/0840B521-4068-E611-BFC8-02163E011843.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/080/00000/8A9DAF15-4068-E611-BD81-FA163E63263E.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/080/00000/E47BC71A-4068-E611-B5A2-FA163EDFC379.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/085/00000/26A064AA-5768-E611-A19C-02163E012657.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/115/00000/2E6B6517-0269-E611-AFAE-02163E013777.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/115/00000/3096156C-1669-E611-A7FB-FA163E5CC44B.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/115/00000/407AD0AF-FB68-E611-9F43-02163E01373F.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/115/00000/84E676C2-0A69-E611-803C-02163E0142C5.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/115/00000/B421BE8C-2469-E611-BAE8-02163E01360C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/115/00000/B4E6577A-F668-E611-AFD4-FA163E101E0E.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/116/00000/5419E82C-1869-E611-84D9-FA163E2633E7.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/116/00000/84B6BA4B-2269-E611-9D31-02163E01276F.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/116/00000/AC30D494-1D69-E611-805C-02163E01263A.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/116/00000/DE8454C5-3669-E611-9263-02163E011A26.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/116/00000/E0AE20BA-1269-E611-80A0-02163E0135D5.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/298/00000/AE7A437F-026B-E611-972A-02163E014685.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/479/00000/C67922A3-6E6C-E611-968E-FA163EE6E572.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/480/00000/96FE57CD-286C-E611-9C0D-02163E013770.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/484/00000/A4B0F178-2D6C-E611-8C0F-FA163E61E7CA.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/487/00000/C24A1628-336C-E611-A069-FA163EB26939.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/488/00000/22723BB0-356C-E611-AC88-02163E0138F9.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/489/00000/2844248E-C16E-E611-A678-FA163E8F391D.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/557/00000/BCE569A2-C86E-E611-B976-02163E011906.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/588/00000/0289878F-426F-E611-A341-02163E012162.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/588/00000/0AFB00EE-046F-E611-8180-02163E01451C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/588/00000/1A442368-1E6F-E611-9F3C-FA163E61263C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/588/00000/225699AF-196F-E611-92C8-FA163E2BC4D8.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/588/00000/26592F00-226F-E611-9740-02163E0142E1.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/588/00000/60E4C4E1-2B6F-E611-A59D-FA163ECB2A1A.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/588/00000/86B7A69B-506F-E611-ACE9-02163E0140D5.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/588/00000/A4F722F1-0C6F-E611-B249-02163E0143DF.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/588/00000/B026A58A-246F-E611-8CF8-02163E01189C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/588/00000/DC52D03C-036F-E611-B750-FA163E1851FB.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/588/00000/DE449E68-FC6E-E611-AA31-FA163EE8BC3A.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/588/00000/E00E7E84-116F-E611-863B-02163E01447D.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/588/00000/E622A7C1-186F-E611-A199-FA163EE0E3A6.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/588/00000/FC8C0E74-156F-E611-B0A7-FA163E40D8B9.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/653/00000/06A0920B-416F-E611-9FE7-02163E012185.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/653/00000/36990B9C-686F-E611-A78E-02163E012807.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/653/00000/AA1F956D-4A6F-E611-9CD8-02163E013816.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/654/00000/348DD4E5-9F6F-E611-B33F-02163E0133A5.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/654/00000/4629DD43-866F-E611-B41B-02163E012319.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/654/00000/46E9423E-936F-E611-B9D8-FA163E0D1D72.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/654/00000/481599E9-956F-E611-B826-FA163E440508.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/654/00000/4E6E1997-906F-E611-880F-02163E0146F5.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/654/00000/5450F181-906F-E611-B43E-FA163E2CDE09.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/654/00000/7E669752-936F-E611-A944-02163E012517.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/654/00000/8C44ED07-836F-E611-B9A7-02163E014748.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/654/00000/9C8E6F7F-986F-E611-A378-FA163E77AD59.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/654/00000/B4DCEE59-8D6F-E611-B657-FA163EE80441.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/654/00000/B8071865-A76F-E611-B234-02163E011D2E.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/654/00000/E0E8A317-BA6F-E611-B125-02163E011AEF.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/654/00000/F2FD92A0-896F-E611-A931-02163E01444B.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/656/00000/F0D04D9C-896F-E611-A127-02163E01471C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/658/00000/3AC90249-B86F-E611-BAE7-02163E0144EF.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/658/00000/44A63D3A-A56F-E611-B867-02163E014405.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/658/00000/82A2B297-AC6F-E611-95F4-02163E0146A4.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/658/00000/A63B3415-AA6F-E611-AF3D-02163E014119.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/658/00000/FA474B3F-E06F-E611-8935-02163E01378C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/658/00000/FC6CAC0B-A56F-E611-832E-02163E013430.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/667/00000/0C95D43F-FC6F-E611-B926-02163E011EF4.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/667/00000/2E47EF14-FC6F-E611-A4F5-02163E011D34.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/667/00000/30D5A40F-FD6F-E611-A28F-FA163E9D91D8.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/667/00000/4A6AF6BC-0370-E611-943C-FA163E817FDD.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/667/00000/5E19C3EE-F16F-E611-9B65-02163E013895.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/667/00000/6AB63BE1-0570-E611-9F58-FA163EE89D6C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/667/00000/709BB295-F46F-E611-8F37-FA163EF21BCF.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/667/00000/741C44BC-0C70-E611-871E-02163E014700.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/667/00000/767D68BB-3070-E611-9CF2-02163E0139AA.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/667/00000/8C10ED2C-1470-E611-8EC7-02163E0137BA.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/667/00000/AA41A506-0170-E611-8EF9-02163E011EF4.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/681/00000/F0861FDE-2370-E611-887E-02163E011B3F.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/682/00000/EC9ABF0F-2E70-E611-8929-02163E0142E6.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/683/00000/1A24130E-2570-E611-B1A6-02163E01360C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/684/00000/083EDD6F-1970-E611-AF32-02163E014189.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/685/00000/2C21BF83-1270-E611-8201-02163E01433D.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/685/00000/3E01F82E-0A70-E611-8D09-02163E0124BC.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/685/00000/EC24472F-3470-E611-965B-02163E014205.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/691/00000/12481FCE-3C70-E611-B483-FA163E89A538.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/00F58204-7170-E611-853A-02163E011B3C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/20647742-8270-E611-976D-02163E011A36.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/2ED2304C-7A70-E611-96AB-02163E0146F7.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/3A7CF708-7370-E611-90E9-02163E01478E.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/3E3D6DBC-7570-E611-80BD-FA163EECCDFC.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/3E52DE20-7C70-E611-BAA3-FA163EDA63B1.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/48373047-7470-E611-B0D6-02163E01465C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/540BAF15-6570-E611-AAC3-02163E0144DF.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/6206965B-6170-E611-B155-02163E013556.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/6CD45437-8A70-E611-9CD4-02163E0144FF.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/76C1CD26-6C70-E611-8B77-02163E013750.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/7A815E76-A470-E611-B106-FA163EB9CEA3.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/7CC253C9-7870-E611-8914-02163E014219.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/7E2CE2D2-7E70-E611-B35E-FA163ECFBB33.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/82746103-6A70-E611-AA93-02163E011B2E.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/90532606-6A70-E611-98B6-02163E013437.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/9E537B82-6770-E611-A64E-02163E0136CD.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/A0D9E291-9070-E611-9733-FA163E5A001F.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/A0E3258A-6E70-E611-97F8-FA163E98B032.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/DEA19F02-7170-E611-98AF-FA163EDC8BE6.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/694/00000/FC6D2FAF-7770-E611-84A7-FA163E552EA3.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/715/00000/2ABB8BC9-B270-E611-8447-FA163EAB012C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/715/00000/4AC3C366-B570-E611-B0BE-FA163E1D2B6C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/715/00000/4AFADF3D-B870-E611-96AF-FA163EE80441.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/715/00000/72997739-AE70-E611-A219-02163E011CA2.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/715/00000/9AA817DC-E870-E611-9478-02163E014537.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/715/00000/ACFB95A5-AF70-E611-822C-02163E011FC5.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/715/00000/D0BD485D-BE70-E611-AE84-02163E011DDA.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/715/00000/EC96EFC3-D470-E611-A944-02163E0141D9.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/716/00000/02C2801D-FE70-E611-AE4A-02163E012134.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/716/00000/06A2AB1E-0771-E611-A835-FA163E949055.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/716/00000/0A0052BD-FB70-E611-B352-02163E0134D3.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/716/00000/0ADC8D07-0371-E611-BEF4-FA163ECB5AED.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/716/00000/1C9DB8D4-F170-E611-99F4-FA163E37EA05.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/716/00000/26BBEDE1-0E71-E611-B09D-02163E014580.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/716/00000/2C22F48A-0171-E611-8AD2-FA163EB30FC4.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/716/00000/4A3AEC4B-2171-E611-8B61-02163E0128E7.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/716/00000/4C24DA5D-F470-E611-AA3A-FA163EFB1786.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/716/00000/58E586F4-FC70-E611-910C-02163E0143D7.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/716/00000/5C8EF7B5-FF70-E611-8F9A-02163E011FBC.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/716/00000/68452CDD-F970-E611-9369-FA163E48A31D.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/716/00000/B6AEE659-F770-E611-9362-02163E0136F3.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/716/00000/C4D63B80-0471-E611-AA68-02163E0124E9.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/716/00000/E6C639D5-2B71-E611-B26F-02163E011DE2.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/760/00000/183E88C2-3271-E611-90D9-02163E0136FC.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/760/00000/28B12C04-2971-E611-9DB5-02163E012B13.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/760/00000/848C88AB-4D71-E611-9A9B-02163E01353B.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/760/00000/883ECEA6-1F71-E611-A844-02163E014333.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/760/00000/CAD93B67-3771-E611-A32C-02163E011823.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/760/00000/DC7974B8-4171-E611-B30E-02163E0140FE.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/760/00000/DCB611C6-3171-E611-953D-FA163EC64E27.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/760/00000/E60183D4-2571-E611-A913-FA163E99558E.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/766/00000/0E83D624-7971-E611-9ADF-02163E0142A9.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/766/00000/1610D6CD-A971-E611-A45B-02163E012484.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/766/00000/2A3941E3-8271-E611-9524-FA163E7A6AB2.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/766/00000/3EAE2057-7471-E611-926F-FA163E6648C8.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/766/00000/4242A470-7B71-E611-8663-02163E0134DE.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/766/00000/62EEDBFA-7E71-E611-8CFF-02163E0142E3.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/766/00000/7874CD46-7D71-E611-8049-FA163E2282A1.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/766/00000/867C88A9-7171-E611-8779-FA163E12ACCD.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/766/00000/8C72EE60-8F71-E611-A7FE-02163E01368A.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/766/00000/9A9F92B8-8071-E611-9E55-02163E0133E1.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/766/00000/A2948429-7671-E611-B544-02163E0145E9.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/766/00000/AC37F6B8-7C71-E611-9CF0-02163E014253.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/766/00000/EE203564-8571-E611-8059-FA163EF672C9.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/766/00000/F0D9DC84-8971-E611-93B3-FA163EF2D667.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/767/00000/04FDEAFC-8571-E611-B44A-02163E0122C7.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/767/00000/3A110114-8C71-E611-9B43-02163E012983.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/767/00000/405634A5-AE71-E611-B642-02163E014655.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/767/00000/CCAFB7ED-8971-E611-9B14-FA163E959AB4.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/767/00000/CEE5B444-8F71-E611-A329-FA163E298B60.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/794/00000/0654FE96-B671-E611-9030-02163E01395C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/794/00000/168F7455-C371-E611-B341-FA163E8B436C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/794/00000/3263B4FF-D471-E611-A95B-FA163E362006.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/794/00000/3A39B91C-C171-E611-87D2-FA163EB26939.root',
] )
readFiles.extend( [
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/794/00000/642B796C-BD71-E611-AA7E-02163E01270C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/794/00000/6667754C-FD71-E611-BE59-02163E0118F6.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/794/00000/845D104D-D071-E611-86C4-02163E0124E0.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/794/00000/869D9E93-C871-E611-8857-02163E0140E5.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/794/00000/A262C85B-F571-E611-9242-FA163E30E307.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/794/00000/AC49E88D-CB71-E611-A743-02163E0133D6.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/794/00000/C633ACCB-C571-E611-AA4C-02163E0141E6.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/794/00000/EEB4958F-BA71-E611-8421-FA163EE0F07E.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/823/00000/24F031EF-F271-E611-B5E8-02163E0143AF.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/823/00000/64949686-F971-E611-A792-02163E011A31.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/823/00000/94E1D753-EB71-E611-B600-02163E011CB7.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/823/00000/CCA0B775-F771-E611-A30A-02163E011939.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/823/00000/F0F2769D-D671-E611-A14B-02163E0141EF.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/840/00000/5825500B-AA71-E611-904F-FA163EE75782.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/841/00000/001BEC5B-7972-E611-8062-02163E014250.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/841/00000/0075A44D-6B72-E611-B25C-FA163E07E120.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/841/00000/0C4F57EB-7572-E611-8A36-02163E0123CA.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/841/00000/447A9A37-7472-E611-B5FF-02163E01457D.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/841/00000/4C94C4DE-6272-E611-B959-FA163E070691.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/841/00000/5003E858-6B72-E611-B52F-02163E013972.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/841/00000/64DC2DE6-6972-E611-A896-02163E0138F1.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/841/00000/68BD5F01-6F72-E611-B62A-02163E011809.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/841/00000/6A3A6499-7172-E611-A567-FA163EA11449.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/841/00000/6A7C5A5C-6C72-E611-A36D-02163E012526.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/841/00000/7A3085C7-6C72-E611-861B-02163E013599.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/841/00000/82356CD6-7D72-E611-9CFD-02163E01471C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/841/00000/A67C815B-8C72-E611-ACFF-02163E01343C.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/841/00000/A86D6207-6C72-E611-BA6B-02163E012B81.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/841/00000/B4D3B9C1-6F72-E611-9D95-02163E013777.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/841/00000/C0886712-9C72-E611-9D30-02163E011ABF.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/841/00000/CC5A20EB-6D72-E611-BEE5-02163E01284B.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/841/00000/DE609148-7372-E611-AB6C-02163E0136A3.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/841/00000/DEF449A0-8372-E611-887F-FA163EF0A849.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/844/00000/06018C10-A272-E611-8F12-02163E013716.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/844/00000/DA279073-CC72-E611-AA7B-02163E01201E.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/844/00000/E4C183B9-AD72-E611-A165-FA163EA90023.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/887/00000/4A336AA7-CF72-E611-AA57-02163E013553.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/887/00000/7869A70E-0373-E611-BBF0-FA163EE6E572.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/887/00000/849F3472-C172-E611-9A9E-FA163E0EA239.root',
       '/store/data/Run2016G/SinglePhoton/MINIAOD/PromptReco-v1/000/279/887/00000/B0A236A9-E572-E611-A815-02163E014356.root',
] )
