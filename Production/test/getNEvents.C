void getNEvents(TString name){
  name = "root://kodiak-se.baylor.edu/"+name;
  TFile *f = TFile::Open(name);
  TTree *t = (TTree*)f->FindObjectAny("Events");
  cout<<name<<"\t"<<t->GetEntries()<<endl;
}
