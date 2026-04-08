# Quality Analysis

## ISO/IEC 25010 Quality Attributes

### 1. Functional Correctness

Functional correctness refers to the degree to which a system provides accurate and correct results when given valid inputs. For a calculator application, this is the most critical quality attribute since users depend entirely on the system to produce mathematically accurate outputs.

This calculator handles a range of operations such as addition, subtraction, multiplication, and division, including support for decimal numbers and chained operations. Each of these operations must produce the exact expected result without deviation. For instance, entering `1.5 + 2.5` must always return `4`, and chaining `10 * 2 + 5` must correctly evaluate the intermediate result before applying the next operator.

Functional correctness also extends to how the system handles invalid inputs. Dividing by zero is a mathematically undefined operation, and the calculator correctly identifies this and returns an `Error` state rather than crashing or producing a misleading result. The system also prevents nonsensical input sequences such as pressing an operator before any number has been entered, or stacking multiple operators without an intermediate operand.

### 2. Reliability

Reliability refers to the degree to which a system performs its required functions under stated conditions over a period of time without failure. In the context of this calculator, reliability means that the application behaves consistently and predictably across all input sequences, including normal usage, boundary conditions, and erroneous inputs.

A key aspect of reliability in this module is state management. The calculator maintains an internal state machine with four states such as `left`, `op`, `right`, and `error`. Each state transition is strictly controlled so that the system never enters an undefined or inconsistent state. For example, after an error occurs, all further input is blocked until the user explicitly clears the display, preventing corrupted calculations from silently continuing.

Reliability also covers recovery behavior. The system provides a clear recovery path from the error state through the `clear()` method, which fully resets all internal state back to its initial values. This ensures that after any failure condition, the calculator is always recoverable and ready for fresh input.

---

## How Testing Supports These Attributes

The test suite in `tests/test_calculator.py` directly validates both quality attributes through 14 automated test cases organized into positive, negative, and edge case categories.

Functional correctness is validated through positive test cases such as `test_basic_addition`, which verifies that `12 + 3` produces `15`, and `test_chained_operations`, which confirms that `10 * 2 + 5` correctly evaluates to `25` by carrying the intermediate result forward. Decimal correctness is covered by tests such as `test_decimal_addition` and `test_decimal_less_than_one`, ensuring that float arithmetic such as `0.5 + 0.3` returns `0.8` as expected.

Reliability is validated through negative and edge case tests. `test_division_by_zero` confirms that the system returns `Error` rather than crashing. `test_input_blocked_after_error` verifies that the error state correctly blocks further input. Edge cases such as `test_operator_without_left_number`, `test_replacing_operator`, and `test_clear_resets_state` confirm that the state machine handles boundary conditions without entering an inconsistent state. `test_duplicate_decimal_ignored` ensures that pressing the decimal point multiple times on the same operand does not corrupt the number being built.

By covering these scenarios systematically, the test suite provides confidence that both correctness and reliability hold across the full range of expected and unexpected usage patterns.

---

## How CI/CD Improves Reliability

The GitHub Actions pipeline defined in `.github/workflows/ci.yml` automates the execution of the full test suite on every push to the main branch. This continuous integration approach improves reliability in several important ways.

First, it eliminates the risk of human error in the testing process. Without CI, a developer might forget to run the tests before pushing, allowing a regression to reach the repository undetected. With the pipeline in place, tests are always executed automatically and any failure immediately blocks the commit from being considered stable.

Second, the pipeline provides a consistent and reproducible test environment. Tests run on a clean Ubuntu runner with a fixed Python version, meaning results are not affected by differences in local machine configurations. This ensures that a test passing on one developer's machine will also pass in the pipeline, and vice versa.

Third, the pipeline installs dependencies from `requirements.txt` before running tests, ensuring that the correct versions of all libraries are present. This prevents environment drift where a test might pass locally due to a previously installed package that is not declared as a dependency.

Finally, the visible green check on each commit in GitHub provides a clear and immediate signal of the system's health. Any change that breaks existing functionality will cause the pipeline to fail, making regressions visible and traceable to the exact commit that introduced them. This feedback loop reinforces both functional correctness and reliability as ongoing properties of the codebase rather than one-time verifications.
