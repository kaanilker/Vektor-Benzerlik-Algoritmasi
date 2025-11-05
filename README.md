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
\text{distance} = \sqrt{(A_1 - B_1)^2 + (A_2 - B_2)^2 + (A_3 - B_3)^2}
\]

The maximum possible distance in this 3D 0–100 color space is:

\[
\sqrt{100^2 + 100^2 + 100^2}
\]

Finally, similarity is:

\[
\text{similarity} = 1 - \frac{\text{distance}}{\text{max\_distance}}
\]

---

## 🧠 Functions Overview

| Function | Description |
|---------|-------------|
| `arrange(item, dim, min, max)` | Normalizes each RGB component into the 0–100 range. |
| `kokal(x)` | Computes the square root of `x`. |
| `usal(x, level)` | Raises `x` to the specified power. |
| `normalize(renk)` | Wrapper for `arrange()` to normalize an RGB vector. |
| `vectorSimilarty(A, B)` | Computes the Euclidean-based similarity score between two normalized color vectors. |

---

## 🎯 Example Output

```python
print(normalize([82, 82, 82]))   # Normalized gray
benzerlik_orani = vectorSimilarty(normalize(kirmizi), normalize(koyuKirmizi))
print("%", benzerlik_orani * 100)
