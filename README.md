# Plagiarism Detector Lab 2

A user-friendly, console-based plagiarism detector for comparing two essays in `.txt` format.

---

## 🚀 How to Use

1. **Requirements:** Python 3.9 or newer.
2. **Prepare your files:** Place `essay-1.txt` and `essay-2.txt` in the same folder as `plagiarism_detector.py`.
3. **Run the program:**
   ```sh
   python plagiarism_detector.py
   ```
4. **View the results:**
   - Essay statistics (total and unique words)
   - Table of common words and their frequencies
   - Plagiarism percentage and detection result
   - **Search for any word**: After the plagiarism check, you can interactively search for any word to see how many times it appears in each essay.
---

## ✨ Features
- **Automatic essay loading** (`essay-1.txt` and `essay-2.txt`)
- **Preprocessing:** Removes punctuation, lowercases, and splits text into words
- **Word frequency analysis** for each essay
- **Common words table** with counts from both essays
- **Plagiarism percentage calculation** using set intersection/union
- **Friendly, readable console output**
- **Interactive word search**: Enter any word after the plagiarism check to see its count in both essays
- **Robust error handling** for missing or empty files

---

## 🖥️ Example Output
```
==============================
    Plagiarism Detector Lab 2
==============================
Compare two essays for common words and plagiarism percentage.

Essay 1 Statistics:
  Total words: 93
  Unique words: 64

Essay 2 Statistics:
  Total words: 102
  Unique words: 73

Common Words:
Word           Essay 1   Essay 2
-------------------------------------
... (table of words) ...

Checking for plagiarism...
Plagiarism Percentage: 19.13%
Result: No Plagiarism Detected.

--- Word Search ---
Type a word to search for its count in both essays, or 'q' to quit.
Enter word to search: innovation
The word 'innovation' appears 1 time(s) in Essay 1 and 1 time(s) in Essay 2.
Enter word to search: q
Exiting word search.

Thank you for using the Plagiarism Detector!
```

---

## 📦 File Structure
```
Plagiarism Detector/
├── plagiarism_detector.py
├── essay-1.txt
├── essay-2.txt
└── README.md
```

---

## 👤 Credits
- **Author:** [Your Name]
- **Student ID:** [Your Student ID]
- **Date:** [Submission Date]

---

For any issues or suggestions, feel free to contact the author.
