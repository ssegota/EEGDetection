
# EEGDetection

## Introduction

This is a project that uses Emotiv EPOC neuroheadset for detecting waves in a certain frequency band and raising an audio alarm if their intensity is higher then a threshold determined. Further explanation can be found in pdf that's part of the repository - PDF is in Croatian, translation might be necessary.
Project was created as part of Assistive Technology class, under the Assistive Technology Laboratory at the Faculty of Engineering Rijeka.

## Requirements

To properly work with the device used all the software is required to be 32 bit versions.

* Python 2.7
..* SciPy 0.9.0 
..* NumPy 1.0.1
* OpenVibe 1.2.2
* Emotiv Research Edition SDK v2.0.0.20

### Recommended

*Emotiv Xavier Pure EEG 3.4.3 (Will assist with positioning the headset and confirming proper signal acquisition)

## Instructions

Use OpenVibe Designer to open the xml file. Load the Python script in it. [instrutions can be found here](http://openvibe.inria.fr/tutorial-using-python-with-openvibe/)
Open OpenVibe Acquisition Server to connect and pass the data. Follow the instructions here: [Acquisition Server Tutorial](http://openvibe.inria.fr/how-to-connect-emotiv-epoc-with-openvibe/)
Connect your headset and confirm the data is received. Run the software. You might need to adjust the **threshold** variable, as well as **cutoff** and **cutoff2** variables which present low and high pass frequenicies in the Python script.
