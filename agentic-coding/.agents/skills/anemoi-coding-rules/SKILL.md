---
name: anemoi-coding-rules
description: Guidelines and best practices for writing code in Anemoi packages.
---

## Object-oriented design

Use object-oriented programming (OOP) principles to design your code.

Follow the SOLID principles of object-oriented design:

- **S**ingle Responsibility Principle: A class should have only one reason to change. Each class should be responsible for a single part of the software's functionality.
- **O**pen/Closed Principle: Software entities should be open for extension but closed for modification. You should be able to add new functionality without changing existing code.
- **L**iskov Substitution Principle: Subclasses must be usable in place of their base class without changing the correctness of the program.
- **I**nterface Segregation Principle: Clients should not be forced to depend on interfaces they do not use. Create focused, client-specific interfaces.
- **D**ependency Inversion Principle: Depend on abstractions, not on concrete implementations. High-level modules should not depend on low-level modules.

The logic of your program should be organized around abstract concepts and the relationships between them. Example: the inference pipeline gets its initial condition from an `Input` and produces an `Output`. The `Input` and `Output` classes encapsulate the data and behaviour of the input and output of the pipeline, respectively. The pipeline itself is a class that orchestrates the flow of data between the `Input` and `Output` classes. Concrete implementations of `Input` and `Output` can be created for different data sources and formats, allowing the pipeline to be reused in different contexts without changing its core logic.

Prefer composition (has-a) over inheritance (is-a). Keep each class focused on a single responsibility. Do not create unnecessary classes or hierarchies. Use dependency injection to decouple classes and make them easier to test.

Do not create classes when a simple function or a data structure would suffice. Avoid over-engineering and premature optimization. Keep your code simple, readable, and maintainable. When the design genuinely requires shared contracts across multiple implementations, use abstract base classes to define interfaces and enforce those contracts.


**Inheritance from instantiated classes:** Never inherit directly from a class that is also instantiated. If you need to share behaviour between an existing instantiated class and a new class, extract a common abstract base class and have both inherit from it.

**Factory pattern for configuration-driven object creation:** When creating objects from configuration files, use a factory. This decouples object creation from the rest of the code and makes it straightforward to add new types later.

Do not select a class based on whether a module can be imported successfully — that module may be unavailable at inference time. Use a factory driven by explicit configuration, and raise a clear exception when a required module is missing.


## No premature optimization

The code must (in order of importance):
- Run (does not crash)
- Be correct (produces the expected results)
- Be maintainable (easy to understand, modify, and extend)
- Be fast (only if it is too slow and does not compromise correctness or maintainability)



## Use of mixins

Although mixins can be useful for code reuse, they can also lead to complex and hard-to-maintain class hierarchies. Use a mixin only when it adds new methods without overriding any base-class methods and is shared by at least two unrelated class hierarchies; otherwise use composition or delegation. Python's preference for the leftmost base class in method resolution order (MRO) can lead to unexpected behaviour when using mixins. Avoid creating mixins that override methods from the base class, as this can lead to confusion and bugs.

## Environment variables

Do not use environment variables to configure model-related settings (e.g. number of layers, learning rate, architecture choices). Environment variables are acceptable only for operational concerns that do not affect the model itself (e.g. logging level, number of workers, etc). Document every environment variable and provide a default value. Log the value of every environment variable your code reads.

Model and graphs related settings (in order of preference):
1. Configuration files
2. Default values in code

All other (non-model, non-graph) settings, including operational concerns (in order of preference):
1. Command-line arguments
2. Environment variables
3. Configuration files
4. Default values in code

## Configuration files

Define the structure and validation of configuration files with pydantic models. Use pydantic's built-in validation to enforce constraints and produce clear error messages when validation fails.

## Calling external commands

Prefer the Python standard library over external commands (`os.mkdir` instead of `mkdir`, `shutil.rmtree` instead of `rm -rf`, etc.). When you must run an external command, use the `subprocess` module — never `os.system()` or similar. Handle errors and exceptions, and validate any input passed to the command.
