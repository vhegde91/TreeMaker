import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/0200761D-BF8B-E611-AACB-002590791D60.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/027548F7-B28A-E611-A1FB-6CC2173BBAB0.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/028881DE-F68B-E611-BDBB-0025905B85D2.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/02A3E552-638B-E611-B926-008CFA19746C.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/0674CA74-288B-E611-AF24-0CC47A4D7626.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/06D1C0FE-178C-E611-8238-002590AC4C6E.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/06E271FE-888B-E611-A9CB-0025905B85BC.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/08506C73-378A-E611-B125-00304867FD0B.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/08F06F59-DF8A-E611-912E-002590A37118.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/0AD34230-1E8B-E611-813D-0CC47A78A446.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/0EAB849F-D18B-E611-9E11-9CB654AEAE86.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/101D5384-8F88-E611-AEF4-008CFA1CBB34.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/102C95B5-0A8B-E611-BEB2-0025905A6088.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/1076C94D-C686-E611-8331-00A0D1EC7318.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/10FB0558-AF8B-E611-B8CA-0CC47A78A4BA.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/12323A4F-CA89-E611-B619-0025905C3DF8.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/12439C03-298B-E611-95DE-0CC47A7C361E.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/12B58562-418B-E611-A5F2-008CFA11138C.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/12E38557-5D88-E611-A76C-1418774124DE.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/14E4F3AB-F48A-E611-9FF4-0025907859B8.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/16F4B1B4-A28B-E611-B5C4-0025905A60D0.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/1845E2F3-F287-E611-93CD-008CFA165F28.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/188F6B76-1B8C-E611-8869-7CD30AB5BBBE.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/18E4B0DE-F68A-E611-9029-0CC47A4D7604.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/1A03EFCC-C68B-E611-93FC-008CFA197928.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/1CF20D9C-108B-E611-AAB4-0CC47A4C8EBA.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/1E9E29D2-248B-E611-9A6D-008CFA111190.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/20142DD4-FC8A-E611-A468-0CC47A4D7604.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/206F4876-A78B-E611-B289-0CC47AA989BE.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/24739D82-C086-E611-9EF4-0025905C2CBE.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/281B40A8-158B-E611-B4AD-0CC47A4D75F6.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/28916D9C-8786-E611-A629-0CC47A0AD48A.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/28EB0EB1-8F8C-E611-89F9-002590D9D8B8.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/2A24D6E9-EC8A-E611-B027-0242AC130002.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/2A2E8838-AF8B-E611-BF58-0CC47A78A360.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/2A37553B-3B8B-E611-99CB-0025905A605E.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/2A9C5C21-CD88-E611-AEDB-001E6739AC71.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/2AC529CE-C28B-E611-93CA-008CFA197418.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/2E488B67-C688-E611-82E1-00238BBD754A.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/2E69BD7B-BB8B-E611-A70A-0242AC130002.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/2E72D8DD-9D8C-E611-8401-0025905A610A.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/2E909EE8-B98B-E611-8659-0CC47A4D7634.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/2EFB1F9E-D68B-E611-9215-001E67792542.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/3080677C-A78B-E611-9812-008CFA1113B4.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/309C5D1E-768B-E611-AD72-008CFA197980.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/30CB363C-AF8B-E611-95CC-0025905A60F4.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/30FA0C84-8F8B-E611-B9C0-0025901D08B0.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/3209A0B5-0A8B-E611-A5FD-0025905A60CE.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/324EC00B-638B-E611-9548-0025905A60B2.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/34A010CB-4A8B-E611-8F49-002590FD5A78.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/34F9FDB5-0A8B-E611-9DFD-0CC47A78A3F8.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/362BA4ED-A088-E611-A894-002590A88802.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/369CBE48-0D8B-E611-B65C-0242AC130003.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/36B32816-508B-E611-B47E-3417EBE47FCA.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/38C5EE6A-4E8B-E611-82C2-0CC47A78A3F8.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/3C80EA83-B68B-E611-B93B-0242AC130004.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/3E30283C-AF8B-E611-8BD9-0025905A6080.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/3E77F5BB-8D8C-E611-B2D7-008CFA165F18.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/3EC24B73-0E8B-E611-A582-0CC47A7C3404.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/4090C9A3-6C8B-E611-8228-0CC47A74527A.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/40BCF5D8-9D8B-E611-9A20-0025905B85FE.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/40CA5D53-AD86-E611-A88D-6CC2173D6E60.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/421DD838-038B-E611-9284-003048FFCC16.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/42AB32DF-F68A-E611-A87D-0CC47A4D765E.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/4487314B-9E8B-E611-92DB-003048FFCBB8.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/4499315A-CA89-E611-911A-FA163E4CDD79.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/44CB3044-588B-E611-8C9E-002590D9D9FC.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/46341D8E-A489-E611-84A2-0025905AA9CC.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/467B7BF3-B58B-E611-8751-008CFA111358.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/46C9E140-C188-E611-96A5-00259073E488.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/46D3D46C-188B-E611-B329-008CFA197C04.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/4ACB002E-D684-E611-B981-D8D385FF1940.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/4C1D4672-D98A-E611-BA5E-0242AC130002.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/4C62E568-848C-E611-942C-0CC47AA989CA.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/4E03061E-BA88-E611-A268-00215E2EAF44.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/4EBEC625-C086-E611-BD2E-842B2B76832A.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/50C0993A-FB87-E611-84F8-0025901AFEA2.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/52117F8E-B68B-E611-8FC5-0242AC130002.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/523D4673-4787-E611-9320-02163E015EA0.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/54297CC1-BE84-E611-A8DB-0002C94D54F8.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/54E85584-B68B-E611-84C1-0242AC130005.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/583860B7-C58B-E611-983A-00259029E714.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/583F03B7-768B-E611-8C9C-0025905B8580.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/5A44424F-C086-E611-A3C1-00259021A39E.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/5CAE8941-D189-E611-BBD3-0025905B85D2.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/5CF00269-988A-E611-A8AE-0025905C5488.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/5EE650FF-0B8B-E611-BB09-008CFA111188.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/624326D2-A78B-E611-A752-0CC47A7C349C.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/62D7E845-CC88-E611-AFFB-0025905A605E.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/62EDDD8C-AF8A-E611-AE38-00237DF244D8.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/644812FF-A08B-E611-A398-0242AC130004.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/64760DC1-248B-E611-846E-0CC47A7C35D2.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/648D50BC-988A-E611-A90C-02163E00C916.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/660128AA-A28B-E611-A52B-003048FFD75A.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/669953B8-768B-E611-9023-0025905A60D6.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/669C4445-3B87-E611-B423-7CD30AB7F7D8.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/66FF8B2B-4C8B-E611-9F2D-0025905B860E.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/68C5E87D-348B-E611-9443-0CC47A57CC42.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/6A0DA872-B98A-E611-A73A-901B0E542756.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/6A1BB65D-988B-E611-93CD-0CC47A4C8E7E.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/6CD24A3C-C988-E611-AB2D-008CFA197A28.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/6CD69010-C68B-E611-85C4-0025905A611C.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/6CD78C9F-9D8C-E611-A082-008CFA197BDC.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/6CF352B5-888B-E611-95A3-0242AC130005.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/6E804867-438B-E611-B213-002590D9D8B6.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/6ED5BCB3-FF8B-E611-9131-A0369F7F9170.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/6EFEE9A7-888B-E611-94AF-002590D9D956.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/7042F09E-B688-E611-98EF-0025905C2D98.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/70A7BFAF-DA88-E611-9FC4-0CC47A7E6A56.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/723909B4-0A8B-E611-8866-0CC47A4D76BE.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/7A1A2FD5-A78B-E611-954C-0CC47A7C361E.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/7A8EF89D-108B-E611-90F4-0025905B8610.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/7A9306C0-F183-E611-B805-A0369F301924.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/7AFC9746-418B-E611-8C18-0242AC130005.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/7C4098A9-158B-E611-A09E-0025905A607A.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/7C76882C-308B-E611-9F64-008CFA1111AC.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/7CC3357E-BB8B-E611-9E25-0CC47A6C183A.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/7CFEEE3C-3B8B-E611-A2F4-0025905B8566.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/7E786F77-0E8B-E611-ACDB-0CC47A4C8E70.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/7EF9A6D5-5B8B-E611-AF65-008CFA1113FC.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/803BB8EA-B98B-E611-A64E-0CC47A4C8E66.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/803C0EFB-758B-E611-8EDC-0242AC130004.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/8289D6BE-8988-E611-B588-FA163EA6A969.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/8832AA6E-B38B-E611-88B8-00259048AC10.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/8A1CA00C-EE8A-E611-A73F-008CFA1113B4.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/8AC2A1F9-F48A-E611-820F-0242AC130002.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/8E099119-B38B-E611-B6A1-0CC47A4C8EBA.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/8EEDC44B-238B-E611-A093-90B11C2AB44B.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/90128CF1-9E8A-E611-9E06-FA163ED7CD85.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/90C39B2A-638B-E611-8B8B-0025904A8ECE.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/9490DEDD-F08B-E611-B699-1CB72C1B64E2.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/94A611ED-A28B-E611-AE46-0025905A60B0.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/96007152-B98B-E611-AA75-002590D9D984.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/96698857-988B-E611-80C1-0CC47A4D769A.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/967F0905-1188-E611-82E2-0242AC130002.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/9832A9D0-D38B-E611-9A63-0090FAA59864.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/9C00778C-418B-E611-BDCB-0025905A605E.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/9EA0E2F3-D58B-E611-BFC4-3417EBE64BBE.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/9EF6D190-9D8C-E611-B2F3-0CC47A4C8ED8.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/A080CA51-C489-E611-BCA0-0CC47AA989C4.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/A230A692-8D88-E611-9927-B083FED07198.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/A28CB541-618B-E611-B32C-0CC47A4C8E1E.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/A2916D6A-588B-E611-9A38-008CFA1112E4.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/A46A6118-B38B-E611-B823-0CC47A7C347E.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/A63C6CB5-0A8B-E611-9DBC-0025905B8594.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/A6E8E041-FE85-E611-9D7A-001E67C9AF38.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/A874EBD7-A18B-E611-B9EB-008CFA111314.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/AC5C582A-5186-E611-A0B6-FA163ED9B7DF.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/ACC09648-7C8B-E611-A2BD-0025905A609A.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/ACFFE518-918B-E611-99AC-00259055C8D6.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/AE0958F0-0288-E611-83C3-0025905A6070.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/AE3826E8-D484-E611-8ABF-002481ACEA80.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/AECF8F6A-138C-E611-A0B8-00266CF94A4C.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/B06F3C99-B48B-E611-AA4B-0CC47A13CCEE.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/B0D2A07C-C688-E611-A7EB-6CC2173BC060.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/B0FB2503-768B-E611-8EAC-00259029E922.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/B40E5E4B-2A8B-E611-982C-0242AC130003.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/B44AD3B4-0A8B-E611-8745-0025905A6066.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/B47D58E4-9789-E611-913C-0CC47A1E0304.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/B62B1542-C884-E611-93B0-9CB654AEBE4A.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/B6357A34-EA88-E611-9D4C-0242AC130002.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/B65319E5-838B-E611-82DD-0025905A609A.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/B8B7FE4C-AD8B-E611-BC11-0CC47A0AD668.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/BA737253-4D8B-E611-A81B-008CFA197B1C.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/BA83A677-9F8A-E611-846D-00259048812E.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/BAF925C0-248B-E611-A5A4-0CC47A4D75F0.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/BC4229FD-758B-E611-93D8-002590E1E9B8.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/BCC11039-E88A-E611-9A8B-0CC47A4C8EE2.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/C06B192E-9B8B-E611-A1FF-002590D9D8C4.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/C091EE6F-7088-E611-A60F-FA163E4CF472.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/C0F7D906-C68B-E611-B04A-0025905BA736.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/C225D37F-E88A-E611-9D6E-90B11C27F383.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/C235F83F-C08B-E611-8A45-0CC47A4D75EC.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/C2472C15-8C8B-E611-BC3F-008CFA110C74.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/C2A62D8B-518B-E611-8C47-0242AC130005.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/C42E97AA-AD8A-E611-8138-180373FF8DE0.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/C49D07C3-B986-E611-B2F6-0CC47A7E68AA.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/C6263F1C-6588-E611-A021-0025905A60A6.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/C66F6627-558B-E611-BE1E-008CFA197E0C.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/C6CA41F7-F48A-E611-9E98-002590491AE4.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/C6F6A7C3-FE86-E611-975F-02163E015142.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/C80C8872-358B-E611-A309-0242AC130003.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/CA484B77-348B-E611-A771-00259048B920.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/CC8E9B54-E889-E611-AACF-001E67792888.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/CCFF6323-C086-E611-9E93-1CB72C1B64E2.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/CE47D131-1E8B-E611-8F1A-003048FFD7A4.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/CEA6D293-518B-E611-B9FB-0242AC130002.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/CEEB1533-078B-E611-B24B-0CC47A57D086.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/D00B97A1-408B-E611-908C-003048F5B2B4.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/D0134FE3-B68B-E611-BE1F-008CFA197E8C.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/D03A4448-D488-E611-ADB3-001EC9ADFC39.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/D0E5B6E0-B389-E611-9587-7845C4FC3668.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/D2268B85-AC89-E611-A0A8-001E67FA423F.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/D2C6E937-3B8B-E611-94E9-0CC47A78A30E.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/D41363E1-598C-E611-BEEA-14187734413C.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/D41478C8-CB8B-E611-98EB-20CF3019DF10.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/D65F5AE5-438B-E611-BF56-0CC47A7C357A.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/D84F676E-E589-E611-91AC-002590551F7E.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/D8ACFD8D-588B-E611-BE50-0025905B85CC.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/DAC7F874-228B-E611-85E1-0CC47A57D036.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/DC145679-1B8C-E611-8D10-44A842CF05B2.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/DE914681-958B-E611-84D9-008CFA11113C.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/DECD7D0B-838C-E611-9B78-0242AC130002.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/E01DF730-078B-E611-AAC6-0CC47A6C0682.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/E071F4E0-828B-E611-9944-0025905A612A.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/E221CED1-158B-E611-8FF9-0242AC130003.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/E222BED5-A78B-E611-AE00-0CC47A4D769A.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/E226B8FA-9D8B-E611-92AE-0025905A6084.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/E8582FA7-158B-E611-9324-0025905A609A.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/E87B341E-728A-E611-A047-002590D601B8.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/EA39B08C-3086-E611-966D-FA163ECEC41E.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/EAC7B6D5-A78B-E611-90CB-0CC47A4D764A.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/EC825100-A38B-E611-AEEB-0CC47A4D76AA.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/ECC289D5-5E8C-E611-BFF8-FA163EE7F932.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/EE43F5C2-248B-E611-B956-0025905A6136.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/EE881CAC-108B-E611-B58A-A0369F6369D2.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/F00827C1-508B-E611-8509-90B11C27F101.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/F0883EDC-618B-E611-9C5E-0242AC130003.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/F213FCA6-158B-E611-899E-0025905B8610.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/F237E9FD-A28B-E611-B60F-0025905A6090.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/F2527B12-9389-E611-8FA0-ECB1D79E5C40.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/F2B24D63-B38B-E611-9990-0025907DE22C.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/F2BB057A-0E8B-E611-9F27-0025905B8596.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/F2E51AEB-8888-E611-8FB1-008CFA001B18.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/F4177F0C-B38B-E611-858F-0CC47A78A360.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/F660D63B-9D89-E611-8A4D-FA163ED13B1A.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/F692DFDD-B386-E611-9634-00215E2EB454.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/F80F99CB-158B-E611-87B9-00238BBD75D6.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/F84C5CE9-6A8B-E611-B242-0CC47A4C8ECA.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/F8A362D6-A78B-E611-9415-0CC47A78A4B8.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/FA44FBDD-F68A-E611-B1AF-0CC47A4D766C.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/FA95D3A6-D28A-E611-B0AA-549F35AE4FE3.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/FAE5972E-9A86-E611-B547-F04DA275C2FB.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/FCEA8C0D-A18B-E611-8696-00259029E71C.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/FE073FD8-E68B-E611-A81B-0025905A6076.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/FE30BB78-8B88-E611-9D86-6CC2173C3DD0.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/70000/FEF23FFC-E487-E611-9803-0242AC130006.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/80000/28FD0789-4A8F-E611-AA10-0025905B8612.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/80000/6458F2A7-4A8F-E611-93CD-0CC47A78A3D8.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/80000/6472E2A7-4A8F-E611-AE83-0CC47A4C8E5E.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/80000/8EDE0E7C-4A8F-E611-8D3F-0025905A60DE.root',
       '/store/data/Run2016C/MET/MINIAOD/23Sep2016-v1/80000/AA90367C-4A8F-E611-AAA4-0CC47A4C8E34.root',
] )
