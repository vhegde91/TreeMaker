from TreeMaker.WeightProducer.namedtuple_with_defaults import namedtuple_with_defaults
import re

class MCSampleHelper():
    """Helps to parse MC sample names and return specific pieces of information.

    The various functions are meant to make it easier to parse the many sample names without the duplication of effort.
    The pieces of information that can be returned are:
        1. The center of mass energy simulated within a given sample
        2. The center of mass energy associated to a given year
        3. The sample name when it's stripped of extraneous information
        4.The year associated to a given MiniAOD production

    Args:
        extra_dicts_energy (:obj:`dict` of :obj:`str`): Extra year-center of mass pairings not specified in the internal dictionary
        extra_dicts_strip (:obj:`dict` of :obj:`list` of :obj:`str`): Extra regular expressions used to strip non-physics process information from the MC sample name

    Example:
        from MCSampleValues import MCSampleHelper
        helper = MCSampleHelper()
        helper.get_cm_energy_by_year("2018")
    """

    __energy_dict = {
        "2010" : "7TeV",
        "2011" : "7TeV",
        "2012" : "8TeV",
        "2015" : "13TeV",
        "2016" : "13TeV",
        "2017" : "13TeV",
        "2018" : "13TeV",
    }

    __names_to_strip = {
        "generators"    : ["(.pythia)([^_-]*)","(.powheg)([^_-]*)","(.madgraph)([^_-]*)","(.madspin)([^_-]*)","(.amcatnlo)([^_-]*)"],
        "tunes"         : ["(.Tune)([^_]*)"],
        "added_info"    : ["(.PSweights)([^_]*)"],
        "other"         : ["(.NLO)([^_-]*)","^\s*(RelVal\s*)?|(\s*_13)?\s*$","step4_MINIAOD_2016_","step4_MINIAOD_","(.mDark)(.*)","(.isr|.fsr)(up|down)","([_|-]v)([0-9]*)","(.mWCutfix)","([_])(ttHtranche3)","SVJ_","_erdON","_ext([0-9])","_hdamp(UP|DOWN)"],
    }

    def __init__(self, extra_dicts_energy=None, extra_dicts_strip=None):
        if extra_dicts_energy is not None:
            for extra in extra_dicts_energy:
                self.__energy_dict.update(extra)
        if extra_dicts_strip is not None:
            for extra in extra_dicts_strip:
                self.__names_to_strip.update(extra)

    def get_cm_energy(self, name):
        energy_result = re.search("(_[0-9]*TeV)",name)
        # allow a default value
        energy = "_13TeV" if energy_result is None else energy_result.group(0)
        return (re.sub("(_[0-9]*TeV)","",name),energy)

    def get_cm_energy_by_year(self, year):
        return self.__energy_dict[year]

    def get_minimal_name(self, name):
        for category, values_to_strip in self.__names_to_strip.iteritems():
            for regex_value in values_to_strip:
                name = re.sub(regex_value,"",name)
        name, energy = self.get_cm_energy(name)
        return name

    def get_year(self, mcVersion):
        year_result = re.search("[0-9]*MiniAOD",mcVersion)
        year = "2016" if year_result is None else "20"+year_result.group(0).split("MiniAOD")[0]
        return year

