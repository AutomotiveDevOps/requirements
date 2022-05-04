#!/bin/bash
mkdir -p reqif
strictdoc export --formats=reqif-sdoc --project-title "Heavy Duty Vehicle Cybersecurity Requirements (HD VCR)" --output-dir . *.sdoc
mv reqif/output.reqif reqif/vcr-experiment.reqif

