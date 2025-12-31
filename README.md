# License Classifier

A research-driven project for **automatic identification, similarity analysis, and classification of open-source software licenses**, with a focus on **SPDX licenses and license exceptions**.

This repository implements and compares **lexical**, **semantic**, and **hybrid** approaches to license analysis, following best practices and gaps identified in recent FOSS license research.

---

## Features

- Canonical SPDX license dataset (ScanCode LicenseDB)
- **TF-IDF (character n-grams)** similarity baseline
- **SBERT semantic similarity** with legal-aware chunking
- **Hybrid TF-IDF + SBERT reranking** (best-performing approach)
- Cluster visualization (PCA + t-SNE)
- Structural evaluation metrics (family-level accuracy, Top-K recall)
- Exported prediction results (JSON)

---

## Project Objectives

- Map license texts to **SPDX identifiers**
- Study **license similarity** beyond exact text matching
- Analyze:
  - SPDX family cohesion
  - License exception proximity
  - Legal category clustering
- Evaluate why **pure ML** struggles with SPDX taxonomy
- Build a foundation for:
  - license variant detection
  - compliance tooling
  - human-in-the-loop review

---

## Dataset

**Source:** ScanCode LicenseDB (canonical license texts)

Each cleaned entry includes:
- `id` – internal identifier
- `target_spdx` – SPDX license or exception ID
- `legal_cat` – legal category (Permissive, Copyleft, etc.)
- `is_exception` – SPDX exception flag
- `content` – raw license text
- `cleaned_content` – normalized text

> This dataset uses **canonical license texts**, not real-world repository files.

---

## Implemented Methods

### 1️⃣ TF-IDF Similarity (Lexical Baseline)

- Character-level TF-IDF (`char_wb`, n-grams 4–8)
- Cosine similarity + nearest neighbors

**Strengths**
- Robust to formatting changes
- Excellent for boilerplate detection
- Fast and interpretable

**Limitations**
- Weak semantic understanding
- Poor exact SPDX classification
- Overlapping SPDX families

---

### 2️⃣ SBERT Semantic Similarity

- Model: `sentence-transformers/all-MiniLM-L6-v2`
- Paragraph / clause-level chunking
- Max-pool aggregation

**Strengths**
- Captures legal meaning
- Groups licenses by obligations and permissions

**Limitations**
- SPDX families are **not semantic categories**
- High semantic similarity across different families

---

### 3️⃣ Hybrid TF-IDF + SBERT (Best Model)

**Pipeline**
1. TF-IDF retrieves Top-K lexical candidates
2. SBERT reranks candidates semantically

**Why it works**
- TF-IDF enforces **taxonomy awareness**
- SBERT refines by **legal meaning**
- Reduces spurious semantic matches

**Outcome**
- Best family-level accuracy
- High Top-K recall
- Most realistic for compliance workflows

---

## Evaluation Metrics

Exact Top-1 SPDX accuracy is **not realistic**, so we evaluate structure instead:

- Family-level Top-1 accuracy
- Top-K family recall
- Silhouette score (family labels)
- Mean same-family vs cross-family similarity
- PCA + t-SNE visual inspection

**Key Insight**
> Legal categories cluster better than SPDX families — SPDX is a *legal taxonomy*, not a semantic one.

---

## Repository Structure

```text
.
├── cleaned_research_dataset.json
├── tfidf_nn_predictions.json
├── sbert_nn_predictions.json
├── hybrid_tfidf_sbert_predictions.json
├── main.ipynb
└── README.md