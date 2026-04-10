# ADS2025-02-12: Data Structures & Algorithms Course Repository

## 📖 Overview
This repository serves as the centralized codebase for the **Data Structures and Algorithms (DSA)** course at the Belarusian State University of Informatics and Radioelectronics (BSUIR), Spring 2025 semester. It contains:
- Student implementations organized by academic group
- Instructor reference solutions and automated test suites
- Standardized lesson modules covering core algorithmic paradigms and data structures

The project follows a strict directory-to-package mapping convention, enabling straightforward compilation, testing, and academic review.

---

## 📁 Project Structure
```
src/
└── by/
    └── bsuir/
        └── dsa/
            ├── csv2025/                 # Student submissions (Cyrillic directory names)
            │   ├── gr410901/            # Group 410901
            │   ├── gr410902/            # Group 410902
            │   ├── gr451001/            # Group 451001
            │   ├── gr451002/            # Group 451002
            │   ├── gr451003/            # Group 451003
            │   └── gr451004/            # Group 451004
            ├── group410901/             # Student submissions (Latin/Transliterated names)
            ├── group410902/
            ├── group451001/
            ├── group451002/
            ├── group451003/
            └── group451004/
            └── it/
                └── a_khmelev/           # Instructor reference implementations & test harnesses
```

### Key Conventions
| Path Component | Purpose |
|----------------|---------|
| `csv2025/` | Primary submission directory using Cyrillic student surnames. Mirrors official university rosters. |
| `groupXXXXXX/` | Parallel submission directory using Latin/transliterated surnames. Provided for cross-platform compatibility and IDE indexing. |
| `it/a_khmelev/` | Instructor workspace containing reference solutions, baseline tests, and lesson scaffolding. |
| `description.md` | Required per-student documentation file detailing algorithmic approach, complexity analysis, and edge-case handling. |

> 💡 **Package Mapping**: Directory structure directly maps to Java packages.  
> Example: `src/by/bsuir/dsa/csv2025/gr410901/Абакумов/Solution.java` → `package by.bsuir.dsa.csv2025.gr410901.Абакумов;`

---

## 📚 Course Curriculum & Lesson Mapping
Each lesson directory contains task variants (`A`, `B`, `C`) and corresponding JUnit test classes.

| Lesson | Directory | Core Topics | Key Files |
|--------|-----------|-------------|-----------|
| 01 | `lesson01` | Recursion & Memoization | `FiboA.java`, `FiboB.java`, `FiboC.java` |
| 02 | `lesson02` | Greedy Algorithms | `A_VideoRegistrator.java`, `B_Sheduler.java`, `C_GreedyKnapsack.java` |
| 03 | `lesson03` | Trees & Priority Queues | `A_Huffman.java`, `B_Huffman.java`, `C_HeapMax.java` |
| 04 | `lesson04` | Divide & Conquer | `A_BinaryFind.java`, `B_MergeSort.java`, `C_GetInversions.java` |
| 05 | `lesson05` | Advanced Sorting | `A_QSort.java`, `B_CountSort.java`, `C_QSortOptimized.java` |
| 06 | `lesson06` | Sequence DP | `A_LIS.java`, `B_LongDivComSubSeq.java`, `C_LongNotUpSubSeq.java` |
| 07 | `lesson07` | String Algorithms | `A_EditDist.java`, `B_EditDist.java`, `C_EditDist.java` |
| 08 | `lesson08` | Dynamic Programming | `A_Knapsack.java`, `B_Knapsack.java`, `C_Stairs.java` |
| 09 | `lesson09` | Linear Structures | `ListA.java`, `ListB.java`, `ListC.java` |
| 10 | `lesson10` | Queues & Deques | `MyArrayDeque.java`, `MyLinkedList.java`, `MyPriorityQueue.java` |
| 11 | `lesson11` | Sets & Hashing | `MyHashSet.java`, `MyLinkedHashSet.java`, `MyTreeSet.java` |
| 12 | `lesson12` | Balanced Trees | `MyAvlMap.java`, `MyRbMap.java`, `MySplayMap.java` |
| 13 | `lesson13` | Graph Algorithms | `GraphA.java`, `GraphB.java`, `GraphC.java` |
| 14 | `lesson14` | Geometry & DSU | `PointsA.java`, `SitesB.java`, `StatesHanoiTowerC.java` |
| 15 | `lesson15` | Lexical Analysis | `SourceScannerA.java`, `SourceScannerB.java`, `SourceScannerC.java` |

---

## 🛠️ Getting Started

### Prerequisites
- **Java Development Kit**: `11` or higher (recommended: `17 LTS`)
- **IDE**: IntelliJ IDEA, Eclipse, or VS Code with Java extensions
- **Build/Run**: Standard `javac`/`java` CLI or IDE run configurations

### Compilation & Execution
```bash
# Compile a specific student solution
javac -d out src/by/bsuir/dsa/csv2025/gr410901/Абакумов/Solution.java

# Run the compiled class
java -cp out by.bsuir.dsa.csv2025.gr410901.Абакумов.Solution
```

> ⚠️ **Encoding Note**: Ensure your terminal/IDE uses `UTF-8` to correctly handle Cyrillic directory and package names.

---

## 📝 Development Workflow & Guidelines

1. **Directory Selection**: Work exclusively within your assigned group folder (`csv2025/` or `groupXXXXXX/`).
2. **File Naming**: 
   - Use `Solution.java` for primary implementations unless the lesson specifies otherwise (e.g., `MyAvlMap.java`).
   - Test files must follow the `*Test.java` naming convention.
3. **Documentation**: Every submission must include a `description.md` containing:
   - Algorithmic strategy
   - Time & space complexity (Big-O)
   - Assumptions & edge cases handled
   - Known limitations or trade-offs
4. **Code Standards**:
   - Follow standard Java naming conventions
   - Include Javadoc for public methods
   - Avoid hardcoded paths or system-specific dependencies
   - Keep implementations self-contained within the lesson package

---

## 🧪 Testing & Validation

- **Test Framework**: JUnit 4/5 (based on `*Test.java` files)
- **Running Tests**:
  ```bash
  # Example: Run all Lesson 04 tests for a student
  java -cp out:lib/junit.jar org.junit.runner.JUnitCore \
    by.bsuir.dsa.csv2025.gr410901.Абакумов.Lesson04Test
  ```
- **Instructor Harness**: Reference tests in `it/a_khmelev/lessonXX/` define expected behavior, input constraints, and output formats. Student implementations must pass these suites without modification.
- **Continuous Validation**: Submissions are expected to compile cleanly and pass all provided test cases before final review.

---

## 📞 Support & Contact
- **Course Instructor**: `a.khmelev` (see `it/a_khmelev/` for reference materials)
- **Academic Groups**: `410901`, `410902`, `451001`, `451002`, `451003`, `451004`
- **Repository Maintainer**: Course Teaching Assistants & Instructors

For technical issues regarding compilation, test failures, or directory structure, consult the `description.md` in your submission folder or raise an issue with the course staff.

---

## 📄 License
This repository is intended strictly for **academic and educational purposes** within the BSUIR DSA curriculum. Code submissions remain the intellectual property of their respective authors. Redistribution or commercial use without explicit permission is prohibited.