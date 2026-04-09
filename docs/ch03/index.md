# Chapter 2: Python Intermediate

This chapter deepens your understanding of Python with topics like dynamic typing, numeric and string internals, iteration protocols, closures, scope rules, and performance fundamentals.

## 2.1 Variables and Naming

- [Name Binding in Python](variables/name_binding.md)
- [Assignment Mechanics](variables/assignment.md)
- [Shorthand Operators](variables/shorthand_operators.md)
- [Simultaneous Assignment](variables/simultaneous_assignment.md)
- [Chained Assignment](variables/chained_assignment.md)
- [Naming Constraints](naming/naming_constraints.md)
- [Unicode Identifiers](naming/unicode_identifiers.md)
- [Underscore Convention](naming/underscore_convention.md)
- [Bad Naming Practices](naming/bad_practices.md)
- [Reserved Keywords](naming/keywords.md)
- [Built-in Names](naming/builtins.md)

## 2.2 Dynamic Typing

- [Static vs Dynamic Typing](typing/static_vs_dynamic.md)
- [Dynamic Typing Basics](typing/dynamic_typing.md)
- [Type Conversion](typing/type_conversion.md)
- [Type Introspection](typing/type_function.md)

## 2.3 Numeric Types Deep Dive

- [int Python vs C](numerics/int_python_vs_c.md)
- [int Bitwise Operations](numerics/int_bitwise_operations.md)
- [int Number Systems](numerics/int_number_systems.md)
- [float Python vs C](numerics/float_python_vs_c.md)
- [float IEEE 754 Standard](numerics/float_ieee754.md)
- [float Numerical Errors](numerics/float_numerical_errors.md)
- [float Special Values](numerics/float_special_values.md)
- [Type Promotion](numerics/type_promotion.md)

## 2.4 Boolean Deep Dive

- [bool Subclass of int](bool/bool_subclass_int.md)
- [Short-Circuit Evaluation](bool/short_circuit.md)
- [and/or Return Values](bool/and_or_return_values.md)
- [bool Applications](bool/bool_applications.md)

## 2.5 String Internals

- [str ASCII and Unicode](strings/str_ascii_unicode.md)
- [str UTF-8 Encoding](strings/str_utf8_encoding.md)
- [str Encode and Decode](strings/str_encode_decode.md)
- [str Immutability](strings/str_immutability.md)
- [str Align Methods](strings/str_align_methods.md)
- [str Format Specifiers](strings/str_format_specifiers.md)
- [F-String Debugging](strings/fstring_debugging.md)

## 2.6 Composite Types Deep Dive

- [Shallow and Deep Copying (copy module)](composites/list_copying.md)
- [Nested Data Structures](composites/nested_structures.md)
- [tuple Optimization](composites/tuple_optimization.md)
- [dict Internals (Hash Tables)](composites/dict_internals.md)
- [dict Ordering Guarantees](composites/dict_ordering.md)
- [dict Merge Operators](composites/dict_merge_operators.md)
- [set Internals](composites/set_internals.md)
- [Time Complexity of Operations](composites/time_complexity.md)

## 2.7 Iteration Protocol

- [Iterables and Iterators](iteration/iterables.md)
- [Generators and yield](iteration/generators.md)
- [yield from](iteration/yield_from.md)
- [StopIteration Mechanics](iteration/stopiteration.md)
- [Lazy Evaluation Patterns](iteration/lazy_evaluation.md)
- [Iterator Chaining](iteration/iterator_chaining.md)

## 2.8 Advanced Built-ins

- [The builtins Namespace](advanced_builtins/builtins_namespace.md)
- [sorted() Advanced (key, stability)](advanced_builtins/sorted.md)
- [id(), type(), isinstance()](advanced_builtins/introspection.md)

## 2.9 Operators Deep Dive

- [Operators Overview](operators/operators_deep_dive_overview.md)
- [Arithmetic Operators](operators/arithmetic.md)
- [Comparison Operators](operators/comparison.md)
- [Sequence Comparison](operators/sequence_comparison.md)
- [Identity Operators](operators/identity.md)
- [Membership Operators](operators/membership.md)
- [Precedence and Associativity](operators/precedence.md)
- [Walrus Operator (:=)](operators/walrus_operator.md)

## 2.10 Exceptions Deep Dive

- [Custom Exceptions](exceptions/custom_exceptions.md)
- [assert Statement](exceptions/assert.md)
- [Compile vs Runtime Errors](exceptions/compile_vs_runtime.md)

## 2.11 File I/O Deep Dive

- [Binary Files](io/binary_files.md)
- [pickle and Serialization](io/pickle.md)
- [io.StringIO and io.BytesIO](io/string_bytes_io.md)
- [tempfile Module](io/tempfile.md)
- [Encoding Issues](io/encoding_issues.md)
- [shelve Module](io/shelve.md)

## 2.12 Scope and Namespace

- [LEGB Resolution](scope/legb_resolution.md)
- [global and nonlocal](scope/global_nonlocal.md)
- [Scope Lifetime](scope/scope_lifetime.md)

## 2.13 Function Parameters

- [Call-by-Object-Reference](functions_params/call_by_object_reference.md)
- [Parameter Mechanisms](functions_params/parameter_mechanisms.md)
- [Default Parameter Gotcha](functions_params/default_parameter_gotcha.md)
- [Parameter Passing](functions_params/parameter_passing.md)
- [Parameter Best Practices](functions_params/best_practices.md)

## 2.14 Closures

- [Closure Fundamentals](closures/closure_fundamentals.md)
- [Late Binding](closures/late_binding.md)
- [nonlocal and Mutation](closures/nonlocal_mutation.md)
- [Scoping Rules](closures/scoping_rules.md)
- [Practical Patterns](closures/practical_patterns.md)
- [Closures Cheat Sheet](closures/closures_cheat_sheet.md)

## 2.15 Performance Basics

- [Time vs Space Trade-offs](performance/tradeoffs.md)
- [Big-O Notation](performance/big_o.md)
- [Python Operation Costs](performance/operation_costs.md)
- [timeit Module](performance/timeit.md)
