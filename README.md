## 📌 Project Overview

The system is designed with a modular architecture:

Video Upload Module – Provides an API and web interface for uploading videos.

OpenFace Processing Module – Uses OpenFace
 to extract Action Units, head pose, gaze, and facial landmarks.

Result Manager – Aggregates extracted features and stores processed data.

Machine Learning Module – Consumes extracted features and applies ML models (e.g., Random Forest, Decision Trees) to classify emotional states.

**Middleware Module (this repo) – The central hub that connects all modules, orchestrates processing requests, and manages communication.**

This repository contains only the Middleware Module, which ensures smooth communication between services and coordinates the workflow.

## 🚀 Features

RESTful API with FastAPI

Communication with the OpenFace processing service

Manages processing requests and collects results

Containerized with Docker for deployment

## 🔗 About OpenFace

This system relies on OpenFace, an open-source tool for facial behavior analysis.
OpenFace enables the extraction of:

Action Units (AU01, AU04, AU06, AU12, etc.)

Head pose (Tx, Ty, Tz, Rx, Ry, Rz)

Eye gaze vectors and gaze angles

Facial landmarks (68-point model)

The Middleware Module does not perform feature extraction itself, but relies on OpenFace results to manage higher-level workflows.

## 📖 Citation

This project relies on [OpenFace](https://github.com/TadasBaltrusaitis/OpenFace) for facial feature extraction.  
If you use this project in your research, please cite OpenFace as follows:

Baltrušaitis, T., Zadeh, A., Lim, Y. C., & Morency, L. P. (2018).  
**OpenFace 2.0: Facial behavior analysis toolkit.**  
*2018 13th IEEE International Conference on Automatic Face & Gesture Recognition (FG 2018)*, 59–66. IEEE.