class MCSampleValuesHelper():
    """Stores the cross sections and k-factors associated to a given physics process.

    The lists of years and energies used to identify a given cross section are also stored within this class.
    Given a process name, year, and energy the appropriate cross section will be returned.
    If a cross section is not specified for an energy (i.e. multiple years), then the cross section for a given year will be returned.

    Args:
        extra_dicts (:obj:`dict` of :obj:`dict` of :obj:`namedtuple_with_defaults`): Extra cross sections and k-factors to add to the __values_dict.

    Example:
        from TreeMaker.WeightProducer.MCSampleValues import MCSampleValuesHelper
        helper = MCSampleValuesHelper()
        helper.get_value("TTJets_SingleLeptFromT","13TeV","2016","CrossSection")
        helper.get_value("TTJets_SingleLeptFromT","13TeV","2016","kFactor")
        helper.get_value("TTJets_SingleLeptFromT","13TeV","2016","BranchingRatio")
        helper.get_value("TTJets_SingleLeptFromT_genMET-150","13TeV","2016","CrossSection")
        helper.get_value("TTJets_SingleLeptFromT_genMET-150","13TeV","2016","kFactor")
        helper.get_value("TTJets_SingleLeptFromT_genMET-150","13TeV","2016","BranchingRatio")
        helper.get_value("TTJets_SingleLeptFromT_genMET-150","13TeV","2017","CrossSection")
        helper.get_value("TTJets_SingleLeptFromT_genMET-150","13TeV","2017","kFactor")
        helper.get_value("TTJets_SingleLeptFromT_genMET-150","13TeV","2017","BranchingRatio")
    """

    __years = ['2010','2011','2012','2015','2016','2017','2018']
    __energies = ["7TeV","8TeV","13TeV"]
    __xs_field_names = []
    __br_field_names = []
    __kfactor_field_names = []
    __corr_field_names = []
    __key_field_map = {
        "CrossSection"   : ("XS",-1.0),
        "BranchingRatio" : ("BR",1.0),
        "kFactor"        : ("kFactor",1.0),
        "Correction"     : ("Corr",1.0),
    }
    for __val in __years+__energies:
        __xs_field_names.append('XS_'+__val)
        __xs_field_names.append('XSSource_'+__val)
        __br_field_names.append('BR_'+__val)
        __br_field_names.append('BRSource_'+__val)
        __kfactor_field_names.append('kFactor_'+__val)
        __kfactor_field_names.append('kFactorSource_'+__val)
        __corr_field_names.append('Corr_'+__val)
        __corr_field_names.append('CorrSource_'+__val)
    XSValues = namedtuple_with_defaults('XSValues', __xs_field_names, [__key_field_map["CrossSection"][1],""]*len(__years+__energies))
    BRValues = namedtuple_with_defaults('BRValues', __br_field_names, [__key_field_map["BranchingRatio"][1],""]*len(__years+__energies))
    kFactorValues = namedtuple_with_defaults('kFactorValues', __kfactor_field_names, [__key_field_map["kFactor"][1],""]*len(__years+__energies))
    CorrValues = namedtuple_with_defaults('CorrValues', __corr_field_names, [__key_field_map["Correction"][1],""]*len(__years+__energies))

    __values_dict = {
        "TTJets" : {
            "CrossSection" : XSValues(
                XS_13TeV=831.76, XSSource_13TeV="XSDB (NNLO)",
            ),
        },
        "TTJets_SingleLeptFromT" : {
            "CrossSection" : XSValues(
                XS_13TeV=831.8, XSSource_13TeV="PDG XS - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.219, BRSource_13TeV="PDG BR (t=tbar) - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"
            ),
        },
        "TTJets_SingleLeptFromTbar" : {
            "CrossSection" : XSValues(
                XS_13TeV=831.8, XSSource_13TeV="PDG XS - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.219, BRSource_13TeV="PDG BR (t=tbar) - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"
            ),
        },
        "TTJets_DiLept" : {
            "CrossSection" : XSValues(
                XS_13TeV=831.8, XSSource_13TeV="PDG XS - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.105, BRSource_13TeV="PDG BR (t=tbar) - http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf"
            ),
        },
        "TTJets_SingleLeptFromT_genMET-80" : {
            "CrossSection" : XSValues(
                XS_2018=32.23, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2018=1.677, kFactorSource_2018="XSDB NNLO/LO=831.76/496.1",
            ),
        },
        "TTJets_SingleLeptFromTbar_genMET-80" : {
            "CrossSection" : XSValues(
                XS_2018=31.78, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2018=1.677, kFactorSource_2018="XSDB NNLO/LO=831.76/496.1",
            ),
        },
        "TTJets_DiLept_genMET-80" : {
            "CrossSection" : XSValues(
                XS_2018=22.46, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2018=1.677, kFactorSource_2018="XSDB NNLO/LO=831.76/496.1",
            ),
        },
        "TTJets_SingleLeptFromT_genMET-150" : {
            "CrossSection" : XSValues(
                XS_2016=5.952, XSSource_2016="XSDB",
                XS_2017=6.196, XSSource_2017="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.627, kFactorSource_2016="XSDB NNLO/LO=831.76/511.3",
                kFactor_2017=1.679, kFactorSource_2017="XSDB/GenXSecAnalyzer NNLO/LO=831.76/495.3",
            ),
        },
        "TTJets_SingleLeptFromTbar_genMET-150" : {
            "CrossSection" : XSValues(
                XS_2016=5.952, XSSource_2016="XSDB",
                XS_2017=6.179, XSSource_2017="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.627, kFactorSource_2016="XSDB NNLO/LO=831.76/511.3",
                kFactor_2017=1.679, kFactorSource_2017="XSDB/GenXSecAnalyzer NNLO/LO=831.76/495.3",
            ),
        },
        "TTJets_DiLept_genMET-150" : {
            "CrossSection" : XSValues(
                XS_2016=3.638, XSSource_2016="XSDB",
                XS_2017=3.655, XSSource_2017="XSDB",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.627, kFactorSource_2016="XSDB NNLO/LO=831.76/511.3",
                kFactor_2017=1.679, kFactorSource_2017="XSDB/GenXSecAnalyzer NNLO/LO=831.76/495.3",
            ),
        },
        "TTJets_HT-600to800" : {
            "CrossSection" : XSValues(
                XS_2016=1.65, XSSource_2016="XSDB",
                XS_2017=1.821, XSSource_2017="XSDB",
                XS_2018=1.808, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.627, kFactorSource_2016="XSDB NNLO/LO=831.76/511.3",
                kFactor_2017=1.679, kFactorSource_2017="XSDB/GenXSecAnalyzer NNLO/LO=831.76/495.3",
                kFactor_2018=1.693, kFactorSource_2018="XSDB/GenXSecAnalyzer NNLO/LO=831.76/491.4",
            ),
        },
        "TTJets_HT-800to1200" : {
            "CrossSection" : XSValues(
                XS_2016=0.6736, XSSource_2016="XSDB",
                XS_2017=0.7532, XSSource_2017="XSDB",
                XS_2018=0.7490, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.627, kFactorSource_2016="XSDB NNLO/LO=831.76/511.3",
                kFactor_2017=1.679, kFactorSource_2017="XSDB/GenXSecAnalyzer NNLO/LO=831.76/495.3",
                kFactor_2018=1.693, kFactorSource_2018="XSDB/GenXSecAnalyzer NNLO/LO=831.76/491.4",
            ),
        },
        "TTJets_HT-1200to2500" : {
            "CrossSection" : XSValues(
                XS_2016=0.1194, XSSource_2016="XSDB",
                XS_2017=0.1313, XSSource_2017="GenXSecAnalyzer",
                XS_2018=0.1315, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.627, kFactorSource_2016="XSDB NNLO/LO=831.76/511.3",
                kFactor_2017=1.679, kFactorSource_2017="XSDB/GenXSecAnalyzer NNLO/LO=831.76/495.3",
                kFactor_2018=1.693, kFactorSource_2018="XSDB/GenXSecAnalyzer NNLO/LO=831.76/491.4",
            ),
        },
        "TTJets_HT-2500toInf" : {
            "CrossSection" : XSValues(
                XS_2016=0.001445, XSSource_2016="XSDB",
                XS_2017=0.001410, XSSource_2017="GenXSecAnalyzer",
                XS_2018=0.001420, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.627, kFactorSource_2016="XSDB NNLO/LO=831.76/511.3",
                kFactor_2017=1.679, kFactorSource_2017="XSDB/GenXSecAnalyzer NNLO/LO=831.76/495.3",
                kFactor_2018=1.693, kFactorSource_2018="XSDB/GenXSecAnalyzer NNLO/LO=831.76/491.4",
            ),
        },
        "TTTo2L2Nu" : {
            "CrossSection" : XSValues(
                XS_13TeV=88.29, XSSource_13TeV="XSDB (NNLO)",
            ),
        },
        "TTToHadronic" : {
            "CrossSection" : XSValues(
                XS_13TeV=377.96, XSSource_13TeV="XSDB (NNLO)",
            ),
        },
        "TTToSemiLeptonic" : {
            "CrossSection" : XSValues(
                XS_13TeV=365.34, XSSource_13TeV="XSDB (NNLO)",
            ),
        },
        "TTGamma_SingleLeptFromT" : {
            "CrossSection" : XSValues(
                XS_2016=0.7684, XSSource_2016="XSDB (NLO)",
                XS_2017=0.7040, XSSource_2017="XSDB (LO)",
                XS_2018=0.7053, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "TTGamma_SingleLeptFromTbar" : {
            "CrossSection" : XSValues(
                XS_2016=0.7659, XSSource_2016="XSDB (NLO)",
                XS_2017=0.7040, XSSource_2017="XSDB (LO)",
                XS_2018=0.7028, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "TTGamma_Dilept" : {
            "CrossSection" : XSValues(
                XS_2016=0.6343, XSSource_2016="XSDB (NLO)",
                XS_2017=0.5795, XSSource_2017="GenXSecAnalyzer",
                XS_2018=0.5799, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "WJetsToLNu_HT-70To100" : {
            "CrossSection" : XSValues(
                XS_2016=1353.0, XSSource_2016="XSDB (LO)",
                XS_2017=1292.0, XSSource_2017="XSDB (LO)",
                XS_2018=1292.0, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.224, kFactorSource_2016="XSDB NNLO/LO=61526.7/50260",
                kFactor_2017=1.162, kFactorSource_2017="XSDB NNLO/LO=61526.7/52940",
                kFactor_2018=1.164, kFactorSource_2018="XSDB NNLO/LO=61526.7/52850",
            ),
        },
        "WJetsToLNu_HT-100To200" : {
            "CrossSection" : XSValues(
                XS_2016=1346.0, XSSource_2016="XSDB (LO)",
                XS_2017=1395.0, XSSource_2017="XSDB (LO)",
                XS_2018=1393.0, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.224, kFactorSource_2016="XSDB NNLO/LO=61526.7/50260",
                kFactor_2017=1.162, kFactorSource_2017="XSDB NNLO/LO=61526.7/52940",
                kFactor_2018=1.164, kFactorSource_2018="XSDB NNLO/LO=61526.7/52850",
            ),
            "Correction" : CorrValues(
                Corr_2017=0.993, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=0.993, CorrSource_2018="Same as 2017",
            ),
        },
        "WJetsToLNu_HT-200To400" : {
            "CrossSection" : XSValues(
                XS_2016=360.1, XSSource_2016="XSDB (LO)",
                XS_2017=407.9, XSSource_2017="XSDB (LO)",
                XS_2018=409.9, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.224, kFactorSource_2016="XSDB NNLO/LO=61526.7/50260",
                kFactor_2017=1.162, kFactorSource_2017="XSDB NNLO/LO=61526.7/52940",
                kFactor_2018=1.164, kFactorSource_2018="XSDB NNLO/LO=61526.7/52850",
            ),
            "Correction" : CorrValues(
                Corr_2017=1.002, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=1.002, CorrSource_2018="Same as 2017",
            ),
        },
        "WJetsToLNu_HT-400To600" : {
            "CrossSection" : XSValues(
                XS_2016=48.8, XSSource_2016="XSDB (LO)",
                XS_2017=57.48, XSSource_2017="XSDB (LO)",
                XS_2018=57.80, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.224, kFactorSource_2016="XSDB NNLO/LO=61526.7/50260",
                kFactor_2017=1.162, kFactorSource_2017="XSDB NNLO/LO=61526.7/52940",
                kFactor_2018=1.164, kFactorSource_2018="XSDB NNLO/LO=61526.7/52850",
            ),
            "Correction" : CorrValues(
                Corr_2017=1.009, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=1.009, CorrSource_2018="Same as 2017",
            ),
        },
        "WJetsToLNu_HT-600To800" : {
            "CrossSection" : XSValues(
                XS_2016=12.07, XSSource_2016="XSDB (LO)",
                XS_2017=12.87, XSSource_2017="XSDB (LO)",
                XS_2018=12.94, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.224, kFactorSource_2016="XSDB NNLO/LO=61526.7/50260",
                kFactor_2017=1.162, kFactorSource_2017="XSDB NNLO/LO=61526.7/52940",
                kFactor_2018=1.164, kFactorSource_2018="XSDB NNLO/LO=61526.7/52850",
            ),
            "Correction" : CorrValues(
                Corr_2017=1.120, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=1.120, CorrSource_2018="Same as 2017",
            ),
        },
        "WJetsToLNu_HT-800To1200" : {
            "CrossSection" : XSValues(
                XS_2016=5.497, XSSource_2016="XSDB (LO)",
                XS_2017=5.366, XSSource_2017="XSDB (LO)",
                XS_2018=5.451, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.224, kFactorSource_2016="XSDB NNLO/LO=61526.7/50260",
                kFactor_2017=1.162, kFactorSource_2017="XSDB NNLO/LO=61526.7/52940",
                kFactor_2018=1.164, kFactorSource_2018="XSDB NNLO/LO=61526.7/52850",
            ),
            "Correction" : CorrValues(
                Corr_2017=1.202, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=1.202, CorrSource_2018="Same as 2017",
            ),
        },
        "WJetsToLNu_HT-1200To2500" : {
            "CrossSection" : XSValues(
                XS_2016=1.329, XSSource_2016="XSDB (LO)",
                XS_2017=1.074, XSSource_2017="XSDB (LO)",
                XS_2018=1.085, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.224, kFactorSource_2016="XSDB NNLO/LO=61526.7/50260",
                kFactor_2017=1.162, kFactorSource_2017="XSDB NNLO/LO=61526.7/52940",
                kFactor_2018=1.164, kFactorSource_2018="XSDB NNLO/LO=61526.7/52850",
            ),
            "Correction" : CorrValues(
                Corr_2017=1.332, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=1.332, CorrSource_2018="Same as 2017",
            ),
        },
        "WJetsToLNu_HT-2500ToInf" : {
            "CrossSection" : XSValues(
                XS_2016=0.03209, XSSource_2016="XSDB (LO)",
                XS_2017=0.008001, XSSource_2017="XSDB (LO)",
                XS_2018=0.008060, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.224, kFactorSource_2016="XSDB NNLO/LO=61526.7/50260",
                kFactor_2017=1.162, kFactorSource_2017="XSDB NNLO/LO=61526.7/52940",
                kFactor_2018=1.164, kFactorSource_2018="XSDB NNLO/LO=61526.7/52850",
            ),
            "Correction" : CorrValues(
                Corr_2017=4.200, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=4.200, CorrSource_2018="Same as 2017",
            ),
        },
        "WJetsToLNu" : {
            "CrossSection" : XSValues(
                XS_13TeV=61526.7, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#W_jets NNLO (60430.0 @ NLO)",
                XS_2016=50260.0, XSSource_2016="XSDB (LO)",
                XS_2017=52940.0, XSSource_2017="XSDB (LO)",
                XS_2018=52850.0, XSSource_2018="XSDB (LO)",
            ),
        },
        "WJetsToLNu_Wpt-0To50" : {
            "CrossSection" : XSValues(
                XS_2018=61850.0, XSSource_2018="XSDB (NLO)",
            ),
            "kFactor" : kFactorValues(
                kFactor_2018=0.929, kFactorSource_2018="XSDB NNLO/LO=61526.7/66231.2",
            ),
        },
        "WJetsToLNu_Pt-50To100" : {
            "CrossSection" : XSValues(
                XS_2018=3570.0, XSSource_2018="XSDB (NLO)",
            ),
            "kFactor" : kFactorValues(
                kFactor_2018=0.929, kFactorSource_2018="XSDB NNLO/LO=61526.7/66231.2",
            ),
        },
        "WJetsToLNu_Pt-100To250" : {
            "CrossSection" : XSValues(
                XS_2018=779.1, XSSource_2018="XSDB (NLO)",
            ),
            "kFactor" : kFactorValues(
                kFactor_2018=0.929, kFactorSource_2018="XSDB NNLO/LO=61526.7/66231.2",
            ),
        },
        "WJetsToLNu_Pt-250To400" : {
            "CrossSection" : XSValues(
                XS_2018=27.98, XSSource_2018="XSDB (NLO)",
            ),
            "kFactor" : kFactorValues(
                kFactor_2018=0.929, kFactorSource_2018="XSDB NNLO/LO=61526.7/66231.2",
            ),
        },
        "WJetsToLNu_Pt-400To600" : {
            "CrossSection" : XSValues(
                XS_2018=3.604, XSSource_2018="XSDB (NLO)",
            ),
            "kFactor" : kFactorValues(
                kFactor_2018=0.929, kFactorSource_2018="XSDB NNLO/LO=61526.7/66231.2",
            ),
        },
        "WJetsToLNu_Pt-600ToInf" : {
            "CrossSection" : XSValues(
                XS_2018=0.5545, XSSource_2018="XSDB (NLO)",
            ),
            "kFactor" : kFactorValues(
                kFactor_2018=0.929, kFactorSource_2018="XSDB NNLO/LO=61526.7/66231.2",
            ),
        },
        "WJetsToQQ_HT400to600_qc19_3j" : {
            "CrossSection" : XSValues(
                XS_2017=315.2, XSSource_2017="GenXSecAnalyzer",
                XS_2018=314.6, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "WJetsToQQ_HT600to800_qc19_3j" : {
            "CrossSection" : XSValues(
                XS_2017=68.61, XSSource_2017="GenXSecAnalyzer",
                XS_2018=68.58, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "WJetsToQQ_HT-800toInf_qc19_3j" : {
            "CrossSection" : XSValues(
                XS_2017=34.71, XSSource_2017="GenXSecAnalyzer",
                XS_2018=34.74, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "WJetsToQQ_HT-600ToInf" : {
            "CrossSection" : XSValues(
                XS_2016=99.65, XSSource_2016="XSDB (LO)"
            ),
        },
        "QCD_HT200to300" : {
            "CrossSection" : XSValues(
                XS_2016=1710000.0, XSSource_2016="XSDB (LO)",
                XS_2017=1547000.0, XSSource_2017="XSDB (LO)",
                XS_2018=1557000.0, XSSource_2018="XSDB (LO)",
            ),
        },
        "QCD_HT300to500" : {
            "CrossSection" : XSValues(
                XS_2016=347500.0, XSSource_2016="XSDB (LO)",
                XS_2017=322600.0, XSSource_2017="XSDB (LO)",
                XS_2018=323400.0, XSSource_2018="XSDB (LO)",
            ),
        },
        "QCD_HT500to700" : {
            "CrossSection" : XSValues(
                XS_2016=32060.0, XSSource_2016="XSDB (LO)",
                XS_2017=29980.0, XSSource_2017="XSDB (LO)",
                XS_2018=30140.0, XSSource_2018="XSDB (LO)",
            ),
        },
        "QCD_HT700to1000" : {
            "CrossSection" : XSValues(
                XS_2016=6829.0, XSSource_2016="XSDB (LO)",
                XS_2017=6334.0, XSSource_2017="XSDB (LO)",
                XS_2018=6310.0, XSSource_2018="XSDB (LO)",
            ),
        },
        "QCD_HT1000to1500" : {
            "CrossSection" : XSValues(
                XS_2016=1207.0, XSSource_2016="XSDB (LO)",
                XS_2017=1088.0, XSSource_2017="XSDB (LO)",
                XS_2018=1094.0, XSSource_2018="XSDB (LO)",
            ),
        },
        "QCD_HT1500to2000" : {
            "CrossSection" : XSValues(
                XS_2016=120.0, XSSource_2016="XSDB (LO)",
                XS_2017=99.11, XSSource_2017="XSDB (LO)",
                XS_2018=99.38, XSSource_2018="XSDB (LO)",
            ),
        },
        "QCD_HT2000toInf" : {
            "CrossSection" : XSValues(
                XS_2016=25.25, XSSource_2016="XSDB (LO)",
                XS_2017=20.23, XSSource_2017="XSDB (LO)",
                XS_2018=20.20, XSSource_2018="XSDB (LO)",
            ),
        },
        "QCD_Pt-15to20_MuEnrichedPt5" : {
            "CrossSection" : XSValues(
                XS_2016=3616000, XSSource_2016="XSDB",
                XS_2017=2799000, XSSource_2017="XSDB",
                XS_2018=2812000, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "QCD_Pt-20to30_MuEnrichedPt5" : {
            "CrossSection" : XSValues(
                XS_2016=3160000, XSSource_2016="XSDB",
                XS_2017=2526000, XSSource_2017="XSDB",
                XS_2018=2531000, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "QCD_Pt-30to50_MuEnrichedPt5" : {
            "CrossSection" : XSValues(
                XS_2016=1650000, XSSource_2016="GenXSecAnalyzer",
                XS_2017=1362000, XSSource_2017="XSDB",
                XS_2018=1367000, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "QCD_Pt-50to80_MuEnrichedPt5" : {
            "CrossSection" : XSValues(
                XS_2016=448300, XSSource_2016="GenXSecAnalyzer",
                XS_2017=376600, XSSource_2017="XSDB",
                XS_2018=378000, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "QCD_Pt-80to120_MuEnrichedPt5" : {
            "CrossSection" : XSValues(
                XS_2016=105200, XSSource_2016="GenXSecAnalyzer",
                XS_2017=88930,  XSSource_2017="XSDB",
                XS_2018=88600,  XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "QCD_Pt-120to170_MuEnrichedPt5" : {
            "CrossSection" : XSValues(
                XS_2016=25470, XSSource_2016="GenXSecAnalyzer",
                XS_2017=21230, XSSource_2017="XSDB",
                XS_2018=21190, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "QCD_Pt-170to300_MuEnrichedPt5" : {
            "CrossSection" : XSValues(
                XS_2016=8635, XSSource_2016="GenXSecAnalyzer",
                XS_2017=7055, XSSource_2017="XSDB",
                XS_2018=7025, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "QCD_Pt-300to470_MuEnrichedPt5" : {
            "CrossSection" : XSValues(
                XS_2016=797.3, XSSource_2016="GenXSecAnalyzer",
                XS_2017=619.8, XSSource_2017="GenXSecAnalyzer",
                XS_2018=620.6, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "QCD_Pt-470to600_MuEnrichedPt5" : {
            "CrossSection" : XSValues(
                XS_2016=79.25, XSSource_2016="GenXSecAnalyzer",
                XS_2017=59.24, XSSource_2017="XSDB",
                XS_2018=59.06, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "QCD_Pt-600to800_MuEnrichedPt5" : {
            "CrossSection" : XSValues(
                XS_2016=25.25, XSSource_2016="XSDB",
                XS_2017=18.18, XSSource_2017="GenXSecAnalyzer",
                XS_2018=18.21, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "QCD_Pt-800to1000_MuEnrichedPt5" : {
            "CrossSection" : XSValues(
                XS_2016=4.723, XSSource_2016="XSDB",
                XS_2017=3.277, XSSource_2017="GenXSecAnalyzer",
                XS_2018=3.276, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "QCD_Pt-1000toInf_MuEnrichedPt5" : {
            "CrossSection" : XSValues(
                XS_2016=1.613, XSSource_2016="XSDB",
                XS_2017=1.079, XSSource_2017="GenXSecAnalyzer",
                XS_2018=1.079, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "QCD_Pt-15to7000_Flat" : {
            "CrossSection" : XSValues(
                XS_2016=1976000000.0, XSSource_2016="XSDB",
                XS_2017=1370000000.0, XSSource_2017="XSDB",
                XS_2018=1371000000.0, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "QCD_Pt-15to7000_FlatP6" : {
            "CrossSection" : XSValues(
                XS_2016=1973000000.0, XSSource_2016="XSDB",
            ),
        },
        "QCD_Pt-15to7000_Flat2017" : {
            "CrossSection" : XSValues(
                XS_2017=1361000000.0, XSSource_2017="XSDB",
            ),
        },
        "QCD_Pt-15to7000_Flat2018" : {
            "CrossSection" : XSValues(
                XS_2018=1372000000.0, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "QCD_Pt_50to80" : {
            "CrossSection" : XSValues(
                XS_2016=19204300.0, XSSource_2016="AN2017_013_v17, XSDB 19100000",
                XS_2017=15710000.0, XSSource_2017="XSDB",
                XS_2018=15680000.0, XSSource_2018="XSDB",
            ),
        },
        "QCD_Pt_80to120" : {
            "CrossSection" : XSValues(
                XS_2016=2762530.0, XSSource_2016="AN2017_013_v17, XSDB 2735000",
                XS_2017=2336000.0, XSSource_2017="XSDB",
                XS_2018=2343000.0, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "QCD_Pt_120to170" : {
            "CrossSection" : XSValues(
                XS_2016=471100.0, XSSource_2016="AN2017_013_v17, XSDB 467500",
                XS_2017=407300.0, XSSource_2017="XSDB",
                XS_2018=406800.0, XSSource_2018="XSDB",
            ),
        },
        "QCD_Pt_170to300" : {
            "CrossSection" : XSValues(
                XS_2016=117276.0, XSSource_2016="AN2017_013_v17, XSDB 117400",
                XS_2017=103500.0, XSSource_2017="XSDB",
                XS_2018=103300.0, XSSource_2018="XSDB",
            ),
        },
        "QCD_Pt_300to470" : {
            "CrossSection" : XSValues(
                XS_2016=7823.0, XSSource_2016="AN2017_013_v17, XSDB 7753",
                XS_2017=6830.0, XSSource_2017="XSDB",
                XS_2018=6826.0, XSSource_2018="XSDB",
            ),
        },
        "QCD_Pt_470to600" : {
            "CrossSection" : XSValues(
                XS_2016=648.2, XSSource_2016="AN2017_013_v17, XSDB 642.1",
                XS_2017=552.1, XSSource_2017="XSDB",
                XS_2018=552.6, XSSource_2018="XSDB",
            ),
        },
        "QCD_Pt_600to800" : {
            "CrossSection" : XSValues(
                XS_2016=186.9, XSSource_2016="AN2017_013_v17, XSDB 185.9",
                XS_2017=156.5, XSSource_2017="XSDB",
                XS_2018=156.6, XSSource_2018="XSDB",
            ),
        },
        "QCD_Pt_800to1000" : {
            "CrossSection" : XSValues(
                XS_2016=32.293, XSSource_2016="AN2017_013_v17, XSDB 32.05",
                XS_2017=26.28, XSSource_2017="XSDB",
                XS_2018=26.32, XSSource_2018="XSDB",
            ),
        },
        "QCD_Pt_1000to1400" : {
            "CrossSection" : XSValues(
                XS_2016=9.4183, XSSource_2016="AN2017_013_v17, XSDB 9.365",
                XS_2017=7.47, XSSource_2017="XSDB",
                XS_2018=7.50, XSSource_2018="XSDB",
            ),
        },
        "QCD_Pt_1400to1800" : {
            "CrossSection" : XSValues(
                XS_2016=0.84265, XSSource_2016="AN2017_013_v17, XSDB 0.8398",
                XS_2017=0.6484, XSSource_2017="XSDB",
                XS_2018=0.6479, XSSource_2018="XSDB",
            ),
        },
        "QCD_Pt_1800to2400" : {
            "CrossSection" : XSValues(
                XS_2016=0.114943, XSSource_2016="AN2017_013_v17, XSDB 0.1124",
                XS_2017=0.08743, XSSource_2017="XSDB",
                XS_2018=0.08715, XSSource_2018="XSDB",
            ),
        },
        "QCD_Pt_2400to3200" : {
            "CrossSection" : XSValues(
                XS_2016=0.00682981, XSSource_2016="AN2017_013_v17, XSDB 0.006752",
                XS_2017=0.005236, XSSource_2017="XSDB",
                XS_2018=0.005242, XSSource_2018="XSDB",
            ),
        },
        "QCD_Pt_3200toInf" : {
            "CrossSection" : XSValues(
                XS_2016=0.000165445, XSSource_2016="AN2017_013_v17, XSDB 0.0001626",
                XS_2017=0.0001357, XSSource_2017="XSDB",
                XS_2018=0.0001349, XSSource_2018="XSDB",
            ),
        },
        "DYJetsToLL_M-50_HT-100to200" : {
            "CrossSection" : XSValues(
                XS_2016=147.4, XSSource_2016="XSDB (LO)",
                XS_2017=161.1, XSSource_2017="XSDB (LO)",
                XS_2018=160.8, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.2245, kFactorSource_2016="XSDB NNLO/LO=6077.22/4963",
                kFactor_2017=1.1374, kFactorSource_2017="XSDB NNLO/LO=6077.22/5343",
                kFactor_2018=1.1421, kFactorSource_2018="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_2017=1.000, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=1.000, CorrSource_2018="Same as 2017",
            ),
        },
        "DYJetsToLL_M-50_HT-200to400" : {
            "CrossSection" : XSValues(
                XS_2016=41.04, XSSource_2016="XSDB (LO)",
                XS_2017=48.66, XSSource_2017="XSDB (LO)",
                XS_2018=48.61, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.2245, kFactorSource_2016="XSDB NNLO/LO=6077.22/4963",
                kFactor_2017=1.1374, kFactorSource_2017="XSDB NNLO/LO=6077.22/5343",
                kFactor_2018=1.1421, kFactorSource_2018="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_2017=0.999, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=0.999, CorrSource_2018="Same as 2017",
            ),
        },
        "DYJetsToLL_M-50_HT-400to600" : {
            "CrossSection" : XSValues(
                XS_2016=5.674, XSSource_2016="XSDB (LO)",
                XS_2017=6.968, XSSource_2017="XSDB (LO)",
                XS_2018=6.978, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.2245, kFactorSource_2016="XSDB NNLO/LO=6077.22/4963",
                kFactor_2017=1.1374, kFactorSource_2017="XSDB NNLO/LO=6077.22/5343",
                kFactor_2018=1.1421, kFactorSource_2018="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_2017=0.990, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=0.990, CorrSource_2018="Same as 2017",
            ),
        },
        "DYJetsToLL_M-50_HT-600to800" : {
            "CrossSection" : XSValues(
                XS_2016=1.358, XSSource_2016="XSDB (LO)",
                XS_2017=1.743, XSSource_2017="XSDB (LO)",
                XS_2018=1.757, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.2245, kFactorSource_2016="XSDB NNLO/LO=6077.22/4963",
                kFactor_2017=1.1374, kFactorSource_2017="XSDB NNLO/LO=6077.22/5343",
                kFactor_2018=1.1421, kFactorSource_2018="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_2017=0.975, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=0.975, CorrSource_2018="Same as 2017",
            ),
        },
        "DYJetsToLL_M-50_HT-800to1200" : {
            "CrossSection" : XSValues(
                XS_2016=0.6229, XSSource_2016="XSDB (LO)",
                XS_2017=0.8052, XSSource_2017="XSDB (LO)",
                XS_2018=0.8094, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.2245, kFactorSource_2016="XSDB NNLO/LO=6077.22/4963",
                kFactor_2017=1.1374, kFactorSource_2017="XSDB NNLO/LO=6077.22/5343",
                kFactor_2018=1.1421, kFactorSource_2018="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_2017=0.907, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=0.907, CorrSource_2018="Same as 2017",
            ),
        },
        "DYJetsToLL_M-50_HT-1200to2500" : {
            "CrossSection" : XSValues(
                XS_2016=0.1512, XSSource_2016="XSDB (LO)",
                XS_2017=0.1933, XSSource_2017="XSDB (LO)",
                XS_2018=0.1931, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.2245, kFactorSource_2016="XSDB NNLO/LO=6077.22/4963",
                kFactor_2017=1.1374, kFactorSource_2017="XSDB NNLO/LO=6077.22/5343",
                kFactor_2018=1.1421, kFactorSource_2018="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_2017=0.833, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=0.833, CorrSource_2018="Same as 2017",
            ),
        },
        "DYJetsToLL_M-50_HT-2500toInf" : {
            "CrossSection" : XSValues(
                XS_2016=0.003659, XSSource_2016="XSDB (LO)",
                XS_2017=0.003468, XSSource_2017="XSDB (LO)",
                XS_2018=0.003514, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.2245, kFactorSource_2016="XSDB NNLO/LO=6077.22/4963",
                kFactor_2017=1.1374, kFactorSource_2017="XSDB NNLO/LO=6077.22/5343",
                kFactor_2018=1.1421, kFactorSource_2018="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_2017=1.015, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=1.015, CorrSource_2018="Same as 2017",
            ),
        },
        "DYJetsToLL_M-50" : {
            "CrossSection" : XSValues(
                XS_13TeV=6077.22, XSSource_13TeV="XSDB (NNLO)",
            ),
        },
        "ZJetsToNuNu_HT-100To200" : {
            "CrossSection" : XSValues(
                XS_2016=280.35, XSSource_2016="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#DY_Z",
                XS_2017=302.8, XSSource_2017="XSDB (LO)",
                XS_2018=304.0, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.2245, kFactorSource_2016="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/4963",
                kFactor_2017=1.1374, kFactorSource_2017="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/5343",
                kFactor_2018=1.1421, kFactorSource_2018="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_2017=0.994, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=0.994, CorrSource_2018="Same as 2017",
            ),
        },
        "ZJetsToNuNu_HT-200To400" : {
            "CrossSection" : XSValues(
                XS_2016=77.67, XSSource_2016="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#DY_Z",
                XS_2017=92.59, XSSource_2017="XSDB (LO)",
                XS_2018=91.68, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.2245, kFactorSource_2016="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/4963",
                kFactor_2017=1.1374, kFactorSource_2017="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/5343",
                kFactor_2018=1.1421, kFactorSource_2018="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_2017=0.981, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=0.981, CorrSource_2018="Same as 2017",
            ),
        },
        "ZJetsToNuNu_HT-400To600" : {
            "CrossSection" : XSValues(
                XS_2016=10.73, XSSource_2016="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#DY_Z",
                XS_2017=13.18, XSSource_2017="XSDB (LO)",
                XS_2018=13.11, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.2245, kFactorSource_2016="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/4963",
                kFactor_2017=1.1374, kFactorSource_2017="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/5343",
                kFactor_2018=1.1421, kFactorSource_2018="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_2017=0.977, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=0.977, CorrSource_2018="Same as 2017",
            ),
        },
        "ZJetsToNuNu_HT-600To800" : {
            "CrossSection" : XSValues(
                XS_2016=2.559, XSSource_2016="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#DY_Z",
                XS_2017=3.257, XSSource_2017="XSDB (LO)",
                XS_2018=3.245, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.2245, kFactorSource_2016="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/4963",
                kFactor_2017=1.1374, kFactorSource_2017="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/5343",
                kFactor_2018=1.1421, kFactorSource_2018="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_2017=0.975, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=0.975, CorrSource_2018="Same as 2017",
            ),
        },
        "ZJetsToNuNu_HT-800To1200" : {
            "CrossSection" : XSValues(
                XS_2016=1.1796, XSSource_2016="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#DY_Z",
                XS_2017=1.49,   XSSource_2017="XSDB (LO)",
                XS_2018=1.497,  XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.2245, kFactorSource_2016="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/4963",
                kFactor_2017=1.1374, kFactorSource_2017="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/5343",
                kFactor_2018=1.1421, kFactorSource_2018="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_2017=0.916, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=0.916, CorrSource_2018="Same as 2017",
            ),
        },
        "ZJetsToNuNu_HT-1200To2500" : {
            "CrossSection" : XSValues(
                XS_2016=0.28833, XSSource_2016="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#DY_Z",
                XS_2017=0.3419,  XSSource_2017="XSDB (LO)",
                XS_2018=0.3425,  XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.2245, kFactorSource_2016="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/4963",
                kFactor_2017=1.1374, kFactorSource_2017="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/5343",
                kFactor_2018=1.1421, kFactorSource_2018="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_2017=0.880, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=0.880, CorrSource_2018="Same as 2017",
            ),
        },
        "ZJetsToNuNu_HT-2500ToInf" : {
            "CrossSection" : XSValues(
                XS_2016=0.006945, XSSource_2016="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#DY_Z",
                XS_2017=0.005146, XSSource_2017="XSDB (LO)",
                XS_2018=0.005263, XSSource_2018="GenXSecAnalyzer",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.2245, kFactorSource_2016="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/4963",
                kFactor_2017=1.1374, kFactorSource_2017="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/5343",
                kFactor_2018=1.1421, kFactorSource_2018="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_2017=1.276, CorrSource_2017="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_2018=1.276, CorrSource_2018="Same as 2017",
            ),
        },
        "ZJetsToNuNu_Zpt-100to200" : {
            "CrossSection" : XSValues(
                XS_2016=35.99, XSSource_2016="XSDB (LO)",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.2245, kFactorSource_2016="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/4963",
                kFactor_2017=1.1374, kFactorSource_2017="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/5343",
                kFactor_2018=1.1421, kFactorSource_2018="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/5321",
            ),
        },
        "ZJetsToNuNu_Zpt-200toInf" : {
            "CrossSection" : XSValues(
                XS_2016=4.201, XSSource_2016="XSDB (LO)",
            ),
            "kFactor" : kFactorValues(
                kFactor_2016=1.2245, kFactorSource_2016="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/4963",
                kFactor_2017=1.1374, kFactorSource_2017="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/5343",
                kFactor_2018=1.1421, kFactorSource_2018="XSDB DYJetsToLL_M-50 NNLO/LO=6077.22/5321",
            ),
        },
        "GJets_HT-100To200" : {
            "CrossSection" : XSValues(
                XS_2016=9249.0, XSSource_2016="XSDB (LO)",
                XS_2017=8640.0, XSSource_2017="XSDB (LO)",
                XS_2018=8608.0, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "GJets_HT-200To400" : {
            "CrossSection" : XSValues(
                XS_2016=2321.0, XSSource_2016="XSDB (LO)",
                XS_2017=2185.0, XSSource_2017="XSDB (LO)",
                XS_2018=2190.0, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "GJets_HT-400To600" : {
            "CrossSection" : XSValues(
                XS_2016=275.2, XSSource_2016="XSDB (LO)",
                XS_2017=258.5, XSSource_2017="GenXSecAnalyzer",
                XS_2018=258.0, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "GJets_HT-600ToInf" : {
            "CrossSection" : XSValues(
                XS_2016=93.19, XSSource_2016="XSDB (LO)",
                XS_2017=85.31, XSSource_2017="XSDB (LO)",
                XS_2018=85.11, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "GJets_DR-0p4_HT-100To200" : {
            "CrossSection" : XSValues(
                XS_2016=5363.0, XSSource_2016="XSDB (LO)",
                XS_2017=5044.0, XSSource_2017="GenXSecAnalyzer",
                XS_2018=5030.0, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "GJets_DR-0p4_HT-200To400" : {
            "CrossSection" : XSValues(
                XS_2016=1178.0, XSSource_2016="XSDB (LO)",
                XS_2017=1130.0, XSSource_2017="GenXSecAnalyzer",
                XS_2018=1125.0, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "GJets_DR-0p4_HT-400To600" : {
            "CrossSection" : XSValues(
                XS_2016=131.8, XSSource_2016="XSDB (LO)",
                XS_2017=124.6, XSSource_2017="GenXSecAnalyzer",
                XS_2018=124.7, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "GJets_DR-0p4_HT-600ToInf" : {
            "CrossSection" : XSValues(
                XS_2016=44.27, XSSource_2016="XSDB (LO)",
                XS_2017=40.65, XSSource_2017="GenXSecAnalyzer",
                XS_2018=40.46, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "ST_s-channel_4f_hadronicDecays" : {
            "CrossSection" : XSValues(
                XS_2017=11.24, XSSource_2017="GenXSecAnalyzer",
                XS_2018=11.24, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "ST_s-channel_4f_leptonDecays" : {
            "CrossSection" : XSValues(
                XS_2016=3.365, XSSource_2016="XSDB (unknown)",
                XS_2017=3.74,  XSSource_2017="XSDB (unknown)",
                XS_2018=3.740, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "ST_s-channel_4f_InclusiveDecays" : {
            "CrossSection" : XSValues(
                XS_13TeV=10.12, XSSource_13TeV="XSDB (unknown)",
            ),
        },
        "ST_t-channel_top_4f_InclusiveDecays" : {
            "CrossSection" : XSValues(
                XS_2016=136.02, XSSource_2016="Unknown (GenXSecAnalyzer/XSDB return 0.0)",
                XS_2017=113.3,  XSSource_2017="XSDB (NLO)",
                XS_2018=115.3,  XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "ST_t-channel_antitop_4f_InclusiveDecays" : {
            "CrossSection" : XSValues(
                XS_2016=80.95, XSSource_2016="Unknown (GenXSecAnalyzer/XSDB return 0.0)",
                XS_2017=67.91, XSSource_2017="XSDB (NLO)",
                XS_2018=69.09, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "ST_tW_top_5f_NoFullyHadronicDecays" : {
            "CrossSection" : XSValues(
                XS_2016=38.09, XSSource_2016="XSDB (NLO)",
                XS_2017=34.91, XSSource_2017="XSDB (NLO)",
                XS_2018=34.91, XSSource_2018="GenXSecAnalyzer",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=(1-(1-3*0.105)**2), BRSource_13TeV="http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf",
            ),
        },
        "ST_tW_antitop_5f_NoFullyHadronicDecays" : {
            "CrossSection" : XSValues(
                XS_2016=38.06, XSSource_2016="XSDB (NLO)",
                XS_2017=34.97, XSSource_2017="XSDB (NLO)",
                XS_2018=34.97, XSSource_2018="GenXSecAnalyzer",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=(1-(1-3*0.105)**2), BRSource_13TeV="http://pdg.lbl.gov/2019/reviews/rpp2018-rev-top-quark.pdf",
            ),
        },
        "ST_tW_top_5f_inclusiveDecays" : {
            "CrossSection" : XSValues(
                XS_2016=38.09, XSSource_2016="XSDB (NLO)",
                XS_2017=34.91, XSSource_2017="XSDB (NLO)",
                XS_2018=34.91, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "ST_tW_antitop_5f_inclusiveDecays" : {
            "CrossSection" : XSValues(
                XS_2016=38.06, XSSource_2016="XSDB (NLO)",
                XS_2017=34.97, XSSource_2017="XSDB (NLO)",
                XS_2018=34.97, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "tZq_W_lept_Z_hadron_4f_ckm" : {
            "CrossSection" : XSValues(
                XS_2016=0.1573, XSSource_13TeV="XSDB (unknown)",
            ),
        },
        "tZq_Zhad_Wlept_4f_ckm" : {
            "CrossSection" : XSValues(
                XS_2017=0.1518, XSSource_2017="XSDB (unknown)",
            ),
        },
        "WW" : {
            "CrossSection" : XSValues(
                XS_13TeV=51.723, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson, WW>4q NNLO",
            ),
        },
        "WZ" : {
            "CrossSection" : XSValues(
                XS_13TeV=47.13, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson, inclusive NLO from MCFM",
            ),
        },
        "ZZ" : {
            "CrossSection" : XSValues(
                XS_13TeV=16.523, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson, inclusive NLO from MCFM",
            ),
        },
        "WWTo2L2Nu" : {
            "CrossSection" : XSValues(
                XS_13TeV=12.178, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson, WW>2l2v NNLO",
            ),
        },
        "WGJets_MonoPhoton_PtG-40to130" : {
            "CrossSection" : XSValues(
                XS_2016=12.68,  XSSource_2016="XSDB (LO)",
                XS_2017=12.93, XSSource_2017="XSDB (LO)",
                XS_2018=12.95, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "WGJets_MonoPhoton_PtG-130" : {
            "CrossSection" : XSValues(
                XS_2016=0.6578, XSSource_2016="XSDB (LO)",
                XS_2017=0.7158, XSSource_2017="GenXSecAnalyzer",
                XS_2018=0.7153, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "WWG" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.2147, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Triboson",
            ),
        },
        "WZG" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.04123, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Triboson",
            ),
        },
        "ZH_HToBB_ZToNuNu_M125" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.10299357, XSSource_13TeV="BR of H->bb from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR with H-mass 125.09 GeV, xsec from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV#ZHllH_H_l_e_or_Process",
            ),
        },
        "WH_HToBB_WToLNu_M125" : {
            "CrossSection" : XSValues(
                XS_13TeV=1.373, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV#ppWH_Total_Cross_Section_with_ap",
            ),
        },
        "WWTo1L1Nu2Q" : {
            "CrossSection" : XSValues(
                XS_2016=45.68, XSSource_2016="XSDB (LO)",
                XS_2017=80.74, XSSource_2017="XSDB (LO)",
                XS_2018=81.46, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "WZTo1L1Nu2Q" : {
            "CrossSection" : XSValues(
                XS_2016=10.73, XSSource_2016="XSDB (LO)",
                XS_2017=11.66, XSSource_2017="XSDB (LO)",
                XS_2018=11.76, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "WZTo1L3Nu" : {
            "CrossSection" : XSValues(
                XS_2016=3.054, XSSource_2016="XSDB (LO)",
                XS_2017=3.294, XSSource_2017="GenXSecAnalyzer",
                XS_2018=3.322, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "ZGTo2NuG" : {
            "CrossSection" : XSValues(
                XS_13TeV=32.3, XSSource_13TeV="MCM",
            ),
        },
        "ZZTo2L2Nu" : {
            "CrossSection" : XSValues(
                XS_2016=0.5644, XSSource_2016="GenXSecAnalyzer",
                XS_2017=0.6008, XSSource_2017="GenXSecAnalyzer",
                XS_2018=0.6008, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "ZZTo2L2Q" : {
            "CrossSection" : XSValues(
                XS_2016=3.222, XSSource_2016="XSDB (unknown)",
                XS_2017=3.688, XSSource_2017="XSDB (unknown)",
                XS_2018=3.709, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "ZZTo2Q2Nu" : {
            "CrossSection" : XSValues(
                XS_2016=4.033, XSSource_2016="XSDB (unknown)",
                XS_2017=4.416, XSSource_2017="MCM",
                XS_2018=4.416, XSSource_2018="MCM",
            ),
        },
        "TTZToLLNuNu_M-10" : {
            "CrossSection" : XSValues(
                XS_2016=0.2529, XSSource_2016="XSDB (unknown)",
                XS_2017=0.2432, XSSource_2017="XSDB (unknown)",
                XS_2018=0.2432, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "TTZToQQ" : {
            "CrossSection" : XSValues(
                XS_2016=0.5297, XSSource_2016="XSDB (unknown)",
                XS_2017=0.5104, XSSource_2017="XSDB (unknown)",
                XS_2018=0.5104, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "TTWJetsToLNu" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.2043, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#TT_X, NLO",
            ),
        },
        "TTWJetsToQQ" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.4062, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#TT_X, NLO",
            ),
        },
        "TTGJets" : {
            "CrossSection" : XSValues(
                XS_13TeV=3.697, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#TT_X, NLO",
            ),
        },
        "ttHJetToNonbb_M125" : {
            "CrossSection" : XSValues(
                XS_2016=0.4870, XSSource_2016="GenXSecAnalyzer",
                XS_2017=0.5086, XSSource_2017="GenXSecAnalyzer",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=(1-0.577), BRSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#ttH",
            ),
        },
        "ttHJetTobb_M125" : {
            "CrossSection" : XSValues(
                XS_2016=0.4884, XSSource_2016="GenXSecAnalyzer",
                XS_2017=0.5080, XSSource_2017="GenXSecAnalyzer",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.577, BRSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#ttH",
            ),
        },
        "ttHToNonbb_M125" : {
            "CrossSection" : XSValues(
                XS_2018=0.5269, XSSource_2018="GenXSecAnalyzer",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=(1-0.577), BRSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#ttH",
            ),
        },
        "ttHTobb_M125" : {
            "CrossSection" : XSValues(
                XS_2018=0.5269, XSSource_2018="GenXSecAnalyzer",
            ),
            "BranchingRatio" : BRValues(
                BR_13TeV=0.577, BRSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#ttH",
            ),
        },
        "TTTT" : {
            "CrossSection" : XSValues(
                XS_2016=0.009103, XSSource_2016="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#TT_X, NLO",
                XS_2017=0.008213, XSSource_2017="XSDB (unknown)",
                XS_2018=0.008213, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "TTHH" : {
            "CrossSection" : XSValues(
                XS_2016=0.0007367, XSSource_2016="XSDB (LO)",
                XS_2017=0.0006655, XSSource_2017="XSDB (LO)",
                XS_2018=0.0006651, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "TTTW" : {
            "CrossSection" : XSValues(
                XS_2016=0.0008612, XSSource_2016="XSDB (LO)",
                XS_2017=0.0007314, XSSource_2017="XSDB (LO)",
                XS_2018=0.0007317, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "TTWH" : {
            "CrossSection" : XSValues(
                XS_2016=0.001344, XSSource_2016="XSDB (LO)",
                XS_2017=0.001141, XSSource_2017="XSDB (LO)",
                XS_2018=0.001140, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "TTWW" : {
            "CrossSection" : XSValues(
                XS_2016=0.007834, XSSource_2016="XSDB (LO)",
                XS_2017=0.006979, XSSource_2017="XSDB (LO)",
                XS_2018=0.006989, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "TTWZ" : {
            "CrossSection" : XSValues(
                XS_2016=0.002938, XSSource_2016="XSDB (LO)",
                XS_2017=0.002441, XSSource_2017="XSDB (LO)",
                XS_2018=0.002449, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "TTZH" : {
            "CrossSection" : XSValues(
                XS_2016=0.001244, XSSource_2016="XSDB (LO)",
                XS_2017=0.00113,  XSSource_2017="XSDB (LO)",
                XS_2018=0.001131, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "TTZZ" : {
            "CrossSection" : XSValues(
                XS_2016=0.001563, XSSource_2016="XSDB (LO)",
                XS_2017=0.001386, XSSource_2017="XSDB (LO)",
                XS_2018=0.001387, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "TTTJ" : {
            "CrossSection" : XSValues(
                XS_2016=0.0004812, XSSource_2016="XSDB (LO)",
                XS_2017=0.0003974, XSSource_2017="XSDB (LO)",
                XS_2018=0.0003972, XSSource_2018="GenXSecAnalyzer",
            ),
        },
        "WWW_4F" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.2086, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Triboson and XSDB, NLO",
            ),
        },
        "WWZ_4F" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.1651, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Triboson and XSDB, NLO",
            ),
        },
        "WWZ" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.1651, XSSource_13TeV="XSDB",
            ),
        },
        "WZZ" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.05565, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Triboson and XSDB, NLO",
            ),
        },
        "ZZZ" : {
            "CrossSection" : XSValues(
                XS_13TeV=0.01398, XSSource_13TeV="https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Triboson and XSDB, NLO",
            ),
        },
        "TChiWZ_800_100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00475843),
        },
        "SMS-T1bbbb_mGluino-1000_mLSP-900" : {
            "CrossSection" : XSValues(XS_13TeV=0.385E+00),
        },
        "SMS-T1bbbb_mGluino-1500_mLSP-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.157E-01),
        },
        "SMS-T1tttt_mGluino-1200_mLSP-800" : {
            "CrossSection" : XSValues(XS_13TeV=0.985E-01),
        },
        "SMS-T1tttt_mGluino-1500_mLSP-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.157E-01),
        },
        "SMS-T1tttt_mGl-1500_mLSP-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.157E-01),
        },
        "SMS-T1tttt_mGluino-2000_mLSP-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.101E-02),
        },
        "SMS-T1qqqq_mGluino-1000_mLSP-800" : {
            "CrossSection" : XSValues(XS_13TeV=0.385E+00),
        },
        "SMS-T1qqqq_mGluino-1400_mLSP-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.284E-01),
        },
        "SMS-T1qqqq_mGluino-1800_mLSP-200_ctau-1" : {
            "CrossSection" : XSValues(XS_13TeV=0.293E-02),
        },
        "SMS-T2tt_mStop-150_mLSP-50" : {
            "CrossSection" : XSValues(XS_13TeV=0.304E+03),
        },
        "SMS-T2tt_mStop-200_mLSP-50" : {
            "CrossSection" : XSValues(XS_13TeV=0.755E+02),
        },
        "SMS-T2tt_mStop-225_mLSP-50" : {
            "CrossSection" : XSValues(XS_13TeV=0.420E+02),
        },
        "SMS-T2tt_mStop-250_mLSP-150" : {
            "CrossSection" : XSValues(XS_13TeV=0.248E+02),
        },
        "SMS-T2tt_mStop-250_mLSP-50" : {
            "CrossSection" : XSValues(XS_13TeV=0.248E+02),
        },
        "SMS-T2tt_mStop-300_mLSP-150" : {
            "CrossSection" : XSValues(XS_13TeV=0.100E+02),
        },
        "SMS-T2tt_mStop-325_mLSP-150" : {
            "CrossSection" : XSValues(XS_13TeV=0.657E+01),
        },
        "SMS-T2tt_mStop-350_mLSP-150" : {
            "CrossSection" : XSValues(XS_13TeV=0.443E+01),
        },
        "SMS-T2tt_mStop-425_mLSP-325" : {
            "CrossSection" : XSValues(XS_13TeV=0.154E+01),
        },
        "SMS-T2tt_mStop-500_mLSP-325" : {
            "CrossSection" : XSValues(XS_13TeV=0.609E+00),
        },
        "SMS-T2tt_mStop-650_mLSP-350" : {
            "CrossSection" : XSValues(XS_13TeV=0.125E+00),
        },
        "SMS-T2tt_mStop-850_mLSP-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.216E-01),
        },
        "SMS-T2tt_mStop-1200_mLSP-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.170E-02),
        },
        "SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1" : {
            "CrossSection" : XSValues(XS_13TeV=0.146E+03),
        },
        "SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50" : {
            "CrossSection" : XSValues(XS_13TeV=0.248E+02),
        },
        "SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-75" : {
            "CrossSection" : XSValues(XS_13TeV=0.248E+02),
        },
        "SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.248E+02),
        },
        "SMS-T2tt_3J_xqcut-20_mStop-700_mLSP-525" : {
            "CrossSection" : XSValues(XS_13TeV=0.783E-01),
        },
        "SMS-T5qqqqWW_mGluino-1900_mLSP-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.171E-02),
        },
        "SMS-T5qqqqZH-mGluino750" : {
            "CrossSection" : XSValues(XS_13TeV=0.277E+01),
        },
        "SMS-T5qqqqZH-mGluino1000" : {
            "CrossSection" : XSValues(XS_13TeV=0.385E+00),
        },
        "SMS-T5qqqqZH-mGluino1100" : {
            "CrossSection" : XSValues(XS_13TeV=0.191E+00),
        },
        "SMS-T5qqqqZH-mGluino1200" : {
            "CrossSection" : XSValues(XS_13TeV=0.985E-01),
        },
        "SMS-T5qqqqZH-mGluino1300" : {
            "CrossSection" : XSValues(XS_13TeV=0.522E-01),
        },
        "SMS-T5qqqqZH-mGluino1400" : {
            "CrossSection" : XSValues(XS_13TeV=0.284E-01),
        },
        "SMS-T5qqqqZH-mGluino1500" : {
            "CrossSection" : XSValues(XS_13TeV=0.157E-01),
        },
        "SMS-T5qqqqZH-mGluino1600" : {
            "CrossSection" : XSValues(XS_13TeV=0.887E-02),
        },
        "SMS-T5qqqqZH-mGluino1700" : {
            "CrossSection" : XSValues(XS_13TeV=0.507E-02),
        },
        "SMS-T5qqqqZH-mGluino1800" : {
            "CrossSection" : XSValues(XS_13TeV=0.293E-02),
        },
        "SMS-T5qqqqZH-mGluino1900" : {
            "CrossSection" : XSValues(XS_13TeV=0.171E-02),
        },
        "SMS-T5qqqqZH-mGluino2000" : {
            "CrossSection" : XSValues(XS_13TeV=0.101E-02),
        },
        "SMS-T5qqqqZH-mGluino2100" : {
            "CrossSection" : XSValues(XS_13TeV=0.598E-03),
        },
        "SMS-T5qqqqZH-mGluino2200" : {
            "CrossSection" : XSValues(XS_13TeV=0.321E-03),
        },
        "SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1" : {
            "CrossSection" : XSValues(XS_13TeV=0.002548),
        },
        "SMS-TChiWZ_ZToLL_mZMin-0p1_mChargino250_mLSP230" : {
            "CrossSection" : XSValues(XS_13TeV=0.6204),
        },
        "SMS-TChiWZ_ZToLL_mZMin-0p1" : {
            "CrossSection" : XSValues(XS_13TeV=0.6204),
        },
        "stealth_stop_350_singlino_SYY" : {
            "CrossSection" : XSValues(XS_13TeV=4.43),
        },
        "stealth_stop_450_singlino_SYY" : {
            "CrossSection" : XSValues(XS_13TeV=1.11),
        },
        "stealth_stop_550_singlino_SYY" : {
            "CrossSection" : XSValues(XS_13TeV=0.347),
        },
        "stealth_stop_650_singlino_SYY" : {
            "CrossSection" : XSValues(XS_13TeV=0.125),
        },
        "stealth_stop_750_singlino_SYY" : {
            "CrossSection" : XSValues(XS_13TeV=0.0500),
        },
        "stealth_stop_850_singlino_SYY" : {
            "CrossSection" : XSValues(XS_13TeV=0.0216),
        },
        "stealth_stop_350_singlino_SHuHd" : {
            "CrossSection" : XSValues(XS_13TeV=4.43),
        },
        "stealth_stop_450_singlino_SHuHd" : {
            "CrossSection" : XSValues(XS_13TeV=1.11),
        },
        "stealth_stop_550_singlino_SHuHd" : {
            "CrossSection" : XSValues(XS_13TeV=0.347),
        },
        "stealth_stop_650_singlino_SHuHd" : {
            "CrossSection" : XSValues(XS_13TeV=0.125),
        },
        "stealth_stop_750_singlino_SHuHd" : {
            "CrossSection" : XSValues(XS_13TeV=0.0500),
        },
        "stealth_stop_850_singlino_SHuHd" : {
            "CrossSection" : XSValues(XS_13TeV=0.0216),
        },
        # Stealth taken From https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom
        "StealthSYY_2t6j_mStop-300_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=10.0),
        },
        "StealthSYY_2t6j_mStop-300_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=10.0),
        },
        "StealthSYY_2t6j_mStop-350_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=4.43),
        },
        "StealthSYY_2t6j_mStop-350_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=4.43),
        },
        "StealthSYY_2t6j_mStop-400_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=2.15),
        },
        "StealthSYY_2t6j_mStop-400_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=2.15),
        },
        "StealthSYY_2t6j_mStop-450_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=1.11),
        },
        "StealthSYY_2t6j_mStop-450_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=1.11),
        },
        "StealthSYY_2t6j_mStop-500_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.609),
        },
        "StealthSYY_2t6j_mStop-500_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.609),
        },
        "StealthSYY_2t6j_mStop-550_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.347),
        },
        "StealthSYY_2t6j_mStop-550_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.347),
        },
        "StealthSYY_2t6j_mStop-600_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.205),
        },
        "StealthSYY_2t6j_mStop-600_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.205),
        },
        "StealthSYY_2t6j_mStop-650_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.125),
        },
        "StealthSYY_2t6j_mStop-650_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.125),
        },
        "StealthSYY_2t6j_mStop-700_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0783),
        },
        "StealthSYY_2t6j_mStop-700_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0783),
        },
        "StealthSYY_2t6j_mStop-750_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0500),
        },
        "StealthSYY_2t6j_mStop-750_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0500),
        },
        "StealthSYY_2t6j_mStop-800_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0326),
        },
        "StealthSYY_2t6j_mStop-800_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0326),
        },
        "StealthSYY_2t6j_mStop-850_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0216),
        },
        "StealthSYY_2t6j_mStop-850_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0216),
        },
        "StealthSYY_2t6j_mStop-900_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0145),
        },
        "StealthSYY_2t6j_mStop-900_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0145),
        },
        "StealthSYY_2t6j_mStop-950_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00991),
        },
        "StealthSYY_2t6j_mStop-950_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00991),
        },
        "StealthSYY_2t6j_mStop-1000_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00683),
        },
        "StealthSYY_2t6j_mStop-1000_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00683),
        },
        "StealthSYY_2t6j_mStop-1050_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00476),
        },
        "StealthSYY_2t6j_mStop-1050_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00476),
        },
        "StealthSYY_2t6j_mStop-1100_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00335),
        },
        "StealthSYY_2t6j_mStop-1100_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00335),
        },
        "StealthSYY_2t6j_mStop-1150_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00238),
        },
        "StealthSYY_2t6j_mStop-1150_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00238),
        },
        "StealthSYY_2t6j_mStop-1200_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00170),
        },
        "StealthSYY_2t6j_mStop-1200_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00170),
        },
        "StealthSYY_2t6j_mStop-1250_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00122),
        },
        "StealthSYY_2t6j_mStop-1250_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00122),
        },
        "StealthSYY_2t6j_mStop-1300_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000887),
        },
        "StealthSYY_2t6j_mStop-1300_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000887),
        },
        "StealthSYY_2t6j_mStop-1350_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000646),
        },
        "StealthSYY_2t6j_mStop-1350_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000646),
        },
        "StealthSYY_2t6j_mStop-1400_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000473),
        },
        "StealthSYY_2t6j_mStop-1400_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000473),
        },
        "StealthSHH_2t4b_mStop-300_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=10.0),
        },
        "StealthSHH_2t4b_mStop-350_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=4.43),
        },
        "StealthSHH_2t4b_mStop-400_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=2.15),
        },
        "StealthSHH_2t4b_mStop-450_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=1.11),
        },
        "StealthSHH_2t4b_mStop-500_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.609),
        },
        "StealthSHH_2t4b_mStop-550_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.347),
        },
        "StealthSHH_2t4b_mStop-600_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.205),
        },
        "StealthSHH_2t4b_mStop-650_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.125),
        },
        "StealthSHH_2t4b_mStop-700_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0783),
        },
        "StealthSHH_2t4b_mStop-750_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0500),
        },
        "StealthSHH_2t4b_mStop-800_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0326),
        },
        "StealthSHH_2t4b_mStop-850_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0216),
        },
        "StealthSHH_2t4b_mStop-900_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0145),
        },
        "StealthSHH_2t4b_mStop-950_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00991),
        },
        "StealthSHH_2t4b_mStop-1000_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00683),
        },
        "StealthSHH_2t4b_mStop-1050_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00476),
        },
        "StealthSHH_2t4b_mStop-1100_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00335),
        },
        "StealthSHH_2t4b_mStop-1150_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00238),
        },
        "StealthSHH_2t4b_mStop-1200_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00170),
        },
        "StealthSHH_2t4b_mStop-1250_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00122),
        },
        "StealthSHH_2t4b_mStop-1300_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000887),
        },
        "StealthSHH_2t4b_mStop-1350_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000646),
        },
        "StealthSHH_2t4b_mStop-1400_mSo-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000473),
        },
        "rpv_stop_350_t3j_uds" : {
            "CrossSection" : XSValues(XS_13TeV=4.43),
        },
        "rpv_stop_450_t3j_uds" : {
            "CrossSection" : XSValues(XS_13TeV=1.11),
        },
        "rpv_stop_550_t3j_uds" : {
            "CrossSection" : XSValues(XS_13TeV=0.347),
        },
        "rpv_stop_650_t3j_uds" : {
            "CrossSection" : XSValues(XS_13TeV=0.125),
        },
        "rpv_stop_750_t3j_uds" : {
            "CrossSection" : XSValues(XS_13TeV=0.0500),
        },
        "rpv_stop_850_t3j_uds" : {
            "CrossSection" : XSValues(XS_13TeV=0.0216),
        },
        # RPV taken from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom
        "RPV_2t6j_mStop-300_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=10.0),
        },
        "RPV_2t6j_mStop-350_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=4.43),
        },
        "RPV_2t6j_mStop-400_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=2.15),
        },
        "RPV_2t6j_mStop-450_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=1.11),
        },
        "RPV_2t6j_mStop-500_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.609),
        },
        "RPV_2t6j_mStop-550_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.347),
        },
        "RPV_2t6j_mStop-600_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.205),
        },
        "RPV_2t6j_mStop-650_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.125),
        },
        "RPV_2t6j_mStop-700_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0783),
        },
        "RPV_2t6j_mStop-750_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0500),
        },
        "RPV_2t6j_mStop-800_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0326),
        },
        "RPV_2t6j_mStop-850_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0216),
        },
        "RPV_2t6j_mStop-900_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.0145),
        },
        "RPV_2t6j_mStop-950_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00991),
        },
        "RPV_2t6j_mStop-1000_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00683),
        },
        "RPV_2t6j_mStop-1050_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00476),
        },
        "RPV_2t6j_mStop-1100_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00335),
        },
        "RPV_2t6j_mStop-1150_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00238),
        },
        "RPV_2t6j_mStop-1200_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00170),
        },
        "RPV_2t6j_mStop-1250_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.00122),
        },
        "RPV_2t6j_mStop-1300_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000887),
        },
        "RPV_2t6j_mStop-1350_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000646),
        },
        "RPV_2t6j_mStop-1400_mN1-100" : {
            "CrossSection" : XSValues(XS_13TeV=0.000473),
        },
    }

    __alternate_names_dict = {
        "TTJets" : ["TT","TTbar"],
        "ST_t-channel_top_4f_InclusiveDecays" : ["ST_t-channel_top_4f_inclusiveDecays"],
        "ST_t-channel_antitop_4f_InclusiveDecays" : ["ST_t-channel_antitop_4f_inclusiveDecays"],
    }

    def __init__(self, extra_dicts=None):
        if self.__alternate_names_dict is not None and len(self.__alternate_names_dict)!=0:
            for key,alt_key_list in self.__alternate_names_dict.items():
                if key in self.__values_dict:
                    for newkey in alt_key_list:
                        self.__values_dict[newkey] = self.__values_dict[key]
                else:
                    raise KeyError('The __values_dict does not contain the key \'' + key + '\'')

        if extra_dicts is not None:
            if type(extra_dicts) == dict:
                self.__values_dict.update(extra_dicts)
            elif type(extra_dicts) == list:
                for ed in extra_dicts:
                    self.__values_dict.update(ed)

    def get_value(self, name, energy, year, key, strict=False):
        """Return the value for a given MC sample, energy or year, and information type

        If information is stored for both an energy and a year, the value for the given energy will be preferentially returned.
        If strict checking is turned on the function will raise an error if a given dictionary or piece of information isn't found.
          Otherwise the default value will be returned with no error (i.e. will return 1.0 for kFactors)

        Args:
            name (`str`): The process name for a given MC sample
            energy (`str`): The simulated energy used during production of the MC sample
            year (`str`): The production year of the MC sample
            key (`str`): The type of information being requested. The Options can be found in the __key_field_map.
            strict (`bool`): Whether or not to perform strict checking of the dictionary

        """
        fields = [self.__key_field_map[key][0]+"_"+energy,self.__key_field_map[key][0]+"_"+year]
        if not name in self.__values_dict:
            raise KeyError("ERROR MCSampleValuesHelper::Unknown process \"" + str(name) + "\"")
        if not key in self.__values_dict[name]:
            if strict:
                print self.__values_dict[name]
                raise KeyError("ERROR MCSampleValuesHelper::The process \"" + str(name) + "\" does not contain a " + str(key) + " tuple")
            else:
                return self.__key_field_map[key][1]
        if not any(f in self.__values_dict[name][key]._fields for f in fields):
            if strict:
                print self.__values_dict[name][key]
                raise KeyError("ERROR MCSampleValuesHelper::The " + str(key) + " tuple for process \"" + str(name) + "\" does contain the key(s) \"" + str(fields) + "\"")
            else:
                self.__key_field_map[key][1]

        if self.__values_dict[name][key].__getattribute__(fields[0]) != self.__key_field_map[key][1]:
            return self.__values_dict[name][key].__getattribute__(fields[0])
        else:
            return self.__values_dict[name][key].__getattribute__(fields[1])

    def get_xs(self, name, energy, year):
        return self.get_value(name, energy, year, "CrossSection", True)

    def get_br(self, name, energy, year):
        return self.get_value(name, energy, year, "BranchingRatio", False)

    def get_kfactor(self, name, energy, year):
        return self.get_value(name, energy, year, "kFactor", False)

    def get_corr(self, name, energy, year):
        return self.get_value(name, energy, year, "Correction", False)
