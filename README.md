# Color Vector Similarity Calculator (Python)

This script calculates the **similarity between two colors** based on their RGB values. Each color is represented as a 3-dimensional vector, which is then **normalized** and compared using a **Euclidean distance**-based similarity metric.

---

## 🎨 What the Program Does

1. Takes predefined RGB color vectors (e.g., Red, Black, Gray).
2. Normalizes each color value to a **0–100** scale.
3. Computes the **Euclidean distance** between two normalized color vectors.
4. Converts that distance into a **similarity score** between **0 and 1**.
5. Outputs the similarity as a **percentage**.

---

## 🧩 How Similarity Is Calculated

After normalization:

\[
\text{distance} = \sqrt{(A_1 - B_1)^2 + (A_2 - B_2)^2 + (A
