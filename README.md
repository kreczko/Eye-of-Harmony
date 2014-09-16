Eye of Harmony
==============

A data analysis ~~meta package/framework~~ aggregator tying up the different analysis steps.

The Goal
==============
The goal is to create a ~~framework/meta-package~~ aggregator which ties up the different components 
that make up a particle physics analysis:

1. Preparation of data (map/copy/stream)
2. Verification
3. Data analysis (calculations)
4. Storage of results (reduce/store)
5. Data presentation (plots/tables)
6. Data publication (copy to web-server, notify)

These steps are usually performed with different software (in different frameworks, etc) 
and add to the complexity of the analysis. So lets try and take the complexity away.

Roadmap
==============
 - [ ] add simple single-CPU job for processing ROOT files
 - [ ] add simple multi-CPU job for processing ROOT files
   - [ ] multiprocessing
   - [ ] PROOF
   - [ ] GRID
 - [ ] add converters for
  - [ ] ROOT to protobuf
  - [ ] ROOT to CouchDB
  - [ ] ROOT to HDF5
- [ ] evaluate potential dependencies
  - [ ] matplotlib (plotting)
  - [ ] rootpy (for general ROOT python stuff)
  - [ ] ganlia (for job submission)
  - [ ] RooUnfold (for unfolding)
- [ ] Tutorial
  - [ ] pick simple analysis case (selection, signal/background, ttbar and/or Z)
  - [ ] MC generation example
  - [ ] fit example
  - [ ] limit setting example
  - [ ] unfolding example
