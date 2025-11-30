# ✨ SOLID design principles ✨

This repository contains Coding Exercise that violate the SOLID principles:

1. Single Responsibility Principle: Every class should have a single responsibility. A class should have one, and only one, reason to change.
Exercises: 
* [Exercise 1](1.Srp)

2. Open/Closed Principle: You should be able to extend a classes behavior, without modifying it. Software entities should be open for extension, but closed for modification.
* [Exercise 1](2.Ocp)

3. Liskov Substitution Principle: Derived classes must be substitutable for their base classes. Functions that use references to base classes must be able to use objects of derived classes without knowing it.
* [Exercise 1](3.Lsp/)
4. Interface Segregation Principle: Make fine grained interfaces that are client specific. Clients should not be forced to depend on interfaces they do not use.
* [Exercise 1](4.Lsp/)
5. Dependency Inversion Principle: Depend on abstractions, not on concretions. High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.
* [Exercise 1](5.Dip/)
---
# ✨ GOAL ✨

The goal is to modify each example so that it does not violate the corresponding SOLID principle.

You can apply the solution to each problem in a separate branch.

## How to make a solution

### Install Node.js and TypeScript

If you haven't already, install Node.js and TypeScript.

Install Node.js: Download and install the Node.js runtime from Node.js official website. This will also install the Node Package Manager (npm), which is used to install TypeScript.

Install TypeScript: Open a terminal or command prompt and run the following command to install TypeScript globally:

```bash
npm install -g typescript
```
Install and use ts-node for **Run TypeScript Directly**. Install ts-node by running:

```bash
npm install -g ts-node
```
Write solution in folder_name_exercise/main.ts

Then run your TypeScript file directly:

```bash
ts-node folder_name_exercise/main.ts
```
Examples:

```bash
ts-node 1.Srp/main.ts
```

### Testing
Use [Jest](https://jestjs.io/) for testing or anything lib you know for JS

Run
```bash
npm install
```

Write a test in tests/** directory with format *.test.ts files and run cmd bellow to run test:
```bash
npm test
```
This is the sample result 

```
 PASS  tests/Spr/main.test.ts
  Library
    ✓ should add a book to the library (5 ms)
    ✓ should remove a book by title from the library (1 ms)
    ✓ should not remove any book if title not found (2 ms)
    ✓ should return the total number of books in the library (1 ms)
    ✓ should return an empty list when no books are added (1 ms)
  BookSearch
    ✓ should find a book by title (2 ms)
    ✓ should return undefined when no book matches the title (2 ms)
    ✓ should return books by author (2 ms)
    ✓ should return an empty array when no books match the author (2 ms)
    ✓ should return books by publication year (1 ms)
    ✓ should return an empty array when no books match the publication year (2 ms)

----------|---------|----------|---------|---------|-------------------
| File       | % Stmts   | % Branch   | % Funcs   | % Lines   | Uncovered Line #s   |
| ---------- | --------- | ---------- | --------- | --------- | ------------------- |
| All files  | 100       | 100        | 100       | 100       |
| lib.ts     | 100       | 100        | 100       | 100       |
| ---------- | --------- | ---------- | --------- | --------- | ------------------- |
Test Suites: 1 passed, 1 total
Tests:       11 passed, 11 total
Snapshots:   0 total
Time:        1.69 s
Ran all test suites.
```
That all!