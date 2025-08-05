# 🎓 Project Supervision Repository

Welcome to the repository coordinating supervised student projects.

This system provides a **transparent, fair, and structured way** for students to explore, ask questions about, and apply to supervised projects offered each academic year.

---

## 🗂️ Repository Structure

The repository is organised by academic year:

```
.
├── 2024-25/
│   ├── README.md
│   ├── projects/
│   └── .github/
├── 2025-26/
│   ├── README.md
│   ├── projects/
│   └── .github/
├── status.md          ← Live project interest overview (auto-generated)
└── README.md          ← (this file)
```

Each year contains:
- 📄 `README.md` — a welcome page and instructions for that year's students
- 📁 `projects/` — one file per available project
- ⚙️ `.github/ISSUE_TEMPLATE/` — GitHub Issue templates for applications

---

## 🎯 Purpose

This repository is designed to:

- Present the list of **supervised projects** available for a given academic year.
- Allow students to **ask public questions** about specific projects.
- Enable **transparent tracking** of student interest per project.
- Ensure **fair allocation** — not first-come-first-serve.
- Support supervisors in managing applications centrally.

---

## 📈 Live Project Status

To support transparency and prevent oversubscription, the repository includes an automatically updated summary of interest per project:

👉 **[View project interest summary →](./status.md)**

This file shows:
- Number of students who applied to each project
- Maximum number of students that can be supervised
- Updates **hourly** via GitHub Actions based on issue labels

Each time a student applies (using the GitHub issue form), the issue is tagged with a label like `project:smartplan-ai`, which feeds into this status table.

---

## 🧑‍🎓 For Students

1. Navigate to the folder for your academic year (e.g., [2025-26/](./2025-26/))
2. Read the year-specific instructions and explore available projects
3. Click the **"Apply / Ask"** link in any project page to open a GitHub Issue
4. Submit your application or question using the provided form

All applications and questions are **public**, allowing others to benefit from existing answers and ensuring fairness.

---

## 📬 Questions

Please **do not email** the supervisor unless asked to. All communication should happen via GitHub Issues to ensure transparency.

---

## ⚖️ Principles

- **No** first-come-first-serve bias
- Public visibility of interest levels
- Equal opportunity for all students to ask questions
- Final decisions made by the supervisor after reviewing all applications

---
