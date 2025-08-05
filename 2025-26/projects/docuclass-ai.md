# DocuClassAI: Lightweight Language Models for Intelligent Planning Document Classification

## Project Summary

As part of its drive to modernise local government services, **IEG4** and **Agile Applications** are developing intelligent tools to support the **planning application process**. One key inefficiency is the **manual classification of supporting documents**, such as:

* Fire Statements
* Environmental Impact Assessments
* Transport Assessments
* Design and Access Statements
* *...and others*

These documents are often submitted in **varied formats** (PDF, DOCX) and exhibit **high variability in length, structure, and terminology**—making traditional rule-based classification unreliable.

This project proposes the development of a **document classification system** using **lightweight open-source language models (LLMs)** to automatically determine the type of each planning-related document. The solution must be **deployable on local infrastructure**, ensuring **GDPR compliance** and **operational efficiency**.

---

## Project Objectives

* Develop a **robust preprocessing pipeline** to extract usable text from diverse document formats (PDFs, DOCX, scanned files).
* Fine-tune or adapt a **lightweight LLM-based classifier** to assign document types from a predefined taxonomy.
* Ensure the model performs **efficiently under constrained compute environments**, without reliance on commercial APIs.
* Return a **document type label and confidence score** for each processed input.
* Package the system into a **deployable local tool** (e.g., CLI or REST API) for integration with IEG4’s digital platforms.

---

## Technical Scope

The project will involve:

* **Preprocessing** a provided corpus of planning documents, including:

  * Text extraction using tools like `pdfminer.six`, `PyMuPDF`, or `textract`
  * Handling OCR for scanned documents (e.g., with **Tesseract**)
  * Cleaning and normalising extracted text (removing headers, footers, artifacts)

* **Training or adapting** a compact transformer model (e.g., **DistilBERT**, **MiniLM**, or **BERT + linear head**) for multi-class document classification.

* **Evaluating performance** using:

  * Accuracy
  * Precision / Recall
  * F1-score per document type

* **Optimising for**:

  * Low-latency inference
  * Minimal memory usage
  * On-premise deployability

* *(Optional)*: Building a **minimal web UI or dashboard** for demonstration.

---

## Learning Outcomes

Students will:

* Gain hands-on experience in **natural language processing**, **LLMs**, and **text classification**.
* Learn practical skills in **document preprocessing and OCR** under real-world constraints.
* Understand how to **integrate AI pipelines into civic digital services**, with attention to **performance** and **compliance**.
* Build **deployable**, **explainable AI tools** aligned with the needs of **public sector digital transformation**.

---

## Real-World Impact

This system will **significantly reduce the manual burden** on planning officers, allowing **faster triage** and **improved consistency** in document handling.

By applying **state-of-the-art NLP** in a **resource-conscious** and **context-aware** way, the project demonstrates how **responsible AI engineering** can deliver **practical value** to local governments and their communities.

---

## Apply or Ask Questions
[📨 Click here to apply](https://github.com/fabriziocosta/projects-supervision/issues/new?template=application.yml&labels=application,project:docuclass-ai&title=Application:%20[Your%20Name]%20for%20docuclass-ai)


## Current Status
🟢 Accepting interest — 0/5 students
