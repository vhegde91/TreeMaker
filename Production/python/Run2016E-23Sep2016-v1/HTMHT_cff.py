import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/0A95B873-D68E-E611-996B-0CC47A7C34A0.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/0AA70A05-AD90-E611-A7F1-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/0E73F649-EF8E-E611-A6DF-0025905A48FC.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/124AB77D-DE8E-E611-993B-0CC47A7C354A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/14E2E52B-FE8E-E611-A5FF-002618FDA21D.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/20475E89-E98E-E611-A96E-0CC47A78A2F6.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/2409E275-D68E-E611-A833-0025905B855C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/26B30FBA-AC90-E611-B439-0CC47A4D762E.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/283B87A5-E98E-E611-9517-0025905A608A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/34F3C270-F18E-E611-8D43-0025905A60DE.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/38A43897-5692-E611-8B8C-0025905B85EE.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/3ACF41D0-E08E-E611-90B5-0CC47A4D767E.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/3C8EE74B-D68E-E611-BB70-0242AC130003.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/3EE5D527-FE8E-E611-8D11-0025905A6134.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/46D66925-FB8E-E611-A3A2-0025905A60E0.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/48011E41-E58E-E611-B4DF-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/4C4C532F-DB8F-E611-B9B8-0CC47A4D75F8.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/4CBD1AE3-E08E-E611-BD20-0025905B85B6.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/4EA95D16-FF8E-E611-BB9A-0025905504C8.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/50722A40-D98E-E611-BCFD-0CC47A4D76C0.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/5E26C8BA-AC90-E611-B661-0CC47A78A3EE.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/623455C8-108F-E611-94A9-0CC47A6C1874.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/624D0342-C18E-E611-B8A4-0242AC130005.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/66EC9C80-EB8E-E611-867B-0CC47A4D7614.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/6ABA2DA4-E28E-E611-B4C5-0CC47A4D764A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/723D1DD2-BA90-E611-AB73-0025901D0C68.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/7417E35C-E58E-E611-A2E2-0CC47A78A436.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/8225DAC5-5692-E611-9472-0025905B856C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/841F6EE6-CB8F-E611-805B-008CFA110C94.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/8E7B619B-5692-E611-86F9-0CC47A4D75F2.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/9CABEBAC-F38E-E611-BD23-0025905A6134.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/A41C6446-F08E-E611-A544-0CC47A4D7604.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/A4852F12-AA8E-E611-B071-0CC47AA98B8C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/A4A40F30-F68E-E611-8B49-0025905B8566.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/A637691A-098F-E611-8CF0-0025905B857E.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/AA6FE43E-E78E-E611-8449-0025905B85A2.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/AE15D818-028E-E611-AABB-0025905B8594.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/AE7B7548-E78E-E611-A424-0CC47A4C8E1C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/B2543959-E58E-E611-B5EA-0CC47A74524E.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/B288F853-E48D-E611-AC5D-002618FDA265.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/B4B671E0-028F-E611-BC02-0025905A6138.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/BC4FE978-DE8E-E611-96EF-0CC47A4D764A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/BE192479-338D-E611-BC68-0CC47A78A3F4.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/CA1A4FA7-E08D-E611-8866-002590574558.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/CC729BAE-B08D-E611-BF68-0CC47A6C1866.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/CCC600B9-C28F-E611-A67F-0242AC130003.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/CE063925-168D-E611-881B-0CC47A78A3EE.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/D0636FBC-FB8E-E611-A98C-0242AC130004.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/D4A02249-078F-E611-926E-0CC47A4D760A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/DC414FAA-F38E-E611-931A-0CC47A4C8E14.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/E0093602-EE8E-E611-BBFA-0CC47A78A418.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/E0E17781-EB8E-E611-B586-0CC47A7C3412.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/E45D4FFE-D98F-E611-B213-0025905A610A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/E6A8CD9C-A98D-E611-A086-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/EE1F2A01-E18E-E611-84BD-0CC47A13D0F2.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/F48829F4-108F-E611-B467-0025905B8612.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/F6498AD9-028F-E611-AA75-0CC47A4C8E82.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/F6CCE7B6-DB8E-E611-BD33-0CC47A78A3E8.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/FA05B899-0E8F-E611-9BED-0CC47A7C3404.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/50000/FC24C218-FB8E-E611-B999-0025905A611C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/0A9005D8-F28E-E611-B560-00259056F3D4.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/0E1469C9-BC8D-E611-B56E-0025907253E0.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/10437096-4E8D-E611-9281-0242AC130003.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/108BD459-D38E-E611-8559-008CFA1974DC.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/10FA1853-D18E-E611-8D78-0CC47A4C8EB6.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/14E14E6C-C98E-E611-98E4-008CFA19746C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/16EF3493-8E8E-E611-AF68-0025905A60E4.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/1E514D19-A48E-E611-8620-0025905A6060.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/2A3EC798-B18E-E611-B6F6-0025905A48BC.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/2A8EFEA1-B28E-E611-AC97-0CC47A4C8E3C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/2C49409A-AC8E-E611-9974-008CFA11113C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/30476285-938E-E611-BD59-0CC47A13CD44.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/327FC10E-A38E-E611-ABEB-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/34AD3D7B-9E8E-E611-94B9-90B11C1DBFB4.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/34BEE514-E78E-E611-9B91-0242AC130005.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/3A6E0E0E-D28F-E611-AE7E-0CC47A4D7670.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/42D948F3-9F8E-E611-B1DD-0CC47A7C3636.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/46ADD46D-A88E-E611-B198-0CC47A7C34C4.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/501EBE15-A18E-E611-8DA4-0CC47A4D764A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/50877F56-D18E-E611-BDBD-0025905A6092.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/5A6F6623-C78E-E611-934B-0242AC130004.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/5C2E889F-7C8E-E611-8BE3-0025907253C6.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/5CD4A856-D18E-E611-B826-0CC47A4D7630.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/627EEBF0-948E-E611-9D5F-0025905A611E.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/6412A639-A68E-E611-BA05-008CFA197B74.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/64B53425-9D8E-E611-B400-0CC47A7C3636.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/6AF7FB61-BF8E-E611-A9D9-0025904897C2.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/6E6B97A9-FF8E-E611-95E5-001C23BED42C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/70904319-8990-E611-B5F6-008CFA111358.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/70C0297E-EC8E-E611-B340-0CC47A4C8E28.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/76932FC1-938E-E611-8478-0025905B8600.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/789F5B0E-D08E-E611-92E4-90B11C27F101.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/7C394514-CA8E-E611-9A59-008CFA1112C0.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/7E542B4B-9A8E-E611-A020-0CC47A4D762A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/7E5456F2-828D-E611-AAAB-008CFA11125C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/7E76D19B-868E-E611-8B45-0242AC130003.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/7E7EFDF0-7A8E-E611-A360-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/7EEB9E2E-A78E-E611-B92B-0025905A609A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/86E5238B-D28E-E611-A555-0025905A613C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/88419B30-408D-E611-BDFE-0CC47A4D7644.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/885DF77A-2B8F-E611-AE16-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/88F9CFE2-8B8E-E611-93A6-003048F5ADF0.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/8C5198D3-0A91-E611-A0BB-00304867FEAF.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/901A09BD-E58E-E611-89DB-00259048B754.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/9054BE44-B08E-E611-AF05-0242AC130003.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/907669D5-B18E-E611-BFDD-002590E3A0EE.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/9648FD53-BD8E-E611-BBB3-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/98571997-B18E-E611-A9B6-0CC47A78A4A0.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/98792CBB-8A8E-E611-8BAC-0CC47A7C35C8.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/9A2FCBFF-CB8E-E611-8664-008CFA1113FC.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/A017D610-048E-E611-A603-0025905A60C6.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/A8409C3F-B08E-E611-8241-008CFA110C8C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/B02DB3D1-CA8F-E611-A44A-0CC47A4D764C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/B260B79E-F68F-E611-A0F4-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/B62DA809-998E-E611-8450-00238BCE44F0.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/B67F0246-AF8F-E611-A9BE-00238BCE4522.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/BA80CA5A-C290-E611-8195-0242AC130004.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/BCD0AE8B-BB8F-E611-9133-008CFA111248.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/BEEAD639-4D8E-E611-8858-008CFA111268.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/C29196C1-AA8E-E611-A6B4-0025905A613C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/C2CF6AF3-0C8E-E611-9154-0CC47A7452D0.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/C84702F6-AD8E-E611-9A7B-0025904897C2.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/CA09345F-9A8E-E611-95D0-002590574922.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/CE4C1491-FF8E-E611-BF1C-0025905B8606.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/D034179B-268F-E611-A151-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/D444E628-A78E-E611-8C0B-0CC47A6C1402.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/DA0BE132-408D-E611-AA70-0025905B85A2.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/E426B4FE-988E-E611-97C8-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/EA96BC87-D28E-E611-BA20-0CC47A4D7634.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/EC39E5BE-4891-E611-8FCA-0025905B8596.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/ECB6C8A1-B28E-E611-AB98-0CC47A7C3628.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/EE3C93B4-AC8E-E611-AA93-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/F25C8786-868E-E611-89CC-0CC47AA98A32.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/F4DC17BE-AA8E-E611-8481-0CC47A7C3458.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/F6863CEF-128E-E611-A41C-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/F69BC4FA-C88E-E611-8FBF-0025905506BE.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/F6FA26B0-A78E-E611-B362-0242AC130005.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/F8282A5D-DB8E-E611-B50B-0242AC130003.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/F8DE8A07-0B8F-E611-AD6D-0CC47A4D7654.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/F8E06C86-858E-E611-9A7B-0CC47A4D7628.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/FA916489-D28E-E611-ABE8-0CC47A745298.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/70000/FADC6400-8E8E-E611-9F31-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/0034AE6D-EA8C-E611-9E2F-0CC47A78A414.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/0075E1AB-EC8C-E611-9136-0025905B8604.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/00947491-228D-E611-B6FD-0CC47A6C06C6.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/04DB0008-F38C-E611-A8A5-002590E3A212.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/060399D7-248D-E611-B7CD-0CC47A4D7618.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/08676EE6-D58C-E611-817B-0025905A6090.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/08B95015-368D-E611-8302-0CC47A4D7694.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/0A5C5417-368D-E611-A3AC-0CC47A4C8E56.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/0AF6B7F8-0B8D-E611-8BAB-0025905B85CC.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/0C629C00-258D-E611-A47F-0025905A60E4.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/0C89DA8B-DF8C-E611-BE84-0025904AC2C0.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/10D67958-FA8C-E611-B3DA-0CC47A4D76A0.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/12ECF941-508D-E611-961A-0CC47A78A436.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/149DB364-CB8C-E611-A231-008CFA197E84.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/1600B6D6-EC8C-E611-AD0A-003048FFD798.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/18E8C233-488D-E611-B850-0CC47A4C8EEA.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/1A75175E-4E8D-E611-88FF-0CC47A78A3EE.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/1A9DB28F-278D-E611-92C4-0CC47A78A468.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/1C1F2FF1-0B8D-E611-BB9B-008CFA197BD0.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/1CE737C5-208D-E611-85B4-0025901D08EA.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/1E115869-4E8D-E611-A98C-0242AC130004.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/1E74D59D-D08C-E611-9CAC-0025901D0C4E.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/1EBD0999-168D-E611-80DE-0CC47A4C8E3C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/203B0836-418D-E611-BFB0-008CFA197C68.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/20AB7181-0C8E-E611-A4C7-0CC47A4D7618.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/222D622C-F38C-E611-AFCE-0242AC130004.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/244A64DA-EC8C-E611-A635-008CFA1111D4.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/26E612E3-418D-E611-AD44-0CC47A7C35E0.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/287F9401-258D-E611-BE64-0025905B858E.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/28B03E8D-278D-E611-B0CC-0CC47A4C8F30.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/28CA0B0E-298D-E611-923D-0242AC130003.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/28F6854A-0F8D-E611-BB2F-0CC47A74525A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/2A61569D-CE8D-E611-80FE-0CC47A4D7644.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/2E5933BD-EA8C-E611-86A1-003048F5B2F0.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/2EBE5E8E-518D-E611-957A-008CFA110C78.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/30084881-338D-E611-AA42-008CFA197438.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/3837F53E-5A8D-E611-8FF5-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/3857D0A5-E98C-E611-9AE1-0242AC130004.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/387ADBB0-3C8D-E611-9833-0CC47A745298.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/3A9336F7-438D-E611-950E-0025905A6066.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/3A94E8FD-AD8C-E611-9969-0CC47A78A30E.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/3AA12D6D-2D8D-E611-9221-0025901D08D8.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/3CD12285-168D-E611-A466-0242AC130004.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/3EC77E2F-A58C-E611-95EE-0242AC130004.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/42691458-C88C-E611-9CCA-003048F7CC92.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/426D991E-0F8D-E611-B5EC-00238BBD7586.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/44552EA0-1D8D-E611-B0CB-0025905A6122.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/44D550B1-FB8C-E611-96C8-0025901D08D8.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/4624DD8B-168D-E611-92B0-0CC47A4D7694.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/4829545D-4E8D-E611-9EB6-0CC47A4C8E3C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/4883EB63-1A8D-E611-8BD3-008CFA5D2758.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/48FB3EAD-B58C-E611-BF58-002590E39D90.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/4A43C54F-F78C-E611-A1D8-0025905A613C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/4EE23210-358D-E611-BF0A-0025904AC2CA.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/502559E3-418D-E611-AF66-0CC47A4D768E.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/50622ABA-F88C-E611-81C2-0CC47A4D7662.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/52635545-C78C-E611-B7A1-0242AC130005.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/54668F6D-2D8D-E611-8720-008CFA56D64C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/5496C2AF-3C8D-E611-A67A-0CC47A78A3EE.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/5A380654-BC8C-E611-A390-0025905A6134.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/5AD8EB0F-B78C-E611-963E-0025904A91F6.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/5E0CF77E-1D8D-E611-B63B-0025905B85D2.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/604B8275-DD8C-E611-A980-0025905B8592.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/62EBC82B-6A8E-E611-ABA8-0CC47A13D2BE.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/64F3A97B-BD8C-E611-911F-0CC47A78A45A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/66861FBD-2A8D-E611-ADF2-0025901D08D2.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/6810C261-E98C-E611-83C2-0CC47A4D76D6.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/687E896A-468D-E611-A72D-0CC47A78A426.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/688B4248-168D-E611-B291-0CC47A7C3420.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/6C3BFFF4-078D-E611-BDDA-0CC47A4D764A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/6CF0B28F-278D-E611-8B62-0CC47A4C8E70.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/6E99B493-268D-E611-A9F7-0025905746AC.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/6EBE0221-D68C-E611-BA71-008CFA165F54.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/70942ADF-E08C-E611-9752-0CC47A13CEF4.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/72023977-F78C-E611-AFF3-0025905A60D6.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/743AB10B-D48C-E611-A8B5-0CC47AA98F9A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/74C75D34-0D8D-E611-B0A4-0242AC130003.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/762411E2-248D-E611-AE00-00259070E22A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/76FCF387-C48C-E611-B092-0242AC130006.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/7CA248D8-408D-E611-986E-00238BBD7678.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/7E5EAF99-EC8C-E611-9DC8-0CC47A13D3A8.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/7E8DC07E-CC8C-E611-8377-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/7EF0C32F-508D-E611-96BD-0CC47A4D75F6.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/80CD5134-488D-E611-A012-0CC47AA98F98.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/80D438A9-498D-E611-B08E-008CFA110C74.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/84137FB5-BE8C-E611-907D-0025904897C2.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/84AA697C-888E-E611-9A60-0CC47A78A4A6.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/84AB9CAD-C58C-E611-A4EA-0CC47A6C14C8.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/8826F35D-4E8D-E611-910C-0CC47A4C8E20.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/8AF5264C-CF8C-E611-9FE4-0CC47A7C340C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/8C5BB029-0F8D-E611-86C1-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/8C94BDC9-C98C-E611-B072-0CC47A4C8F0C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/8E52A036-E28C-E611-86DC-0CC47A4D76A2.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/8E9C7EB3-EC8C-E611-852E-0CC47A78A446.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/90117E3D-B58C-E611-A732-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/90904AB3-F88C-E611-9B49-0025905B8586.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/90DA2899-498D-E611-BA75-0025905488FC.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/92643DF9-438D-E611-BA6F-0025905A6056.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/92A66605-368D-E611-8887-0025905A6082.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/92C236CF-D58C-E611-9972-0CC47A4D7646.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/940ABB27-4A8D-E611-B664-B083FED046D9.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/98164767-468D-E611-9D4E-0CC47A78A4A0.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/98F37EFE-AE8C-E611-854E-0CC47A4D765A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/9C684BA9-278D-E611-9E45-0242AC130005.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/9E528C11-CF8C-E611-A3FC-0CC47A78A45A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/9E6CEA32-178D-E611-A86F-90B11C27E14D.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/9EE20D41-158D-E611-BB24-0025905B858E.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/A015ACC4-FF8C-E611-B10C-0CC47A6C06C6.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/A04EE376-0A8D-E611-AB55-0025905A612A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/A0909FCA-588D-E611-AECF-0CC47A4D769E.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/A46F2FFD-038D-E611-87BF-008CFA11134C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/A85F7B22-D68C-E611-ADEB-0242AC130004.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/A8F7668D-2D8D-E611-AC6E-003048FFD7CE.root',
] )
readFiles.extend( [
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/AA0766C8-048D-E611-AB79-0242AC130004.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/AA87F384-BD8C-E611-94E0-0025905B8574.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/AAC9705B-FA8C-E611-9215-0025905A60F4.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/AC59F61C-088D-E611-AA54-0242AC130003.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/ACCFD296-B48C-E611-A78C-0025905A609A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/ACDCCD02-AF8C-E611-BA37-0025905B8606.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/AE6F0808-888E-E611-B778-0025905A610A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/B01A4493-298D-E611-B744-002590574A20.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/B0F527F7-0B8D-E611-B618-0CC47A4D76A2.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/B8716B77-0A8D-E611-87BE-0025905B85D2.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/BAB32818-368D-E611-B20B-0025905A608C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/BAD2F77D-1E8D-E611-AE39-0CC47A4D765A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/BAFA8D5B-918D-E611-9E58-90B11C2AA16C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/BC57CB38-0E8D-E611-848E-002590E1E9B8.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/BC855859-DD8C-E611-99BC-0242AC130003.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/BCE8FEA4-B58C-E611-BFA8-0025905A606A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/BE60ACB7-838E-E611-BDE5-008CFA197444.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/C0476F84-168D-E611-8161-0CC47A13CEAC.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/C417EBA3-BB8C-E611-881D-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/C66838E6-E28C-E611-85FC-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/C8B8749E-C48C-E611-839B-003048FFCBB8.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/CAA64E0F-B78C-E611-AE58-0025901D08EA.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/CAB62807-6B8D-E611-945C-008CFA197E90.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/CC745EBC-2E8D-E611-A06C-0025905A60A6.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/CCC0A289-BD8C-E611-82A8-0025904A91F6.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/CE6C1E77-0A8D-E611-AA05-0025905A6094.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/CE95428F-EB8C-E611-A065-003048F5B2F0.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/CEA4297F-DD8C-E611-A219-0025905A60D0.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/D0291C36-488D-E611-AD17-0025905A60E4.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/D4C53E2D-488D-E611-86CE-0025905B85CC.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/DA8BDFE3-478D-E611-9B73-0025905B855A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/DCB61BF7-438D-E611-93C0-0025905A612E.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/DE41BAA6-1D8D-E611-AB3B-0CC47A4C8E8A.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/E04CA886-1F8D-E611-A844-008CFA19741C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/E2292D79-1E8D-E611-A107-008CFA197454.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/E2565F5C-FA8C-E611-8D27-0025905B8590.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/E27FB526-068D-E611-A25C-90B11C1DBFB4.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/E4275E58-3B8D-E611-873F-0242AC130004.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/E6A6EB94-228D-E611-8CA2-0CC47A4C8F30.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/E6CAFBA3-578D-E611-9DB5-0CC47A78A436.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/E81DC773-4E8D-E611-9E37-0242AC130003.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/E8F374A8-278D-E611-8055-0242AC130004.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/EA4B6136-4E8D-E611-A8B4-008CFA1111AC.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/EAEF998F-278D-E611-9F76-0CC47A4C8E98.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/ECEF0D7F-EA8C-E611-A0F6-003048FFCBB2.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/F08E52A9-968D-E611-8149-0CC47A4D7638.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/F28554EF-DD8C-E611-9B8B-0242AC130006.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/F465D66B-888E-E611-B875-0242AC130005.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/F6D92279-E28C-E611-880B-008CFA1113B4.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/F8518681-338D-E611-8EF1-0242AC130004.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/F8B98E5F-4E8D-E611-B933-0025905B8580.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/FA2B3EBB-2E8D-E611-A5C6-0CC47A78A30E.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/FA6D6814-0A8D-E611-9C28-0CC47A7C34D0.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/FA816DB4-3C8D-E611-93A6-0025905A60D6.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/FA833360-0F8D-E611-8C78-0CC47A4D763C.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/FC7CC4B9-2E8D-E611-895F-0CC47A78A340.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/FC9D3ED8-378E-E611-AF34-0242AC130002.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/FCCD1378-F88C-E611-8DED-0CC47A4C8EB0.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/FE147FD2-B68D-E611-9743-008CFA197928.root',
       '/store/data/Run2016E/HTMHT/MINIAOD/23Sep2016-v1/80000/FEFE74A0-3B8D-E611-8A75-0025905A6094.root',
] )
