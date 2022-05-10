# Requirements

An experimental capture of some Vehicle Cybersecurity Requirements based on https://github.com/AutomotiveDevOps/requirements template using https://github.com/strictdoc-project/strictdoc.

Browsable HTML Output here: https://nmfta-repo.github.io/vcr-experiment/
Download the ReqIF export of the requirements here: https://nmfta-repo.github.io/vcr-experiment/vcr-experiment.reqif

[![Requirements Publish](https://github.com/nmfta-repo/vcr-experiment/actions/workflows/publish.yml/badge.svg)](https://github.com/nmfta-repo/vcr-experiment/actions/workflows/publish.yml)

This document is an experimental capture of a list of security requirements for the gateway devices which are prevalent and proliferating in heavy vehicle network architectures.

The collection of requirements captured here in ``strictdoc`` form were developed in a breakout session at the NMFTA CTSRP November 2021 workshop. The breakout session group discussed a) the workable definition of a gateway device -- focusing especially on the attacker's perspective -- b) possible security requirements for those devices that are gateways (intentional or not) and c) attempted to tie those back to the security requirements for vehicle gateways which were outline by a vehicle network security expert whose presentation on the subject was delivered earlier that day. The workshop participants and the expert cannot be revealed here, except by their own actions since the workshop was held -- as is tradition -- under Chatham house rules.

The reason why gateway devices were considered is because the previous work of the RFPCTL working group focused on telematics devices (ultimately releasing the TSRM) and the next most relevant device from a security point of view are devices that enable pivoting/lateral-movement in attacks: gateways. Indeed, the interim result of the VCRWG is that there are multiple likely present devices in modern heavy duty vehicle which are gateway devices.

This experimental capture of the requirements as ``strictdoc`` ``STATEMENT`` blocks was performed because the completion of the work by the RFPCTL working group yielded a large number of requirements that need to be periodically updated, refined, reviewed etc. And furthermore the requirements need to be processed on each release to produce printable references and questionnaires for use by the fleets in the procurement processes. We expect that by the completion of the work by the VCRWG that there will be even more requirements to manage in ongoing releases and to produce more products such as in the TSRM. It is clear that machine readable form for specifying the requirements is necessary. An alternative considered was `doorstop` but the multi-file approach of doorstop was estimated to cause more friction in development and review of the requirements by the VCRWG.
