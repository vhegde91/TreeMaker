import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/0044FF4D-EBEA-E611-8431-0090FAA57260.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/028C1750-EBEA-E611-84BA-0090FAA58D84.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/04362B4F-EBEA-E611-BD32-0090FAA57AA0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/04DFBCB7-93EA-E611-A9E2-002590D0AF54.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/06264B40-24EB-E611-9617-0090FAA58114.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/06A0BE78-0DEB-E611-B844-0090FAA587C4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/0A04FFF7-EAEA-E611-9AB7-0090FAA58294.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/0A20BF37-24EB-E611-B4BB-0090FAA588B4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/0AA48F12-A0EA-E611-93B6-485B3989725C.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/0E0F2F29-CFEB-E611-826D-0090FAA57A60.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/0E17FC70-EFEA-E611-B082-0090FAA57E84.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/0E51BA4F-EBEA-E611-8801-0090FAA583C4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/0E851944-72EB-E611-B262-0090FAA588B4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/12F7D34F-EBEA-E611-8FEB-002590D0AFCC.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/14705850-EBEA-E611-87D3-0025907B4FAE.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/14834931-A7EA-E611-9D2E-00259073E322.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/16D0B1C2-1CEB-E611-8182-002590747E28.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/16ED6A30-A7EA-E611-A597-00259073E496.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/188AE445-92EA-E611-BB24-0090FAA58484.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/18A96B8C-EBEA-E611-85F1-00259073E4BC.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/1A6531B6-93EA-E611-A159-0090FAA57D64.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/1AA01934-24EB-E611-960B-0090FAA57690.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/1AA4FC11-14EB-E611-8F62-0090FAA58114.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/1CAFA003-EAEA-E611-A15A-0090FAA57E84.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/1CD83E0F-35EB-E611-8445-0090FAA57420.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/1E647905-EAEA-E611-8D51-0025907B4FC2.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/1E94CD03-EAEA-E611-84C7-0090FAA57E84.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/1E94E22C-A7EA-E611-99B1-0090FAA57380.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/1EB40716-9BEB-E611-BDD3-0090FAA57420.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/20726A04-EAEA-E611-A801-0090FAA58864.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/224412F5-B8EB-E611-8A81-0090FAA597B4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/226750E4-A9EB-E611-A5D9-0090FAA57F34.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/22A85A12-95EB-E611-AD9C-00259073E44E.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/22B9632D-A7EA-E611-B8FA-0090FAA59D74.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/22FD82CF-E7EA-E611-8891-0090FAA583F4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/24A75537-24EB-E611-8F5A-00259074AEAE.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/24C43684-06EB-E611-98C8-00259073E470.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/268FD406-14EB-E611-8A1C-0090FAA58974.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/26B69D4E-EBEA-E611-8D56-0090FAA583F4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/26F46D05-EAEA-E611-9CC9-0025907B4FC2.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/286DE404-EAEA-E611-8E80-0090FAA57D64.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/28935281-06EB-E611-A818-20CF30561726.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/289CA731-76EA-E611-886C-0090FAA57660.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/28A75615-9BEB-E611-91D0-0090FAA57260.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/28EADC62-99EA-E611-9ED6-00259073E380.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/2A8A4C60-99EA-E611-8AB0-0090FAA57C74.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/2C3673D7-47EB-E611-94AC-20CF305616EC.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/2E3CF97A-52EB-E611-B243-00259073E4FC.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/2EBD3234-ADEA-E611-B93E-00259073E34A.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/30CDC092-6DEA-E611-82E2-0090FAA579F0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/32893A64-EBEA-E611-93EB-0090FAA58544.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/32B8204F-EBEA-E611-A65F-0090FAA597B4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/32E72C06-EAEA-E611-A6ED-20CF3027A62F.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/3630A1BC-1CEB-E611-9EB6-0090FAA573F0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/3684270F-95EB-E611-8407-002590D0AF64.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/36F1E205-EAEA-E611-BB78-20CF305B04E3.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/36FAB22F-C8EB-E611-B237-485B39897219.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/38715D04-EAEA-E611-A410-0090FAA576C0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/3A19AE0D-EBEA-E611-BBC2-0090FAA59124.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/3A21AF4F-EBEA-E611-9E3C-0CC47A4DED2A.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/3CDD94E4-FDEA-E611-81FC-0090FAA597B4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/3E94C507-14EB-E611-92F7-0090FAA572C0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/4010B4D2-D6EB-E611-846B-0090FAA57BF0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/40C77303-EAEA-E611-829C-0090FAA58224.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/420F6454-EBEA-E611-B6AE-002590D0B038.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/44195052-EBEA-E611-976E-002590D6009C.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/44BBA70D-95EB-E611-8641-0090FAA572B0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/44F224D4-47EB-E611-9088-0090FAA57310.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/46CA567C-52EB-E611-8DCC-00259073E488.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/487A9404-EAEA-E611-BB2F-485B3989725B.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/48A35D11-A0EA-E611-A9E9-0090FAA57710.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/48E63614-EAEA-E611-B6AF-0025907B4F88.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/4EB519C5-2BEB-E611-93DA-0090FAA58974.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/500D684E-EBEA-E611-9131-0090FAA57E54.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/525834CC-2BEB-E611-B2DE-00259073E510.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/527F0A51-EBEA-E611-8C97-0090FAA58B64.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/52BD8F51-EBEA-E611-B4BD-0090FAA57310.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/540CE5F5-B8EB-E611-9501-0090FAA584B4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/54C48378-0DEB-E611-BC2F-0090FAA58274.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/54E00B59-5BEB-E611-A33A-00259073E34A.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/5678FEC7-83EA-E611-B832-0090FAA57BF0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/5A30FC30-A7EA-E611-B989-00259073E34A.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/5AC55DB2-3DEB-E611-8E4C-0090FAA57460.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/5C7AF50C-35EB-E611-B797-0090FAA58254.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/5CE17E06-14EB-E611-A049-0090FAA57430.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/5CF935C5-2BEB-E611-8072-0090FAA587C4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/5E3507EC-EBEA-E611-B2AF-485B39897264.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/604EBB05-EAEA-E611-B49F-20CF305B04E3.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/622F1A45-72EB-E611-91E0-0090FAA57AE0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/62DBDFD9-ADEA-E611-A251-0090FAA576C0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/64DBA75E-EBEA-E611-814C-002590D0B060.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/66267152-EBEA-E611-89B4-20CF305B0512.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/68521B15-9BEB-E611-8720-0090FAA57430.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/6A4CA647-92EA-E611-A116-0090FAA57CE4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/6AB580DE-7AEB-E611-AE0E-0090FAA58274.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/6C241050-EBEA-E611-8200-0090FAA59D74.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/6CD245BD-1CEB-E611-887A-0090FAA57CB4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/744CF078-52EB-E611-9A83-0090FAA576C0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/74EE3751-EBEA-E611-B392-0090FAA57430.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/7863670E-35EB-E611-B13D-0090FAA57410.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/7873474F-EBEA-E611-8EE9-0090FAA57AE0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/78A7E805-14EB-E611-ABD7-0090FAA57410.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/7A97EB34-AFEA-E611-9E0A-20CF305616EC.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/7C4EA330-A7EA-E611-98A1-00259073E412.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/7C69EF4D-EBEA-E611-A7BC-0090FAA57260.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/7CEFEDA7-C0EB-E611-958F-00259073E51A.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/82061946-67EB-E611-AEE6-485B3989725B.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/8225F0C7-2BEB-E611-AAC6-0090FAA58864.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/84266798-8BEB-E611-8B66-0090FAA58D04.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/8AFBDB55-5BEB-E611-9AC0-0090FAA57360.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/8CA0F204-EAEA-E611-91AD-0090FAA57D64.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/8CD885C5-1CEB-E611-B606-00259073E53E.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/8CFEA74F-EBEA-E611-9067-0090FAA57420.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/8E1E5405-EAEA-E611-8763-0090FAA57D64.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/8E994150-EBEA-E611-BB1B-0090FAA58274.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/8EF25A43-67EB-E611-8CB2-0090FAA58D64.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/9228E66E-94EB-E611-A9F4-0090FA9DFD8A.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/94423F9A-6DEA-E611-AA6F-0090FAA572B0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/96D9DD5E-99EA-E611-A006-0090FAA57B40.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/96FF0F61-99EA-E611-BE57-485B3989725C.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/98F5D4DF-7AEB-E611-92EC-0090FAA59124.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/9A40A6E2-A9EB-E611-8AE0-0090FAA58754.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/9C9CF899-F7EA-E611-BC15-002590D0B038.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/9E4745CB-2BEB-E611-BD88-0090FAA59184.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/9E785E2E-A7EA-E611-9FB4-0090FAA58484.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/9E7C8FD5-47EB-E611-AC31-002590D0AF54.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/9ECF72C5-2BEB-E611-B5E9-0090FAA587C4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/A053D74D-EBEA-E611-86C1-0090FAA57260.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/A6EE15B2-3DEB-E611-AC0C-00259073E51A.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/A6FEDD05-EAEA-E611-916F-20CF3027A62F.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/A8098951-EBEA-E611-993D-00248CB3209C.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/A8A1557A-0DEB-E611-8D09-00259073E4FC.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/A8F32938-24EB-E611-A345-0090FAA573F0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/AA5C099A-8BEB-E611-BA4C-0090FAA57AE0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/AC019F56-5BEB-E611-AB7C-0090FAA57AE0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/AC8B922E-A7EA-E611-95C3-0090FAA57660.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/ACB623D6-47EB-E611-923E-0090FAA59124.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/B00AB905-EAEA-E611-A3C3-20CF3027A62F.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/B0E7FE05-EAEA-E611-A686-20CF305B04E3.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/B40188C7-2BEB-E611-854A-0090FAA57690.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/B4A3CE02-EAEA-E611-9768-0090FAA57380.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/B67821D5-47EB-E611-94A5-002590D0AFEC.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/BAD5C117-A0EA-E611-943E-00259073E4B6.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/BADE37A4-A2EB-E611-9C26-0090FAA58B94.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/BC3CC050-EBEA-E611-83BF-0CC47A4DEF50.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/BEFB23B1-3DEB-E611-A8E8-0090FAA58C54.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/C05210C4-1CEB-E611-9E9A-00259073E3F2.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/C0807A32-76EA-E611-BFED-0090FAA57E54.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/C0B0295D-99EA-E611-A57B-0090FAA58484.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/C213D215-9BEB-E611-BD78-0090FAA57420.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/C2745B18-95EB-E611-9AD9-0090FAA57350.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/C2E19138-AFEA-E611-8ECB-00259073E34A.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/C60EAE0E-A0EA-E611-868F-0090FAA58484.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/C6731A05-14EB-E611-A934-0090FAA578F0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/C68068B4-B8EB-E611-A360-0090FAA57E94.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/C6815652-EBEA-E611-AD97-0025907B5048.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/C8767849-67EB-E611-A97C-00259073E3FC.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/CA07242B-A7EA-E611-B0CA-0090FAA58544.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/CA5BEE5E-EBEA-E611-BA9E-002590D0B060.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/CC0C0511-83EB-E611-82E2-0090FAA581F4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/CC102F44-72EB-E611-AD56-0CC47A4DEF00.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/CC453A14-EAEA-E611-9358-0025907B4F88.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/CC8E8036-24EB-E611-93FF-0090FAA58864.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/CE166A43-67EB-E611-BD97-0090FAA572C0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/D0C4C01D-EBEA-E611-859F-0090FAA57F24.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/D22F9C43-72EB-E611-872B-0090FAA58B64.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/D4695621-8BEA-E611-8FA4-0090FAA57660.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/D486914F-EBEA-E611-BC05-0090FAA58C54.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/D4FCA57A-0DEB-E611-8E31-00259073E4E2.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/D60BCF4E-EBEA-E611-8372-0090FAA597B4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/DA7FF62F-A7EA-E611-B76E-00259073E3AE.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/DC81AD04-EAEA-E611-9F16-485B3989725B.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/E436A5E1-ADEA-E611-97C2-00259073E4DA.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/E445A2A3-C0EB-E611-A863-0090FAA57FA4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/E6C5FE05-EAEA-E611-ABDA-20CF3027A62F.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/E6F52012-A0EA-E611-8BD0-0090FAA57710.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/E8684834-AFEA-E611-A522-0090FAA578E0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/E8CCAD3B-24EB-E611-AD78-0090FAA57EA4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/E8E05D51-EBEA-E611-903C-0090FAA58B64.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/EA058736-24EB-E611-AFE3-0090FAA576C0.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/EA2995A3-C0EB-E611-8464-0090FAA56F60.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/EA680F7B-0DEB-E611-9C4C-00259077501E.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/EACA64BE-1CEB-E611-86DE-0025907B4FA4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/EC6A2515-A0EA-E611-9BEE-0090FAA57490.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/EC7018A5-C0EB-E611-92D7-0090FAA58B94.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/EE60A101-EAEA-E611-98DE-0090FAA57CE4.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/EE9A2D53-EBEA-E611-991B-00259073E398.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/F2102700-B1EB-E611-B8B7-0090FAA58C54.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/F4238346-72EB-E611-B1A7-0090FAA57690.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/F48785BA-93EA-E611-A661-00259073E4DA.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/F8F4B900-B1EB-E611-86BA-0090FAA58D64.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/FA663EF1-A0EA-E611-B7DE-0090FAA59D74.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/FC84DF99-8BEB-E611-AEB5-0090FAA58D34.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/FCBACBBE-1CEB-E611-9C23-0090FAA57D64.root',
       '/store/data/Run2016C/HTMHT/MINIAOD/03Feb2017-v1/110000/FE298148-67EB-E611-A832-00259073E500.root',
] )
