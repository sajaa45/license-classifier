# License Classifier

A **research-driven project** for **automatic identification, similarity analysis, and retrieval-based classification of open-source software licenses**, with a focus on **canonical SPDX licenses** under **extreme label sparsity**.

This repository implements, evaluates, and explains **lexical**, **semantic**, and **hybrid similarity-based methods**, and demonstrates why **supervised machine learning classifiers are structurally unsuitable** for canonical SPDX license identification.

---

## Core Contributions

* Formalize SPDX license identification as a **one-shot retrieval problem**
* Demonstrate the **failure of supervised classification** under SPDX taxonomy
* Show that **similarity-based NLP methods outperform classifiers**
* Propose a **hybrid TF-IDF + SBERT pipeline** approaching industry-grade accuracy
* Provide **explainable similarity signals** suitable for compliance workflows

---

## Features

* Canonical **SPDX License List** dataset (680 licenses)
* **TF-IDF (character n-grams)** lexical similarity baseline
* **SBERT semantic similarity** with legal-aware chunking
* **Hybrid TF-IDF + SBERT reranking** (best-performing NLP method)
* Supervised baselines (Random Forest, SVM, Logistic Regression) for failure analysis
* Embedding-space visualization (PCA + t-SNE)
* Structural evaluation metrics (family-level accuracy, similarity separation)
* Exported predictions and similarity scores (JSON)

---

## Project Objectives

* Map license texts to **SPDX identifiers at family level**
* Analyze **license similarity** beyond exact text matching
* Study:

  * SPDX family cohesion
  * Semantic vs lexical separation
  * Copyleft vs permissive clustering
* Explain why **pure supervised ML fails** on canonical license data
* Lay foundations for:

  * license variant detection
  * explainable compliance tooling
  * human-in-the-loop license review

---

## Dataset

**Source:** SPDX License List (canonical reference texts)

> This project intentionally uses **canonical licenses only**, not real-world repository files.

### Dataset Characteristics

* 680 SPDX licenses
* One canonical text per license (≈ one per family)
* No formatting noise, no variants, no embedded licenses

### Stored Fields

* `spdx_id` – SPDX license identifier
* `family` – normalized license family (e.g., GPL, MIT)
* `name` – human-readable license name
* `text` – full canonical license text
* `cleaned_text` – normalized text used for modeling

⚠️ **Key Constraint:**
Extreme label sparsity (≈1 sample per family) makes supervised learning fundamentally ill-posed.

---

## Implemented Methods

### 1️⃣ TF-IDF Similarity (Lexical Baseline)

* Character-level TF-IDF (`n=3–5`)
* Cosine similarity + nearest-neighbor retrieval

**Strengths**

* Robust to formatting differences
* Captures boilerplate legal language
* Fast and interpretable

**Limitations**

* Weak semantic discrimination
* Strong overlap between SPDX families
* Moderate family-level accuracy only

---

### 2️⃣ SBERT Semantic Similarity

* Model: `sentence-transformers/all-MiniLM-L6-v2`
* Paragraph-level chunking
* Max-pooling aggregation

**Strengths**

* Captures legal semantics
* Separates copyleft vs permissive licenses
* Strong one-shot retrieval performance

**Limitations**

* High similarity across permissive families
* Fine-tuning yields marginal gains due to dataset size

---

### 3️⃣ Hybrid TF-IDF + SBERT (Best NLP Method)

**Two-stage pipeline**

1. TF-IDF retrieves top-K lexical candidates
2. SBERT reranks candidates semantically

**Why it works**

* TF-IDF enforces **lexical and taxonomic filtering**
* SBERT refines matches by **legal meaning**
* Avoids semantic false positives

**Outcome**

* Best NLP-based family-level accuracy
* 100% detection rate
* Strong explainability via nearest neighbors

---

### 4️⃣ Supervised Classification (Failure Baseline)

Models evaluated:

* Random Forest
* Support Vector Machine
* Logistic Regression

**Result**

* High training accuracy
* Near-random test performance

**Conclusion**

> Supervised classifiers fail structurally due to extreme label sparsity.
> Canonical SPDX license identification is **not a classification problem**.

---

## Evaluation Strategy

Exact SPDX ID prediction is **not realistic** for canonical data.
Evaluation focuses on **structural correctness and retrieval behavior**.

### Metrics Used

* Family-level Top-1 accuracy
* Detection rate
* Mean same-family vs cross-family similarity
* Silhouette score (family labels)
* PCA + t-SNE embedding inspection

**Key Insight**

> SPDX families are a **legal taxonomy**, not a semantic partition.
> Similarity-based retrieval aligns better with this structure than classification.

---

## Repository Structure

```text
.
├── cleaned_spdx_dataset.json
├── tfidf_predictions.json
├── sbert_predictions.json
├── hybrid_predictions.json
├── supervised_baselines.json
├── plots/
│   ├── tfidf_tsne.png
│   └── sbert_tsne.png
├── main.ipynb
└── README.md
```

---

## Takeaway

This project shows that:

* **Similarity-based retrieval** is the correct paradigm for SPDX license identification
* **Hybrid lexical + semantic pipelines** outperform pure ML
* **Explainability** is a first-class requirement for legal NLP systems

The results generalize beyond licenses to other **canonical legal documents** such as contracts, regulations, and policy texts.
