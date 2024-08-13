# IoT Policy Language Tutorial Summary

## Introduction

This tutorial explains how to convert English statements into an easily parseable policy language for IoT defenses using logical expressions and variables.

## Logical Expressions and Variables

- Use logical expressions for statements like "If Fire Sprinkler is on, then Water Valve is on."
- Improve readability by assigning expressions to variables.

## Device Attributes

- Utilize various device attributes in logical expressions.

## Functions

- Incorporate functions like `timer(logical_expression)` to handle time-related conditions.

## Logical Operators

- Employ operators such as `and`, `or`, and `not` for combining multiple expressions.

## Unique Policies

### Policies with "Only If"

- Statements like "X only if Y" are equivalent to "If X Then Y."

### Policies with "Allow"

- Convert "Allow" statements to standard policy format.

### Policies with "Deny"

- Remove "Deny" and use the `not` operator for the conclusion.

### Policies with "when"

- "when" is equivalent to "if". Consider "when" as "if" and apply standard translation rule.

### Temporal Operators

- Use operators like **since** and **yesterday** for temporal logic.

### Perpetually Valid

- Ensure consistency with the `true` keyword for perpetually valid expressions.

## Conclusion

By following these guidelines, you can effectively translate natural language statements into a policy language suitable for IoT defenses.